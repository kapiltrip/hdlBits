# 134 — Sequential circuit 8

| Field | Value |
|---|---|
| Day | Day 06 |
| Last successful submission | 2026-06-28 2:46:53 PM |
| Course location | Verification: Reading Simulations → Build a circuit from a simulation waveform |
| HDLBits identifier | `sim/circuit8` |
| Attempts | 18 total: 14 incorrect, 3 compile error, 0 simulation error |
| Success rate | 6% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/sim/circuit8) |
| Files | Screenshot rendered below · [Verilog solution](../../solutions/Day%2006/134-sim__circuit8.sv) |

## Question and submitted solution

![Sequential circuit 8 question and submitted solution](../../images/Day%2006/134-sim__circuit8.png)

## What the question is asking

The waveform is reproduced by two level/edge-sensitive storage stages. P is a transparent-high latch: while `clock=1`, P follows A; while the clock is low, P holds the last value seen during the high phase. The incomplete assignment inside the combinational block intentionally infers that latch.

Q updates on the falling edge with `q <= p`. Since P has just been tracking A during the high phase, Q captures the final latched value at the high-to-low transition and then holds it.

**Trace method:** during a high clock phase, changes on A appear on P but not immediately on Q. At the falling edge, Q takes P. During the low phase, later A changes affect neither stored output. This timing distinguishes a latch-plus-negedge-flip-flop chain from two ordinary flip-flops.

## Saved Verilog solution

```verilog
module top_module (
    input clock,
    input a,
    output reg p,
    output reg q
);

    // p is transparent while clock is high.
    always @(*) begin
        if (clock)
            p = a;
    end

    // q samples p when the clock falls.
    always @(negedge clock) begin
        q <= p;
    end

endmodule
```

## What I learned

_Fill this in during revision._
