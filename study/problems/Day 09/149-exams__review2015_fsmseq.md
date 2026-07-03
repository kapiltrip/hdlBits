# 149 — FSM: Sequence 1101 recognizer

| Field | Value |
|---|---|
| Day | Day 09 |
| Last successful submission | 2026-07-02 5:30:53 PM |
| Course location | Circuits → Building Larger Circuits |
| HDLBits identifier | `exams/review2015_fsmseq` |
| Attempts | 12 total: 6 incorrect, 5 compile error, 0 simulation error |
| Success rate | 8% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/exams/review2015_fsmseq) |
| Files | [Open screenshot at full resolution](../../images/Day%2009/149-exams__review2015_fsmseq.png) · [Verilog solution](../../solutions/Day%2009/149-exams__review2015_fsmseq.sv) |

## Question and submitted solution

<a href="../../images/Day%2009/149-exams__review2015_fsmseq.png"><img src="../../images/Day%2009/149-exams__review2015_fsmseq.png" alt="FSM: Sequence 1101 recognizer question and submitted solution" width="100%"></a>

## What the question is asking

This Moore finite-state machine recognizes the serial bit pattern 1101 and then latches a permanent command to begin shifting. States S0 through S3 record how much of the target prefix has been matched: no useful prefix, 1, 11, and 110. DONE means the complete 1101 sequence has appeared.

The transitions preserve useful overlap. From S2 (the suffix 11), another 1 remains in S2 because the newest two bits are still 11; a 0 advances to S3. From S3, a 1 completes 1101 and enters DONE, while a 0 has no useful suffix and returns to S0. Earlier mismatches similarly return to the correct prefix state.

DONE is absorbing: both possible data values leave the machine in DONE. Therefore start_shifting, decoded solely from the registered state, stays asserted forever after recognition and can be cleared only by reset. Reset is synchronous because it is tested inside an always @(posedge clk) process rather than included in the sensitivity list.

**Example trace:** after reset, inputs 1,1,0,1 move S0→S1→S2→S3→DONE. The output becomes high after the edge accepting the final 1 and remains high on all later edges.

## Saved Verilog solution

```verilog
module top_module (
    input clk,
    input reset,
    input data,
    output start_shifting
);
    localparam S0   = 3'b000;
    localparam S1   = 3'b001;
    localparam S2   = 3'b010;
    localparam S3   = 3'b011;
    localparam DONE = 3'b100;

    reg [2:0] state;
    reg [2:0] next_state;

    always @(posedge clk) begin
        if (reset)
            state <= S0;
        else
            state <= next_state;
    end

    always @(*) begin
        case (state)
            S0:      next_state = data ? S1 : S0;
            S1:      next_state = data ? S2 : S0;
            S2:      next_state = data ? S2 : S3;
            S3:      next_state = data ? DONE : S0;
            DONE:    next_state = DONE;
            default: next_state = S0;
        endcase
    end

    assign start_shifting = (state == DONE);
endmodule
```

## What I learned

_Fill this in during revision._
