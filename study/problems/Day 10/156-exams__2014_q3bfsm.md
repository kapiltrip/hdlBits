# 156 — Q3b: FSM

| Field | Value |
|---|---|
| Day | Day 10 — 2026-07-03 |
| Status | Completed — live HDLBits submission verified |
| Course location | Circuits → Sequential Logic → Finite State Machines |
| HDLBits identifier | `exams/2014_q3bfsm` |
| Last saved success shown by HDLBits | 2026-07-03 10:10:20 PM |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/exams/2014_q3bfsm) |
| Files | [Successful question-and-answer screenshot](../../images/Day%2010/156-exams__2014_q3bfsm-question-and-answer.png) · [Verilog solution](../../solutions/Day%2010/156-exams__2014_q3bfsm.sv) |

## Complete question, submitted answer, and success result

<a href="../../images/Day%2010/156-exams__2014_q3bfsm-question-and-answer.png"><img src="../../images/Day%2010/156-exams__2014_q3bfsm-question-and-answer.png" alt="Q3b FSM full question, submitted solution, and successful result" width="100%"></a>

## What the question is asking

The state table supplies a five-state Moore machine with binary encodings `000` through `100`. Unlike Q3c, this problem asks for the **complete sequential machine**: a state register, combinational next-state logic, and output decode.

The three structural pieces have different responsibilities:

1. The clocked block stores `state` and applies the synchronous reset to `S0`.
2. The combinational `case` converts `(state,x)` into `next_state` using the table.
3. The Moore output decode asserts `z` only in `S3` and `S4`.

The default case is important even though every legal state is listed. A three-bit register has eight possible encodings, so `101`, `110`, and `111` need deterministic recovery behavior in simulation and synthesis.

### Transition trace

Starting in `S0`, input sequence `1,1,0,0` produces:

| Edge | Present state | `x` | Next state | `z` after edge |
|---:|---|---:|---|---:|
| Reset | — | — | `S0` | 0 |
| 1 | `S0` | 1 | `S1` | 0 |
| 2 | `S1` | 1 | `S4` | 1 |
| 3 | `S4` | 0 | `S3` | 1 |
| 4 | `S3` | 0 | `S1` | 0 |

`z` is decoded from the registered present state, so it changes only after a clock edge changes `state`.

## Saved Verilog solution

```verilog
module top_module (
    input clk,
    input reset,
    input x,
    output z
);
    localparam S0 = 3'd0, S1 = 3'd1, S2 = 3'd2,
               S3 = 3'd3, S4 = 3'd4;
    reg [2:0] state, next_state;

    always @(posedge clk) begin
        if (reset)
            state <= S0;
        else
            state <= next_state;
    end

    always @(*) begin
        case (state)
            S0: next_state = x ? S1 : S0;
            S1: next_state = x ? S4 : S1;
            S2: next_state = x ? S1 : S2;
            S3: next_state = x ? S2 : S1;
            S4: next_state = x ? S4 : S3;
            default: next_state = S0;
        endcase
    end

    assign z = (state == S3) || (state == S4);
endmodule
```

## Points to remember

- Synchronous reset belongs inside `always @(posedge clk)`.
- `next_state` needs a value for every state and input combination.
- Moore output `z` depends only on the registered state.
- Sized constants avoid width-truncation warnings.
- A default transition provides recovery from unused encodings.
