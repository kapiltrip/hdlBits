import fs from "node:fs/promises";
import path from "node:path";

const root = process.cwd();
const manifest = JSON.parse(await fs.readFile(path.join(root, "archive_manifest.json"), "utf8"));
const explanations = JSON.parse(await fs.readFile(path.join(root, "problem_explanations.json"), "utf8"));
const failures = [];

if (manifest.length !== 114) failures.push(`Manifest count is ${manifest.length}, expected 114`);

for (const record of manifest) {
  if (!explanations[record.slug]) failures.push(`Missing explanation: ${record.slug}`);
  for (const relative of [record.problemNotePath, record.screenshotPath, record.solutionPath]) {
    try {
      await fs.access(path.join(root, relative));
    } catch {
      failures.push(`Missing file: ${relative}`);
    }
  }
  const solution = await fs.readFile(path.join(root, record.solutionPath), "utf8");
  if (!solution.includes("endmodule")) failures.push(`Invalid solution: ${record.solutionPath}`);
}

const markdownFiles = [
  "README.md",
  ...Array.from({ length: 5 }, (_, index) => `Day ${String(index + 1).padStart(2, "0")}.md`),
  ...manifest.map((record) => record.problemNotePath),
];

for (const relativeFile of markdownFiles) {
  const absoluteFile = path.join(root, relativeFile);
  const content = await fs.readFile(absoluteFile, "utf8");
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
  console.log(JSON.stringify({ records: manifest.length, markdownFiles: markdownFiles.length, dayCounts: counts, brokenLinks: 0 }, null, 2));
}
