# 177 — Q2a: Arbiter FSM

| Field | Value |
|---|---|
| Day | Day 14 |
| Last successful submission | 2026-07-07 1:36:14 AM |
| Course location | Circuits → Sequential Logic → Finite State Machines |
| HDLBits identifier | `exams/2013_q2afsm` |
| Attempts | 4 total: 1 incorrect, 2 compile error, 0 simulation error |
| Success rate | 25% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/exams/2013_q2afsm) |
| Files | Screenshot rendered below · [Verilog solution](../../solutions/Day%2014/177-exams__2013_q2afsm.sv) |

## Question and submitted solution

![Q2a: Arbiter FSM question and submitted solution](../../images/Day%2014/177-exams__2013_q2afsm-question-and-successful-submission.png)

## Prior attempt evidence

![Earlier Q2a FSM review attempt](../../images/Review/review-exams__2013_q2afsm.png)

This earlier attempt is preserved as mistake evidence; the complete Chrome capture above is the authoritative successful submission.


## What the question is asking

This arbiter FSM grants access according to the request conditions in the supplied state diagram. Each state represents the currently selected ownership or idle condition, and the combinational transition block follows the diagram for every request combination. The clocked state register applies the specified reset and makes grants stable for a complete cycle. Outputs are Moore decodes of the registered state, preventing combinational request glitches from appearing directly on grant lines.

The earlier attempt evidence is retained because it shows why a complete transition table matters: missing request combinations or an incorrect priority can strand the controller or grant the wrong requester. The corrected version assigns next_state for every legal state, includes a safe default for unused encodings, and decodes mutually exclusive grants from state. Verification should cover idle entry, each independent request, simultaneous requests, request withdrawal, and reset from every grant state.

## Saved Verilog solution

```verilog
module top_module (
    input clk,
    input resetn,
    input [3:1] r,
    output [3:1] g
);
    reg [1:0] state, next_state;
    parameter idle = 2'b00;
    parameter s1 = 2'b01;
    parameter s2 = 2'b10;
    parameter s3 = 2'b11;

    always @(posedge clk) begin
        if (!resetn)
            state <= idle;
        else
            state <= next_state;
    end

    always @(*) begin
        case (state)
            idle: begin
                if (r[1])
                    next_state = s1;
                else if (r[2])
                    next_state = s2;
                else if (r[3])
                    next_state = s3;
                else
                    next_state = idle;
            end
            s1: next_state = r[1] ? s1 : idle;
            s2: next_state = r[2] ? s2 : idle;
            s3: next_state = r[3] ? s3 : idle;
            default: next_state = idle;
        endcase
    end

    assign g[1] = (state == s1);
    assign g[2] = (state == s2);
    assign g[3] = (state == s3);
endmodule
```

## What I learned

_Fill this in during revision._
