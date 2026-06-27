import fs from "node:fs";
import path from "node:path";

const root = path.resolve(import.meta.dirname, "..");
const records = JSON.parse(fs.readFileSync(path.join(root, "archive_manifest.json"), "utf8"));

const explanations = {
  wire: "Connect the single input directly to the output so the module behaves exactly like a wire.",
  wire4: "Create the requested one-to-one and fan-out wire connections between the named inputs and outputs.",
  notgate: "Drive the output with the logical inverse of the input, implementing a NOT gate.",
  andgate: "Produce an output that is high only when both input signals are high.",
  norgate: "Implement a NOR gate: OR the inputs and invert the result.",
  xnorgate: "Implement an XNOR gate whose output is high when the two inputs have equal values.",
  wire_decl: "Declare intermediate wires and connect the supplied gates so the module matches the shown circuit diagram.",
  "7458": "Recreate the 7458-style sum-of-products circuit by combining several AND terms into two OR outputs.",
  vector0: "Declare vector ports with the required widths and connect the complete input bus to the output bus.",
  vector1: "Practice vector declarations, bit ordering, and selecting individual bits from buses with different index directions.",
  vector2: "Split a 16-bit input vector into its upper and lower 8-bit halves and route them to separate outputs.",
  vectorgates: "Apply bitwise OR, logical OR, and bitwise inversion to vectors so their different behaviours are visible.",
  gates4: "Use reduction operators to compute one-bit AND, OR, and XOR results across all four input bits.",
  vector3: "Use concatenation to regroup the input vectors and assign the requested output vectors in the specified bit order.",
  vectorr: "Reverse the bit order of the input vector so the most-significant and least-significant positions swap.",
  vector4: "Use the replication operator to repeat a bit pattern and form the required wider output vector.",
  vector5: "Combine replication and concatenation to build widened vectors and compare them bit by bit.",
  module: "Instantiate the provided submodule and connect its input and output ports to the top-level module.",
  module_pos: "Instantiate a module and connect its ports by position, keeping the connection order exactly correct.",
  module_name: "Instantiate a module and connect its ports by name so each signal is matched explicitly.",
  module_shift: "Chain three copies of the provided module so each stage feeds the next stage.",
  module_shift8: "Instantiate the supplied 8-bit module and connect vector signals correctly through the hierarchy.",
  module_add: "Instantiate two 16-bit adders to create a 32-bit adder, propagating the carry between the lower and upper halves.",
  module_fadd: "Build a ripple-carry adder from full-adder instances and expose the carry produced by every bit position.",
  module_cseladd: "Build a carry-select adder by computing both possible upper sums and selecting the correct one using the lower carry.",
  module_addsub: "Create an adder-subtractor by conditionally inverting one operand and using the mode signal as the initial carry-in.",
  alwaysblock1: "Describe the same combinational logic with both a continuous assignment and an always block.",
  alwaysblock2: "Describe clocked storage in an always block so the output captures the input on each active clock edge.",
  always_if: "Use an if/else statement in combinational logic to implement the requested multiplexer behaviour.",
  always_if2: "Correct an incomplete combinational if statement by assigning every output on every path and thereby avoiding latches.",
  always_case: "Use a case statement to select one of several input values according to the selector.",
  always_case2: "Implement a priority encoder whose output identifies the highest-priority asserted input bit.",
  always_casez: "Implement the priority encoder compactly with casez patterns and don't-care bits.",
  always_nolatches: "Complete the combinational case logic with safe defaults so no output retains an old value or infers a latch.",
  conditional: "Use nested ternary operators to select the smallest unsigned value from several inputs.",
  reduction: "Compare bitwise and reduction operators by producing per-bit results and single-bit reductions from two vectors.",
  gates100: "Apply reduction operators across a 100-bit vector to implement very wide AND, OR, and XOR gates.",
  vector100r: "Use a combinational for loop to reverse all 100 bits of a vector.",
  popcount255: "Count how many bits are high in a 255-bit input vector using combinational accumulation.",
  adder100i: "Generate a 100-bit ripple-carry adder and return both the sum and the carry from every bit stage.",
  bcdadd100: "Chain 100 one-digit BCD adders to add two 100-digit decimal numbers with carry propagation.",
  "exams/m2014_q4h": "Implement the shown circuit's output as a direct wire connection.",
  "exams/m2014_q4i": "Tie the requested output permanently low to represent ground.",
  "exams/m2014_q4e": "Translate the shown gate symbol into the equivalent NOR logic expression.",
  "exams/m2014_q4f": "Identify the function of the shown gate circuit and express it correctly in Verilog.",
  "exams/m2014_q4g": "Translate the two-gate schematic into a single correct combinational output expression.",
  gates: "Implement several basic gates at once, including bitwise outputs and their logical complements.",
  "7420": "Model a 7420 chip containing two independent four-input NAND gates.",
  truthtable1: "Convert the supplied truth table into combinational Verilog that produces the specified output for every input combination.",
  mt2015_eq2: "Compare two 2-bit inputs and assert the output only when both vectors are equal.",
  mt2015_q4a: "Implement the first small combinational circuit exactly as shown in the diagram.",
  mt2015_q4b: "Implement the second small combinational circuit exactly as shown in the diagram.",
  mt2015_q4: "Instantiate or combine circuits A and B so they operate together with the requested top-level connections.",
  ringer: "Choose whether a phone should ring or vibrate from the incoming-call and silent-mode control signals.",
  thermostat: "Implement the thermostat's heater, air-conditioner, and fan control rules from the temperature and mode inputs.",
  popcount3: "Count the number of asserted bits in a 3-bit input and return that count as a binary value.",
  gatesv: "For two vectors, compute bitwise gate results and also indicate whether the vectors differ at any or every position.",
  gatesv100: "Extend the vector-gate comparison to 100-bit inputs, including per-bit outputs and wide reduction results.",
  mux2to1: "Implement a one-bit 2-to-1 multiplexer that selects one input according to the select signal.",
  mux2to1v: "Implement a 2-to-1 multiplexer that selects an entire vector rather than a single bit.",
  mux9to1v: "Select one of nine 16-bit inputs; produce the required default value when the selector is outside the valid range.",
  mux256to1: "Select one bit from a 256-bit input vector using an 8-bit selector as the index.",
  mux256to1v: "Select one 4-bit word from 256 packed words by calculating the correct vector slice from the selector.",
  hadd: "Implement a half adder that produces a one-bit sum and carry from two input bits.",
  fadd: "Implement a full adder that includes carry-in and produces both sum and carry-out.",
  adder3: "Chain three full adders to add two 3-bit numbers and expose the intermediate carry signals.",
  "exams/m2014_q4j": "Implement the adder circuit shown in the exam diagram with the requested sum and carry behaviour.",
  "exams/ece241_2014_q1c": "Add two signed values and assert overflow when the mathematical result cannot fit in the signed output width.",
  adder100: "Implement a 100-bit combinational adder and return the final carry-out together with the sum.",
  bcdadd4: "Chain four BCD full adders to add two four-digit decimal values and propagate decimal carry between digits.",
  kmap1: "Derive and implement the simplified logic function represented by the supplied 3-variable Karnaugh map.",
  kmap2: "Derive a minimal combinational expression from the supplied 4-variable Karnaugh map.",
  kmap3: "Implement the 4-variable Karnaugh-map function while using the indicated don't-care cells for simplification.",
  kmap4: "Translate the supplied 4-variable Karnaugh map into a correct simplified Verilog expression.",
  "exams/ece241_2013_q2": "Implement both the minimum sum-of-products and minimum product-of-sums forms for the given logic function.",
  "exams/m2014_q3": "Simplify the exam Karnaugh map and implement the resulting combinational output.",
  "exams/2012_q1g": "Convert the supplied Karnaugh map, including any don't-care conditions, into simplified logic.",
  "exams/ece241_2014_q3": "Implement the Karnaugh-map function using the specified multiplexer structure and input assignments.",
  dff: "Create a positive-edge-triggered D flip-flop that stores the input value on each rising clock edge.",
  dff8: "Create eight D flip-flops in parallel so an entire 8-bit vector is registered on the rising clock edge.",
  dff8r: "Add a synchronous reset to an 8-bit register so reset is sampled on the active clock edge.",
  dff8p: "Create an 8-bit register whose synchronous reset loads the specified non-zero reset value.",
  dff8ar: "Create an 8-bit register with asynchronous reset, allowing reset to change the output without waiting for a clock edge.",
  dff16e: "Build a 16-bit register with synchronous reset and independent byte-enable controls for its upper and lower bytes.",
  "exams/m2014_q4a": "Model the level-sensitive D latch shown in the exam circuit.",
  "exams/m2014_q4b": "Model the positive-edge-triggered D flip-flop shown in the exam circuit.",
  "exams/m2014_q4c": "Model the specified D flip-flop behaviour and its control connection from the diagram.",
  "exams/m2014_q4d": "Implement the shown combination of a D flip-flop and combinational gate.",
  mt2015_muxdff: "Implement the circuit in which a multiplexer chooses the value captured by a D flip-flop.",
  "exams/2014_q4a": "Translate the exam's multiplexer-and-DFF schematic into equivalent sequential Verilog.",
  "exams/ece241_2014_q4": "Implement the shown network of D flip-flops and logic gates with the correct cycle-to-cycle behaviour.",
  "exams/ece241_2013_q7": "Build the sequential circuit described by the state/output truth table, including its registered state.",
  edgedetect: "Generate a one-cycle pulse whenever each input bit makes a 0-to-1 transition.",
  edgedetect2: "Generate a one-cycle pulse whenever each input bit changes in either direction.",
  edgecapture: "Set a register bit when a falling edge occurs and keep it set until a synchronous reset clears it.",
  dualedge: "Emulate dual-edge-triggered storage using logic that captures data on both rising and falling clock edges.",
  count15: "Implement a 4-bit binary counter with synchronous reset that naturally wraps after 15.",
  count10: "Implement a decade counter that counts from 0 through 9 and then wraps to 0.",
  count1to10: "Implement the specified 1-to-10 decade count sequence with the required reset and enable behaviour.",
  countslow: "Create a decade counter that advances only when the slow-enable input is asserted.",
  shift4: "Build a 4-bit shift register with the specified load/shift controls and expose the requested stage output.",
  rotate100: "Build a 100-bit register that can hold, load, rotate left, or rotate right according to the controls.",
  shift18: "Build a 64-bit register that can load or perform left/right arithmetic shifts by either 1 or 8 positions.",
  lfsr5: "Implement the specified 5-bit linear-feedback shift register using the given feedback taps and reset state.",
  mt2015_lfsr: "Implement the shown 3-bit LFSR and reproduce its required feedback sequence.",
  lfsr32: "Implement a 32-bit linear-feedback shift register with the specified tap positions.",
  "exams/m2014_q4k": "Translate the exam shift-register schematic into clocked Verilog with the same data movement.",
  "exams/2014_q4b": "Implement the shown shift register and its control logic exactly as specified by the exam circuit.",
  "exams/ece241_2013_q12": "Build a 3-input lookup table from a shift register and multiplexer so its truth table can be loaded serially.",
  fsm1: "Implement the provided two-state FSM, using an asynchronous reset and the diagram's transition and output rules.",
  fsm1s: "Implement the same two-state FSM with a synchronous reset instead of an asynchronous reset.",
  fsm2: "Implement the second supplied finite-state machine, including its asynchronous reset, transitions, and output decoding.",
  fsm2s: "Implement the second FSM with a synchronous reset while preserving the transition and output behaviour.",
  fsm3comb: "Write only the combinational next-state logic for the supplied state-transition diagram.",
};

