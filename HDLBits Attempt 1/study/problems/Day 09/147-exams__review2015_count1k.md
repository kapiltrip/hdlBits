# 147 — Counter with period 1000

| Field | Value |
|---|---|
| Day | Day 09 |
| Last successful submission | 2026-07-02 4:31:18 PM |
| Course location | Circuits → Building Larger Circuits |
| HDLBits identifier | `exams/review2015_count1k` |
| Attempts | 1 total: 0 incorrect, 0 compile error, 0 simulation error |
| Success rate | 100% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/exams/review2015_count1k) |
| Files | Screenshot rendered below · [Verilog solution](../../solutions/Day%2009/147-exams__review2015_count1k.sv) |

## Question and submitted solution

![Counter with period 1000 question and submitted solution](../../images/Day%2009/147-exams__review2015_count1k.png)

## What the question is asking

This design is a modulo-1000 synchronous counter. Its legal sequence is 0, 1, 2, ... 999, then back to 0, which gives exactly 1000 distinct states and therefore a period of 1000 clock cycles. Ten bits are required because nine bits can represent only 0 through 511, while ten bits can represent the terminal value 999.

The clocked process gives synchronous reset the highest priority. When reset is sampled high on a rising edge, the register becomes zero. Otherwise, the terminal-count comparison is evaluated using the old value: 999 loads zero, and every other value increments by one. A nonblocking assignment is appropriate because q represents registered state and changes only after the active clock edge.

The explicit terminal comparison is essential. Letting a 10-bit binary register overflow naturally would produce a modulo-1024 counter, so values 1000 through 1023 would incorrectly appear in the sequence. The separate internal register is connected continuously to q, although q could equivalently be declared as a register and updated directly.

**Boundary trace:** 998 advances to 999; 999 advances to 0; asserting reset while the count is 417 loads 0 at the next rising edge.

## Saved Verilog solution

```verilog
module top_module (
    input clk,
    input reset,
    output [9:0] q
);
    reg [9:0] count;

    always @(posedge clk) begin
        if (reset)
            count <= 10'd0;
        else if (count == 10'd999)
            count <= 10'd0;
        else
            count <= count + 10'd1;
    end

    assign q = count;
endmodule
```

## What I learned

_Fill this in during revision._
