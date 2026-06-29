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
  fsm3onehot: `This problem gives the four-state Moore machine as a transition table, but supplies the current state as a one-hot vector instead of asking for a state register. The implementation therefore derives each bit of \`next_state\` from the incoming transitions to that state.

For example, state A is reached from A or C only when \`in=0\`, so \`next_state[A] = ~in & (state[A] | state[C])\`. State B is reached from A, B, or D when \`in=1\`; C is reached from B or D when \`in=0\`; and D is reached only from C when \`in=1\`. The Moore output is high only in D, so it is simply \`state[D]\`.

**Why the direct equations matter:** HDLBits deliberately supplies non-one-hot test vectors. A \`case\` statement that assumes exactly one active state, or logic that forces illegal states back to A, would implement different behaviour. The sum-of-products equations preserve every simultaneously active incoming term.

**Trace example:** with \`state=4'b0100\` (C), \`in=1\` asserts only \`next_state[D]\`; with the same state and \`in=0\`, only \`next_state[A]\` is asserted.`,
  fsm3: `This is the complete four-state Moore FSM whose combinational transition table was implemented in the preceding exercises. The design separates three concerns: combinational next-state decoding, the clocked state register, and Moore output decoding.

The transition logic implements A: 0→A/1→B, B: 0→C/1→B, C: 0→A/1→D, and D: 0→C/1→B. A default assignment of \`next_state = state\` prevents an unintended latch and gives a safe hold value before the \`case\` overrides it.

The reset is **asynchronous** because \`areset\` appears in the event control: \`always @(posedge clk or posedge areset)\`. As soon as reset rises, the state becomes A without waiting for a clock. Ordinary transitions still occur only at a rising clock edge. Since this is a Moore machine, \`out\` depends only on the registered state and is asserted exactly in D.

**Revision pitfall:** putting reset only inside \`always @(posedge clk)\` would silently change this into the synchronous-reset version.`,
  fsm3s: `This exercise uses the same A/B/C/D transition graph and Moore output as \`fsm3\`, but changes the reset timing. The transition decoder still computes A: 0→A/1→B, B: 0→C/1→B, C: 0→A/1→D, and D: 0→C/1→B, while \`out\` is high only when the registered state is D.

The state register is sensitive only to \`posedge clk\`. Consequently, asserting \`reset\` between edges does not immediately change the state; reset is sampled at the next rising edge and then loads A. This is the defining behaviour of a synchronous reset.

**Cycle trace:** if the machine is in D and reset rises halfway through a cycle, \`out\` remains high until the next rising clock edge. At that edge state becomes A and \`out\` falls. In the asynchronous version, state and output would change as soon as reset rose.

**Revision pitfall:** the comment in the submitted starter code mentions an asynchronous reset, but the actual problem and sensitivity list require synchronous reset. The event control, not the comment, determines the hardware.`,
  "exams/ece241_2013_q4": `This problem is more than a water-level decoder: the outputs depend on both the current sensor pattern and whether the water level was rising or falling. That history requirement makes it a Moore FSM rather than pure combinational logic.

Sensors \`s[1]\`, \`s[2]\`, and \`s[3]\` represent progressively higher levels. The six encoded states distinguish below-sensor-1, between sensors 1–2 while rising or falling, between sensors 2–3 while rising or falling, and above sensor 3. The next-state priority checks the highest asserted sensor first, which maps any valid thermometer-like sensor pattern to the appropriate level band.

The output vector is \`{fr3, fr2, fr1, dfr}\`. More fill valves are enabled at lower levels. The direction-sensitive \`dfr\` bit is clear while the level is rising and set while it is falling, preserving the required hysteresis. At the lowest state all four outputs are asserted; above the highest sensor all are clear.

Reset is active-high and synchronous, loading the below-sensor-1 state. The explicit default state and default output also recover deterministically from an unused 3-bit encoding.

**Key lesson:** whenever identical input values require different outputs depending on the path taken to reach them, the path must be stored as state.`,
  "exams/ece241_2013_q8": `This is a three-state Mealy sequence detector for the overlapping bit pattern 101. The states store the longest useful prefix of the target sequence that has already been seen: S0 means no useful prefix, S1 means the last bit can serve as the leading 1, and S10 means the input stream currently ends in 10.

The next-state table follows that prefix meaning. From S0, input 1 enters S1 and input 0 stays in S0. From S1, another 1 still leaves a valid leading 1, while 0 advances to S10. From S10, input 1 completes 101 and also becomes the leading 1 of a possible overlapping next match, so the machine goes to S1; input 0 breaks the prefix and returns to S0.

The output is Mealy-style: \`z = (state == S10) && x\`. It asserts during the same cycle that the final 1 arrives, not one clock later. The reset is active-low and asynchronous because the state register is sensitive to \`negedge aresetn\`; when reset is asserted, state returns immediately to S0.

**Trace example:** for input stream 10101, the machine visits S0 -> S1 -> S10, asserts z on the third bit, returns to S1, moves to S10, and asserts z again on the fifth bit. That is the overlapping behavior the problem asks for.`,
  lemmings1: `The Lemming has only two Moore states: walking left and walking right. Direction changes occur only when an obstacle is encountered on the side toward which it is currently walking.

In LEFT, \`bump_left=1\` sends the FSM to RIGHT; otherwise it stays LEFT. In RIGHT, \`bump_right=1\` sends it to LEFT; otherwise it stays RIGHT. If both bump inputs are high, the relevant condition for either current state is high, so the machine still reverses direction exactly once.

The asynchronous reset is implemented with \`posedge areset\` in the event control and immediately places the Lemming in LEFT. The two outputs are Moore decodes: \`walk_left\` is high only in LEFT and \`walk_right\` only in RIGHT, so they are mutually exclusive for every legal state.

**Trace example:** LEFT + right-side bump only remains LEFT because an obstacle behind the Lemming does not matter. LEFT + left-side bump changes the registered state to RIGHT at the next clock edge.`,
  "exams/2013_q2bfsm": `This controller combines a one-cycle start pulse, a serial sequence detector, a two-cycle deadline, and two absorbing terminal outcomes.

After active-low **synchronous** reset, state A is held. Once reset is released, A→B makes \`f=1\` for exactly one clock, then B→C begins monitoring \`x\`. States C, D, and E recognize the overlapping sequence 1-0-1: C waits for the first 1, D remembers a trailing 1, and E remembers 10. A 1 in E completes the sequence and enters F.

States F and G implement the “within at most two cycles” check for \`y\`. If \`y\` is high in either state, the machine enters H, where \`g\` stays high until reset. If both checks fail, it enters I, where \`g\` stays low until reset. The output expression keeps \`g\` high during F and G as required while the decision window is open.

**Important timing point:** outputs are Moore decodes of registered state. Sequence completion on one edge changes the state to F, and \`g\` becomes high during the following cycle.`,
  bugs_mux2: `The broken circuit mixed two independent mistakes: the output was declared as a scalar even though both data inputs are 8-bit buses, and the selection expression did not implement the required bus mux correctly.

The fixed output is \`[7:0]\`, and the ternary operator selects the entire vector in one expression: when \`sel=1\`, output A; otherwise output B. This is width-preserving and synthesizes to eight parallel 2-to-1 multiplexers sharing the same select line.

**Check:** \`sel=0\` must copy every bit of B, and \`sel=1\` must copy every bit of A. A one-bit output declaration could appear to work for bit 0 while silently discarding bits 7:1.`,
  bugs_nand3: `The required primitive is a five-input AND gate with positional port order \`(out, a, b, c, d, e)\`. To create a three-input AND, the unused inputs must be tied to the AND identity value 1, not 0. The intermediate \`ando\` is therefore \`a & b & c & 1 & 1\`.

A separate NOT gate inverts that intermediate value to produce the requested NAND function. The resulting truth rule is simple: \`out\` is low only for \`a=b=c=1\`; every other input combination produces high.

**Debugging lessons:** positional module connections must follow the declaration order exactly, intermediate nets need explicit declarations, and unused AND inputs must be tied high. Named port connections would reduce the risk of an ordering error.`,
  bugs_mux4: `A 4-to-1 bus multiplexer can be built as a two-level tree of the supplied 2-to-1 muxes. The first level uses \`sel[0]\` to choose A/B and C/D independently. The second level uses \`sel[1]\` to choose between those two intermediate buses.

The intermediate signals must be 8-bit vectors; scalar wires would truncate seven bits. The corrected third instance also uses a unique instance name and selects with \`sel[1]\`, not \`sel[0]\`.

| sel | output |
|---|---|
| 00 | A |
| 01 | B |
| 10 | C |
| 11 | D |

This table is a quick way to trace both levels and catch swapped select bits.`,
  bugs_addsubz: `The combinational block first computes either \`a+b\` or \`a-b\` according to \`do_sub\`, then derives \`result_is_zero\` from the newly computed \`out\`.

Blocking assignments are important here. With \`out = ...\`, the following zero comparison sees the current combinational result in the same evaluation. A nonblocking assignment could make the flag observe the previous value during simulation and create a mismatch between intent and behaviour.

The zero test is placed after the \`case\`, so it applies equally to addition and subtraction. Both outputs are declared \`reg\` because they are assigned procedurally.

**Revision pitfall:** calculating the zero flag in only one case branch, or omitting an assignment on a path, would infer storage or leave stale flag data.`,
  bugs_case: `This decoder recognizes the PS/2 scan codes for decimal keys 0 through 9. Each recognized hexadecimal code assigns the corresponding 4-bit digit and asserts \`valid\`.

The critical repair is to provide defaults before the \`case\`: \`out=0\` and \`valid=0\`. Every recognized branch overrides both values. Any unlisted scan code therefore produces a deterministic invalid result instead of retaining the previous output and inferring latches.

Examples: \`8'h45\` maps to digit 0, \`8'h16\` to 1, and \`8'h46\` to 9. The \`default\` branch repeats the safe values, making the intended behaviour explicit.

**Debugging checklist:** verify literal width, hexadecimal code, digit mapping, and assignments to every combinational output on every path.`,
  "sim/circuit1": `The waveform shows a combinational AND function. Output \`q\` is high only during intervals in which both \`a\` and \`b\` are high, so the implementation is \`q = a & b\`.

Because there is no clock or storage, output changes propagate whenever either input changes. The four-row truth table is 00→0, 01→0, 10→0, and 11→1.

**Waveform method:** compare each transition of one input while holding the other fixed. When B is 0, changing A has no effect; when B is 1, Q follows A. That uniquely identifies AND rather than OR or XOR.`,
  "sim/circuit2": `The waveform corresponds to four-input even parity, implemented as the inverse of a four-way XOR: \`q = ~(a ^ b ^ c ^ d)\`.

An XOR reduction is 1 when an odd number of inputs are high. Inverting it makes Q high for 0, 2, or 4 asserted inputs and low for 1 or 3 asserted inputs. The same function could be written with the reduction-XNOR operator \`~^{a,b,c,d}\`.

**Trace examples:** 0000 has zero ones and produces 1; 0001 has one one and produces 0; 1010 has two ones and produces 1. Counting asserted bits is often the fastest way to recognize parity in a waveform.`,
  "sim/circuit3": `The submitted expression factors to \`q = (a | b) & (c | d)\`. Thus at least one signal from the A/B pair and at least one signal from the C/D pair must be high.

The unfactored form, \`d&(a|b) | c&(a|b)\`, makes the waveform-derived product terms visible; Boolean factoring exposes the simpler two-ORs-into-an-AND circuit.

**Checks:** if A=B=0, Q is always 0 regardless of C/D. If C=D=0, Q is also always 0. With A=1 and C=1, Q is 1 regardless of B/D. These controlled waveform comparisons distinguish the grouped function from a four-input OR.`,
  "sim/circuit4": `The waveform shows that only \`b\` and \`c\` affect the output. Q is high whenever either is high, giving \`q = b | c\`; inputs A and D are observable distractors with no functional influence.

**How to infer this:** find intervals where A or D toggles while B and C remain fixed. Q does not change. Then compare the four B/C combinations: only 00 produces 0, while 01, 10, and 11 produce 1.

Ignoring irrelevant inputs is an important waveform-reading skill: a port’s presence does not guarantee that synthesized logic uses it.`,
  "sim/circuit5": `This circuit is a 4-bit lookup/multiplexer controlled by \`c\`. For selector values 0 through 3, Q chooses different input buses: 0→B, 1→E, 2→A, and 3→D. All other selector values produce \`4'hf\`.

The \`case\` statement is combinational and assigns Q in every branch, including \`default\`, so no latch is inferred. Input bus C is used as the selector, while the data buses retain their full 4-bit widths.

**Waveform technique:** locate periods where one candidate bus has a distinctive value, then see whether Q matches it for a particular C value. Repeating that across multiple simulations disambiguates buses that happen to share a value temporarily.`,
  "sim/circuit6": `The waveform describes a small combinational ROM. The 3-bit address \`a\` selects one of eight fixed 16-bit words.

| a | q |
|---:|---:|
| 0 | 16'h1232 |
| 1 | 16'haee0 |
| 2 | 16'h27d4 |
| 3 | 16'h5a0e |
| 4 | 16'h2066 |
| 5 | 16'h64ce |
| 6 | 16'hc526 |
| 7 | 16'h2f19 |

All eight address values are covered, so the combinational \`case\` fully specifies Q without a default. This pattern synthesizes as decode/multiplexer logic or a ROM structure, depending on the target technology.`,
  "sim/circuit7": `This is a positive-edge-triggered register whose D input is the inverse of \`a\`. On each rising edge, \`q <= ~a\`; between rising edges Q holds its previous value even if A changes.

The nonblocking assignment models simultaneous flip-flop sampling. A waveform trace should therefore read A immediately before each rising edge and compare its inverse with Q immediately after that edge.

**Distinguishing feature:** if Q followed \`~a\` continuously, it would be combinational. The observed hold intervals between clock edges prove that memory is present.`,
  "sim/circuit8": `The waveform is reproduced by two level/edge-sensitive storage stages. P is a transparent-high latch: while \`clock=1\`, P follows A; while the clock is low, P holds the last value seen during the high phase. The incomplete assignment inside the combinational block intentionally infers that latch.

Q updates on the falling edge with \`q <= p\`. Since P has just been tracking A during the high phase, Q captures the final latched value at the high-to-low transition and then holds it.

**Trace method:** during a high clock phase, changes on A appear on P but not immediately on Q. At the falling edge, Q takes P. During the low phase, later A changes affect neither stored output. This timing distinguishes a latch-plus-negedge-flip-flop chain from two ordinary flip-flops.`,
  "sim/circuit9": `The circuit is a modulo-7 counter with a synchronous load-like control. When \`a=0\`, the 4-bit state counts 0,1,2,3,4,5,6 and then wraps to 0. When \`a=1\` at a rising edge, the state is loaded with 4 instead of incrementing.

Q continuously exposes the registered count. All changes therefore occur after rising clock edges, not when A changes between edges.

**Trace examples:** count=6 and A=0 produces 0 on the next edge; count=2 and A=0 produces 3; any current count with A=1 produces 4. Priority is clear because the A branch is tested before the wrap/increment logic.`,
  "sim/circuit10": `This circuit behaves like a serial full adder with one stored carry bit. The combinational output \`q = a ^ b ^ state\` is the one-bit sum of A, B, and the previous carry.

At each rising edge, \`state\` is updated to the majority function \`ab | b·state | a·state\`, which is exactly the carry-out of a full adder. The new carry then participates in Q during the following cycle.

| a | b | carry-in | q (sum) | next state (carry-out) |
|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 | 1 |
| 0 | 0 | 1 | 1 | 0 |

The absence of reset means the testbench must establish or tolerate the initial carry state before checking deterministic sequences.`,
  "tb/clock": `This exercise moves from describing hardware to controlling simulation time. The top-level testbench has no ports because it is the simulation root. It declares an internal \`reg clk\`, connects that signal to the supplied \`dut\` instance, initializes it to zero at time 0, and toggles it every 5 ps.

Two half-periods make the required 10 ps period. Starting from zero means the first scheduled toggle is a rising edge at 5 ps, exactly matching the requested waveform. The \`initial\` block runs once, while \`always #5\` repeats forever; these are simulation constructs and are not intended to synthesize into physical logic.

**Timing trace:** \`clk=0\` at t=0, 1 at t=5, 0 at t=10, 1 at t=15, and so on. A common error is using \`#10\` for each toggle, which produces a 20 ps full period. Another is leaving the clock uninitialized: negating an unknown \`X\` still produces \`X\`, so the clock never becomes usable.`,
  "tb/tb1": `The goal is to generate two output waveforms directly from procedural stimulus. Because A and B are assigned inside an \`initial\` block, the module declares them as \`output reg\`. Both begin low at time 0, then the delays reproduce each transition in chronological order.

| Simulation time | A | B | Event |
|---:|---:|---:|---|
| 0 | 0 | 0 | initialize both outputs |
| 10 | 1 | 0 | raise A |
| 15 | 1 | 1 | raise B five time units later |
| 20 | 0 | 1 | lower A |
| 40 | 0 | 0 | lower B after its long high interval |

Delay statements are relative to the current process time, not absolute timestamps. Thus \`#10 A=1; #5 B=1;\` places the second event at t=15. Keeping the entire timeline in one ordered block makes that accumulation explicit and avoids accidental races between several independent stimulus processes.`,
  "tb/and": `This testbench verifies a two-input AND gate exhaustively. The DUT input is a 2-bit procedural register, while the DUT output is a wire because it is driven by the instantiated module. A loop enumerates the four binary input combinations 00, 01, 10, and 11, holding each combination for 10 simulation time units.

Using \`in = i[1:0]\` makes the mapping from loop counter to stimulus width explicit. The observed output should remain zero for the first three patterns and become one only for \`2'b11\`. This is exhaustive verification because a two-input combinational circuit has exactly four possible input states.

The important separation is stimulus versus response: the testbench drives \`in\`, but only observes \`out\`. Declaring the response as a procedural variable or assigning to it from the testbench would create an additional driver and invalidate the test. For larger circuits, the same enumeration idea scales until the input space becomes too large, at which point constrained or directed vectors are preferable.`,
  "tb/tb2": `This testbench coordinates two independent timelines: a free-running clock and a directed sequence for \`in\` and the 3-bit bus \`s\`. One \`initial\` block initializes the clock and toggles it every 5 time units, producing a 10-unit period. A second block applies the waveform values at the required boundaries, while the \`q7\` instance connects all generated signals to the supplied DUT.

| Time interval | in | s |
|---|---:|---:|
| 0-10 | 0 | 2 |
| 10-20 | 0 | 6 |
| 20-30 | 1 | 2 |
| 30-40 | 0 | 7 |
| 40-70 | 1 | 0 |
| 70 onward | 0 | 0 |

The sequence uses cumulative delays, so each \`#10\` advances from the preceding event, and \`#30\` creates the long final high interval for \`in\`. Changes occur on falling-clock boundaries in this waveform, giving the DUT stable inputs before the following rising edge. A frequent failure is to treat the delay values as absolute times or to forget that concurrent \`initial\` blocks begin together at t=0.`,
  "tb/tff": `The testbench instantiates the supplied T flip-flop and creates separate clock and control processes. The clock starts low and toggles every 5 time units. Reset starts high and \`t\` starts low, so the first rising edge samples the synchronous reset and forces Q to its reset state. After 10 time units, reset is deasserted and T is asserted; subsequent rising edges toggle Q.

The word *synchronous* is crucial: changing reset does not immediately change Q. Reset only has an effect when a rising edge occurs while reset is high. With this timeline, the rising edge at t=5 performs the reset, reset becomes low at t=10, and the edge at t=15 performs the first toggle.

The DUT output is a wire because the T flip-flop drives it. Clock, reset, and T are registers because the testbench drives them procedurally. Keeping the free-running clock and one-time stimulus in separate \`initial\` processes is intentional concurrency: both timelines advance together under the simulator's event scheduler.`,
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
