# 132 — Combinational circuit 6

| Field | Value |
|---|---|
| Day | Day 06 |
| Last successful submission | 2026-06-28 4:07:13 PM |
| Course location | Verification: Reading Simulations → Build a circuit from a simulation waveform |
| HDLBits identifier | `sim/circuit6` |
| Attempts | 2 total: 1 incorrect, 0 compile error, 0 simulation error |
| Success rate | 50% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/sim/circuit6) |
| Files | [Open screenshot at full resolution](../../images/Day%2006/132-sim__circuit6.png) · [Verilog solution](../../solutions/Day%2006/132-sim__circuit6.sv) |

## Question and submitted solution

<a href="../../images/Day%2006/132-sim__circuit6.png"><img src="../../images/Day%2006/132-sim__circuit6.png" alt="Combinational circuit 6 question and submitted solution" width="100%"></a>

## What the question is asking

The waveform describes a small combinational ROM. The 3-bit address `a` selects one of eight fixed 16-bit words.

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

All eight address values are covered, so the combinational `case` fully specifies Q without a default. This pattern synthesizes as decode/multiplexer logic or a ROM structure, depending on the target technology.

## Saved Verilog solution

```verilog
module top_module (
    input [2:0] a,
    output reg [15:0] q
);

    always @(*) begin
        case (a)
            3'd0: q = 16'h1232;
            3'd1: q = 16'haee0;
            3'd2: q = 16'h27d4;
            3'd3: q = 16'h5a0e;
            3'd4: q = 16'h2066;
            3'd5: q = 16'h64ce;
            3'd6: q = 16'hc526;
            3'd7: q = 16'h2f19;
        endcase
    end

endmodule
```

## What I learned

_Fill this in during revision._
