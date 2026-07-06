import fs from "node:fs/promises";
import path from "node:path";

const root = path.resolve(import.meta.dirname, "../..");
const internal = path.join(root, "internal");
const manifest = JSON.parse(await fs.readFile(path.join(internal, "archive_manifest.json"), "utf8"));
const explanations = JSON.parse(await fs.readFile(path.join(internal, "problem_explanations.json"), "utf8"));
const screenshotAudit = JSON.parse(await fs.readFile(path.join(internal, "screenshot_audit.json"), "utf8"));
const failures = [];
const readText = (relative) => fs.readFile(path.join(root, relative), "utf8");
const hasInlineImageTarget = (content, target) => Array.from(
  content.matchAll(/!\[[^\]]*\]\(([^)]+)\)/g),
  (match) => match[1],
).includes(target);

const readImageMetadata = (buffer) => {
  if (
    buffer.length >= 24 &&
    buffer.subarray(0, 8).equals(Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]))
  ) {
    return {
      format: "PNG",
      width: buffer.readUInt32BE(16),
      height: buffer.readUInt32BE(20),
    };
  }

  if (buffer.length >= 4 && buffer[0] === 0xff && buffer[1] === 0xd8) {
    const startOfFrameMarkers = new Set([
      0xc0, 0xc1, 0xc2, 0xc3, 0xc5, 0xc6, 0xc7,
      0xc9, 0xca, 0xcb, 0xcd, 0xce, 0xcf,
    ]);
    let offset = 2;
    while (offset + 8 < buffer.length) {
      if (buffer[offset] !== 0xff) {
        offset += 1;
        continue;
      }
      const marker = buffer[offset + 1];
      if (marker === 0xd8 || marker === 0xd9) {
        offset += 2;
        continue;
      }
      const segmentLength = buffer.readUInt16BE(offset + 2);
      if (segmentLength < 2 || offset + segmentLength + 2 > buffer.length) break;
      if (startOfFrameMarkers.has(marker)) {
        return {
          format: "JPEG",
          width: buffer.readUInt16BE(offset + 7),
          height: buffer.readUInt16BE(offset + 5),
        };
      }
      offset += segmentLength + 2;
    }
  }

  return null;
};

if (screenshotAudit.totals.checked !== screenshotAudit.screenshots.length) {
  failures.push(`Screenshot audit count is ${screenshotAudit.totals.checked}, but contains ${screenshotAudit.screenshots.length} records`);
}
if (screenshotAudit.totals.failures !== 0) failures.push(`Screenshot audit reports ${screenshotAudit.totals.failures} failures`);

const problemNumbers = manifest.map((record) => record.problemNumber);
const slugs = manifest.map((record) => record.slug);
if (new Set(problemNumbers).size !== manifest.length) failures.push("Manifest contains duplicate problem numbers");
if (new Set(slugs).size !== manifest.length) failures.push("Manifest contains duplicate HDLBits IDs");
if (problemNumbers.some((number) => !Number.isInteger(number) || number <= 0)) {
  failures.push("Manifest contains an invalid problem number");
}

const completedScreenshots = screenshotAudit.screenshots.filter((screenshot) => screenshot.status === "Completed");
const reviewScreenshots = screenshotAudit.screenshots.filter((screenshot) => screenshot.status === "Review");
const todoScreenshots = screenshotAudit.screenshots.filter((screenshot) => screenshot.status === "To Do");
if (completedScreenshots.length !== manifest.length) {
  failures.push(`Completed screenshot count is ${completedScreenshots.length}, but manifest contains ${manifest.length} records`);
}
if (reviewScreenshots.length !== 0) failures.push(`Review screenshot count is ${reviewScreenshots.length}, expected 0`);
if (todoScreenshots.length !== 0) failures.push(`Captured To Do screenshot count is ${todoScreenshots.length}, expected 0`);

