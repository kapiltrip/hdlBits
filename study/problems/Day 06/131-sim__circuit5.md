# 131 — Combinational circuit 5

| Field | Value |
|---|---|
| Day | Day 06 |
| Last successful submission | 2026-06-28 3:57:19 PM |
| Course location | Verification: Reading Simulations → Build a circuit from a simulation waveform |
| HDLBits identifier | `sim/circuit5` |
| Attempts | 4 total: 0 incorrect, 2 compile error, 0 simulation error |
| Success rate | 50% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/sim/circuit5) |
| Files | [Open screenshot at full resolution](../../images/Day%2006/131-sim__circuit5.png) · [Verilog solution](../../solutions/Day%2006/131-sim__circuit5.sv) |

## Question and submitted solution

<a href="../../images/Day%2006/131-sim__circuit5.png"><img src="../../images/Day%2006/131-sim__circuit5.png" alt="Combinational circuit 5 question and submitted solution" width="100%"></a>

## What the question is asking

This circuit is a 4-bit lookup/multiplexer controlled by `c`. For selector values 0 through 3, Q chooses different input buses: 0→B, 1→E, 2→A, and 3→D. All other selector values produce `4'hf`.

The `case` statement is combinational and assigns Q in every branch, including `default`, so no latch is inferred. Input bus C is used as the selector, while the data buses retain their full 4-bit widths.

**Waveform technique:** locate periods where one candidate bus has a distinctive value, then see whether Q matches it for a particular C value. Repeating that across multiple simulations disambiguates buses that happen to share a value temporarily.

## Saved Verilog solution

```verilog
module top_module (
    input [3:0] a,
    input [3:0] b,
    input [3:0] c,
    input [3:0] d,
    input [3:0] e,
    output reg [3:0] q
);

    always @(*) begin
        case (c)
            4'd0: q = b;
            4'd1: q = e;
            4'd2: q = a;
            4'd3: q = d;
            default: q = 4'hf;
        endcase
    end

endmodule
```

## What I learned

_Fill this in during revision._
