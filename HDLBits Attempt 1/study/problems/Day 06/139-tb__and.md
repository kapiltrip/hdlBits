# 139 — AND gate

| Field | Value |
|---|---|
| Day | Day 06 |
| Last successful submission | 2026-06-28 6:15:10 PM |
| Course location | Verification: Writing Testbenches → Writing Testbenches |
| HDLBits identifier | `tb/and` |
| Attempts | 7 total: 2 incorrect, 4 compile error, 0 simulation error |
| Success rate | 14% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/tb/and) |
| Files | Screenshot rendered below · [Verilog solution](../../solutions/Day%2006/139-tb__and.sv) |

## Question and submitted solution

![AND gate question and submitted solution](../../images/Day%2006/139-tb__and.png)

## What the question is asking

This testbench verifies a two-input AND gate exhaustively. The DUT input is a 2-bit procedural register, while the DUT output is a wire because it is driven by the instantiated module. A loop enumerates the four binary input combinations 00, 01, 10, and 11, holding each combination for 10 simulation time units.

Using `in = i[1:0]` makes the mapping from loop counter to stimulus width explicit. The observed output should remain zero for the first three patterns and become one only for `2'b11`. This is exhaustive verification because a two-input combinational circuit has exactly four possible input states.

The important separation is stimulus versus response: the testbench drives `in`, but only observes `out`. Declaring the response as a procedural variable or assigning to it from the testbench would create an additional driver and invalidate the test. For larger circuits, the same enumeration idea scales until the input space becomes too large, at which point constrained or directed vectors are preferable.

## Saved Verilog solution

```verilog
module top_module ();
    reg [1:0] in;
    wire out;
    integer i;

    andgate dut_instance (
        .in(in),
        .out(out)
    );

    initial begin
        for (i = 0; i < 4; i = i + 1) begin
            in = i[1:0];
            #10;
        end
    end
endmodule
```

## What I learned

_Fill this in during revision._