for (const screenshot of screenshotAudit.screenshots) {
  if (!screenshot.complete) failures.push(`Incomplete screenshot audit: ${screenshot.slug}`);
  const moduleDeclarationRequired = !["step_one", "zero"].includes(screenshot.slug);
  if (!screenshot.containsTitle || (moduleDeclarationRequired && !screenshot.containsModuleDeclaration) || !screenshot.containsEditor) {
    failures.push(`Missing required screenshot content marker: ${screenshot.slug}`);
  }
  if (screenshot.status === "Completed" && !screenshot.containsLoadedSolution) {
    failures.push(`Completed screenshot lacks loaded solution: ${screenshot.slug}`);
  }
  if (screenshot.width < 800 || screenshot.height < 700) {
    failures.push(`Suspicious screenshot dimensions for ${screenshot.slug}: ${screenshot.width}x${screenshot.height}`);
  }
  try {
    const image = await fs.readFile(path.join(root, screenshot.screenshotPath));
    const metadata = readImageMetadata(image);
    if (!metadata) {
      failures.push(`Unsupported or corrupt screenshot format: ${screenshot.slug}`);
    } else {
      if (metadata.format !== screenshot.format) {
        failures.push(`Screenshot format mismatch for ${screenshot.slug}: audit ${screenshot.format}, file ${metadata.format}`);
      }
      if (metadata.width !== screenshot.width || metadata.height !== screenshot.height) {
        failures.push(
          `Screenshot dimension mismatch for ${screenshot.slug}: audit ${screenshot.width}x${screenshot.height}, file ${metadata.width}x${metadata.height}`,
        );
      }
    }
    if (image.length !== screenshot.bytes) {
      failures.push(`Screenshot byte-count mismatch for ${screenshot.slug}: audit ${screenshot.bytes}, file ${image.length}`);
    }
  } catch {
    failures.push(`Missing or unreadable screenshot: ${screenshot.screenshotPath}`);
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
  const expectedProblemImage = `../../${record.screenshotPath.split("/").map(encodeURIComponent).join("/")}`;
  if (!hasInlineImageTarget(problemNote, expectedProblemImage)) {
    failures.push(`Problem note does not render its screenshot inline: ${record.problemNotePath}`);
  }
  if (![153, 154].includes(record.problemNumber) && !problemNote.includes(solution.trim())) {
    failures.push(`Problem note code is out of sync: ${record.problemNotePath}`);
  }
  if (record.problemNumber >= 115 && ![151, 152].includes(record.problemNumber) && explanations[record.slug].length < 400) {
    failures.push(`New explanation is not deep enough: ${record.slug}`);
  }
}

const readme = await readText("README.md");
for (const record of manifest) {
  for (const target of [record.problemNotePath, record.screenshotPath, record.solutionPath]) {
    if (!readme.includes(encodeURI(target).replaceAll("#", "%23")) && !readme.includes(target)) {
      failures.push(`README is missing archive target: ${target}`);
    }
  }
}

const archiveDays = [...new Set(manifest.map((record) => record.day))].sort();
for (const day of archiveDays) {
  const dayPage = await readText(`${day}.md`);
  const dayRecords = manifest.filter((item) => item.day === day);
  const inlineCodeBlocks = Array.from(dayPage.matchAll(/^```verilog$/gm)).length;
  if (inlineCodeBlocks !== dayRecords.length) {
    failures.push(`${day}.md has ${inlineCodeBlocks} inline Verilog blocks for ${dayRecords.length} completed problems`);
  }
  if (/\[Code\]\(solutions\//.test(dayPage)) {
    failures.push(`${day}.md still uses a click-only Code link in its index`);
  }
  for (const record of dayRecords) {
    if (!dayPage.includes(path.basename(record.problemNotePath))) failures.push(`${day}.md is missing ${record.problemNotePath}`);
    if (!dayPage.includes(path.basename(record.screenshotPath))) failures.push(`${day}.md is missing ${record.screenshotPath}`);
    const expectedDayImage = record.screenshotPath.split("/").map(encodeURIComponent).join("/");
    if (!hasInlineImageTarget(dayPage, expectedDayImage)) {
      failures.push(`${day}.md does not render ${record.screenshotPath} inline`);
    }
  }
}

for (const requiredFile of [
  "../HDLBits_Tracker.xlsx",
  "images/Review/review-exams__2013_q2afsm.png",
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
  "internal/REPOSITORY_REVIEW.md",
  "Mistakes.md",
  ...archiveDays.map((day) => `${day}.md`),
  ...manifest.map((record) => record.problemNotePath),
];

for (const relativeFile of markdownFiles) {
  const absoluteFile = path.join(root, relativeFile);
  const content = await fs.readFile(absoluteFile, "utf8");
  if (/[ \t]+$/m.test(content)) failures.push(`Markdown contains trailing whitespace: ${relativeFile}`);
  if (/<a\s+href="[^"]+"><img\s/i.test(content)) {
    failures.push(`Clickable HTML image wrapper found in ${relativeFile}; use direct Markdown image syntax`);
  }
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
    verifiedImageMetadata: screenshotAudit.screenshots.length,
    markdownFiles: markdownFiles.length,
    dayCounts: counts,
    brokenLinks: 0,
    duplicateRecords: 0,
    staleEmbeddedSolutions: 0,
    trailingWhitespace: 0,
  }, null, 2));
}
