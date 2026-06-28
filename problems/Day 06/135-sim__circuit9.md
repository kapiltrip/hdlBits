# 135 — Sequential circuit 9

| Field | Value |
|---|---|
| Day | Day 06 |
| Last successful submission | 2026-06-28 2:35:52 PM |
| Course location | Verification: Reading Simulations → Build a circuit from a simulation waveform |
| HDLBits identifier | `sim/circuit9` |
| Attempts | 3 total: 2 incorrect, 0 compile error, 0 simulation error |
| Success rate | 33% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/sim/circuit9) |
| Files | [Open screenshot at full resolution](../../images/Day%2006/135-sim__circuit9.png) · [Verilog solution](../../solutions/Day%2006/135-sim__circuit9.sv) |

## Question and submitted solution

<a href="../../images/Day%2006/135-sim__circuit9.png"><img src="../../images/Day%2006/135-sim__circuit9.png" alt="Sequential circuit 9 question and submitted solution" width="100%"></a>

## What the question is asking

The circuit is a modulo-7 counter with a synchronous load-like control. When `a=0`, the 4-bit state counts 0,1,2,3,4,5,6 and then wraps to 0. When `a=1` at a rising edge, the state is loaded with 4 instead of incrementing.

Q continuously exposes the registered count. All changes therefore occur after rising clock edges, not when A changes between edges.

**Trace examples:** count=6 and A=0 produces 0 on the next edge; count=2 and A=0 produces 3; any current count with A=1 produces 4. Priority is clear because the A branch is tested before the wrap/increment logic.

## Saved Verilog solution

```verilog
module top_module (
    input clk,
    input a,
    output [3:0] q
);
    reg [3:0] count;

    always @(posedge clk) begin
        if (!a) begin
            if (count == 4'b0110)
                count <= 4'b0000;
            else
                count <= count + 1'b1;
        end else begin
            count <= 4'b0100;
        end
    end

    assign q = count;

endmodule
```

## What I learned

_Fill this in during revision._
