import fs from "node:fs/promises";
import path from "node:path";

const root = process.cwd();
const manifest = JSON.parse(await fs.readFile(path.join(root, "archive_manifest.json"), "utf8"));
const explanations = JSON.parse(await fs.readFile(path.join(root, "problem_explanations.json"), "utf8"));
const screenshotAudit = JSON.parse(await fs.readFile(path.join(root, "screenshot_audit.json"), "utf8"));
const failures = [];
const readText = (relative) => fs.readFile(path.join(root, relative), "utf8");

if (manifest.length !== 135) failures.push(`Manifest count is ${manifest.length}, expected 135`);
if (screenshotAudit.totals.checked !== 140) failures.push(`Screenshot audit count is ${screenshotAudit.totals.checked}, expected 140`);
if (screenshotAudit.totals.failures !== 0) failures.push(`Screenshot audit reports ${screenshotAudit.totals.failures} failures`);

const problemNumbers = manifest.map((record) => record.problemNumber);
const slugs = manifest.map((record) => record.slug);
if (new Set(problemNumbers).size !== manifest.length) failures.push("Manifest contains duplicate problem numbers");
if (new Set(slugs).size !== manifest.length) failures.push("Manifest contains duplicate HDLBits IDs");
if (problemNumbers.some((number, index) => index > 0 && number <= problemNumbers[index - 1])) {
  failures.push("Manifest is not in strictly increasing problem-number order");
}

const completedScreenshots = screenshotAudit.screenshots.filter((screenshot) => screenshot.status === "Completed");
const reviewScreenshots = screenshotAudit.screenshots.filter((screenshot) => screenshot.status === "Review");
const todoScreenshots = screenshotAudit.screenshots.filter((screenshot) => screenshot.status === "To Do");
if (completedScreenshots.length !== 135) failures.push(`Completed screenshot count is ${completedScreenshots.length}, expected 135`);
if (reviewScreenshots.length !== 1) failures.push(`Review screenshot count is ${reviewScreenshots.length}, expected 1`);
if (todoScreenshots.length !== 4) failures.push(`Captured To Do screenshot count is ${todoScreenshots.length}, expected 4`);

for (const screenshot of screenshotAudit.screenshots) {
  if (!screenshot.complete) failures.push(`Incomplete screenshot audit: ${screenshot.slug}`);
  if (!screenshot.containsTitle || !screenshot.containsModuleDeclaration || !screenshot.containsEditor) {
    failures.push(`Missing required screenshot content marker: ${screenshot.slug}`);
  }
  if (screenshot.status === "Completed" && !screenshot.containsLoadedSolution) {
    failures.push(`Completed screenshot lacks loaded solution: ${screenshot.slug}`);
  }
  if (screenshot.width !== 1043 || screenshot.height < 800) {
    failures.push(`Suspicious screenshot dimensions for ${screenshot.slug}: ${screenshot.width}x${screenshot.height}`);
  }
}

for (const record of manifest) {
  if (!explanations[record.slug]) failures.push(`Missing explanation: ${record.slug}`);
  for (const relative of [record.problemNotePath, record.screenshotPath, record.solutionPath]) {
    try {
      await fs.access(path.join(root, relative));
    } catch {
      failures.push(`Missing file: ${relative}`);
    }
  }
  const solution = await readText(record.solutionPath);
  if (!solution.includes("endmodule")) failures.push(`Invalid solution: ${record.solutionPath}`);
  if (!solution.endsWith("\n")) failures.push(`Solution lacks terminal newline: ${record.solutionPath}`);
  if (/[ \t]+$/m.test(solution)) failures.push(`Solution contains trailing whitespace: ${record.solutionPath}`);
  const problemNote = await readText(record.problemNotePath);
  if (!problemNote.includes(solution.trim())) failures.push(`Problem note code is out of sync: ${record.problemNotePath}`);
  if (record.problemNumber >= 115 && explanations[record.slug].length < 400) failures.push(`New explanation is not deep enough: ${record.slug}`);
}

const readme = await readText("README.md");
for (const record of manifest) {
  for (const target of [record.problemNotePath, record.screenshotPath, record.solutionPath]) {
    if (!readme.includes(encodeURI(target).replaceAll("#", "%23")) && !readme.includes(target)) {
      failures.push(`README is missing archive target: ${target}`);
    }
  }
}

for (const day of Array.from({ length: 6 }, (_, index) => `Day ${String(index + 1).padStart(2, "0")}`)) {
  const dayPage = await readText(`${day}.md`);
  for (const record of manifest.filter((item) => item.day === day)) {
    if (!dayPage.includes(path.basename(record.problemNotePath))) failures.push(`${day}.md is missing ${record.problemNotePath}`);
    if (!dayPage.includes(path.basename(record.screenshotPath))) failures.push(`${day}.md is missing ${record.screenshotPath}`);
  }
}

for (const requiredFile of [
  "outputs/hdlbits-archive/HDLBits_Tracker.xlsx",
  "images/Review/120-lemmings2.png",
  "images/Review/todo-exams__ece241_2014_q7a.png",
  "images/Review/todo-exams__ece241_2014_q7b.png",
  "images/Review/todo-countbcd.png",
  "images/Review/todo-count_clock.png",
]) {
  try {
    await fs.access(path.join(root, requiredFile));
  } catch {
    failures.push(`Missing review/tracker artifact: ${requiredFile}`);
  }
}

const markdownFiles = [
  "README.md",
  "Review.md",
  "REPOSITORY_REVIEW.md",
  ...Array.from({ length: 6 }, (_, index) => `Day ${String(index + 1).padStart(2, "0")}.md`),
  ...manifest.map((record) => record.problemNotePath),
];

for (const relativeFile of markdownFiles) {
  const absoluteFile = path.join(root, relativeFile);
  const content = await fs.readFile(absoluteFile, "utf8");
  if (/[ \t]+$/m.test(content)) failures.push(`Markdown contains trailing whitespace: ${relativeFile}`);
  const linkPattern = /!?\[[^\]]*\]\(([^)]+)\)/g;
  const htmlLinkPattern = /\b(?:href|src)="([^"]+)"/g;
  const targets = new Set([
    ...Array.from(content.matchAll(linkPattern), (match) => match[1]),
    ...Array.from(content.matchAll(htmlLinkPattern), (match) => match[1]),
  ]);
  for (const linkedTarget of targets) {
    const target = linkedTarget.split("#", 1)[0];
    if (!target || /^https?:\/\//i.test(target) || /^mailto:/i.test(target)) continue;
    const decoded = decodeURIComponent(target);
    const resolved = path.resolve(path.dirname(absoluteFile), decoded);
    try {
      await fs.access(resolved);
    } catch {
      failures.push(`Broken link in ${relativeFile}: ${target}`);
    }
  }
}

if (failures.length) {
  console.error(failures.join("\n"));
  process.exitCode = 1;
} else {
  const counts = {};
  for (const record of manifest) counts[record.day] = (counts[record.day] || 0) + 1;
  console.log(JSON.stringify({
    records: manifest.length,
    screenshots: screenshotAudit.totals.checked,
    markdownFiles: markdownFiles.length,
    dayCounts: counts,
    brokenLinks: 0,
    duplicateRecords: 0,
    staleEmbeddedSolutions: 0,
    trailingWhitespace: 0,
  }, null, 2));
}