function urlPath(value) {
  return value.split("/").map(encodeURIComponent).join("/");
}

function readSolution(record) {
  return fs.readFileSync(path.join(root, record.solutionPath), "utf8")
    .split(/\r?\n/)
    .map((line) => line.trimEnd())
    .join("\n")
    .trimEnd();
}

function imageHtml(src, title) {
  const alt = `${title} question and submitted solution`;
  return `<a href="${src}"><img src="${src}" alt="${alt}" width="100%"></a>`;
}

function buildProblemNote(record) {
  const image = `../../${urlPath(record.screenshotPath)}`;
  const solution = `../../${urlPath(record.solutionPath)}`;
  const explanation = explanations[record.slug];
  const code = readSolution(record);
  const attempts = `${record.totalAttempts} total: ${record.incorrect} incorrect, ${record.compileError} compile error, ${record.simulationError} simulation error`;

  return `# ${String(record.problemNumber).padStart(3, "0")} — ${record.title}

| Field | Value |
|---|---|
| Day | ${record.day} |
| Last successful submission | ${record.dateKey} ${record.time} |
| Course location | ${record.category} → ${record.section}${record.subsection ? ` → ${record.subsection}` : ""} |
| HDLBits identifier | \`${record.slug}\` |
| Attempts | ${attempts} |
| Success rate | ${record.successRate} |
| Source | [Open original HDLBits problem](${record.url}) |
| Files | [Open screenshot at full resolution](${image}) · [Verilog solution](${solution}) |

## Question and submitted solution

${imageHtml(image, record.title)}

## What the question is asking

${explanation}

## Saved Verilog solution

\`\`\`verilog
${code}
\`\`\`

## What I learned

_Fill this in during revision._
`;
}

