# 141 — T flip-flop

| Field | Value |
|---|---|
| Day | Day 06 |
| Last successful submission | 2026-06-28 6:29:03 PM |
| Course location | Verification: Writing Testbenches → Writing Testbenches |
| HDLBits identifier | `tb/tff` |
| Attempts | 9 total: 2 incorrect, 5 compile error, 0 simulation error |
| Success rate | 22% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/tb/tff) |
| Files | [Open screenshot at full resolution](../../images/Day%2006/141-tb__tff.png) · [Verilog solution](../../solutions/Day%2006/141-tb__tff.sv) |

## Question and submitted solution

<a href="../../images/Day%2006/141-tb__tff.png"><img src="../../images/Day%2006/141-tb__tff.png" alt="T flip-flop question and submitted solution" width="100%"></a>

## What the question is asking

The testbench instantiates the supplied T flip-flop and creates separate clock and control processes. The clock starts low and toggles every 5 time units. Reset starts high and `t` starts low, so the first rising edge samples the synchronous reset and forces Q to its reset state. After 10 time units, reset is deasserted and T is asserted; subsequent rising edges toggle Q.

The word *synchronous* is crucial: changing reset does not immediately change Q. Reset only has an effect when a rising edge occurs while reset is high. With this timeline, the rising edge at t=5 performs the reset, reset becomes low at t=10, and the edge at t=15 performs the first toggle.

The DUT output is a wire because the T flip-flop drives it. Clock, reset, and T are registers because the testbench drives them procedurally. Keeping the free-running clock and one-time stimulus in separate `initial` processes is intentional concurrency: both timelines advance together under the simulator's event scheduler.

## Saved Verilog solution

```verilog
module top_module ();
    reg clk;
    reg reset;
    reg t;
    wire q;

    tff dut_instance (
        .clk(clk),
        .reset(reset),
        .t(t),
        .q(q)
    );

    initial begin
        clk = 1'b0;
        forever #5 clk = ~clk;
    end

    initial begin
        reset = 1'b1;
        t = 1'b0;
        #10 begin
            reset = 1'b0;
            t = 1'b1;
        end
    end
endmodule
```

## What I learned

_Fill this in during revision._
