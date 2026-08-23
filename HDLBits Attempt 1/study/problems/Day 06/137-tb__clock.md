# 137 — Clock

| Field | Value |
|---|---|
| Day | Day 06 |
| Last successful submission | 2026-06-28 5:45:53 PM |
| Course location | Verification: Writing Testbenches → Writing Testbenches |
| HDLBits identifier | `tb/clock` |
| Attempts | 5 total: 0 incorrect, 4 compile error, 0 simulation error |
| Success rate | 20% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/tb/clock) |
| Files | Screenshot rendered below · [Verilog solution](../../solutions/Day%2006/137-tb__clock.sv) |

## Question and submitted solution

![Clock question and submitted solution](../../images/Day%2006/137-tb__clock.png)

## What the question is asking

This exercise moves from describing hardware to controlling simulation time. The top-level testbench has no ports because it is the simulation root. It declares an internal `reg clk`, connects that signal to the supplied `dut` instance, initializes it to zero at time 0, and toggles it every 5 ps.

Two half-periods make the required 10 ps period. Starting from zero means the first scheduled toggle is a rising edge at 5 ps, exactly matching the requested waveform. The `initial` block runs once, while `always #5` repeats forever; these are simulation constructs and are not intended to synthesize into physical logic.

**Timing trace:** `clk=0` at t=0, 1 at t=5, 0 at t=10, 1 at t=15, and so on. A common error is using `#10` for each toggle, which produces a 20 ps full period. Another is leaving the clock uninitialized: negating an unknown `X` still produces `X`, so the clock never becomes usable.

## Saved Verilog solution

```verilog
module top_module ();
    reg clk;

    dut dut_instance (
        .clk(clk)
    );

    initial
        clk = 1'b0;

    always #5
        clk = ~clk;
endmodule
```

## What I learned

_Fill this in during revision._