function buildDayPage(day, dayRecords) {
  const date = dayRecords[0].dateKey;
  const rows = dayRecords.map((record, index) => {
    const number = String(record.problemNumber).padStart(3, "0");
    return `| ${index + 1} | ${record.time} | [${number}](#problem-${number}) | ${record.section} | [${record.title}](${urlPath(record.problemNotePath)}) | [Code](${urlPath(record.solutionPath)}) | [HDLBits](${record.url}) |`;
  }).join("\n");

  const sections = dayRecords.map((record) => {
    const number = String(record.problemNumber).padStart(3, "0");
    const image = urlPath(record.screenshotPath);
    const code = readSolution(record);
    return `<a id="problem-${number}"></a>
## ${number} — ${record.title}

[Problem note](${urlPath(record.problemNotePath)}) · [Open screenshot at full resolution](${image}) · [Verilog file](${urlPath(record.solutionPath)}) · [HDLBits problem](${record.url})

${imageHtml(image, record.title)}

### What the question is asking

${explanations[record.slug]}

### Saved Verilog solution

\`\`\`verilog
${code}
\`\`\`
`;
  }).join("\n---\n\n");

  return `# ${day} — ${date}

Completed problems: **${dayRecords.length}**

Each screenshot is embedded at the full width of the GitHub page. Select an image to open its original-resolution file.

## Index

| # | Time | Problem | Section | Problem note | Solution | Source |
|---:|---|---:|---|---|---|---|
${rows}

---

${sections}`;
}

const missing = records.filter((record) => !explanations[record.slug]);
if (missing.length) {
  throw new Error(`Missing explanations: ${missing.map((record) => record.slug).join(", ")}`);
}

for (const record of records) {
  fs.writeFileSync(path.join(root, record.problemNotePath), buildProblemNote(record), "utf8");
}

for (const day of [...new Set(records.map((record) => record.day))]) {
  const dayRecords = records.filter((record) => record.day === day);
  fs.writeFileSync(path.join(root, `${day}.md`), buildDayPage(day, dayRecords), "utf8");
}

fs.writeFileSync(path.join(root, "problem_explanations.json"), `${JSON.stringify(explanations, null, 2)}\n`, "utf8");
console.log(`Updated ${records.length} problem notes and ${new Set(records.map((record) => record.day)).size} day pages.`);
