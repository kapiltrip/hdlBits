# 148 — 4-bit shift register and down counter

| Field | Value |
|---|---|
| Day | Day 09 |
| Last successful submission | 2026-07-02 4:47:48 PM |
| Course location | Circuits → Building Larger Circuits |
| HDLBits identifier | `exams/review2015_shiftcount` |
| Attempts | 12 total: 7 incorrect, 4 compile error, 0 simulation error |
| Success rate | 8% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/exams/review2015_shiftcount) |
| Files | Screenshot rendered below · [Verilog solution](../../solutions/Day%2009/148-exams__review2015_shiftcount.sv) |

## Question and submitted solution

![4-bit shift register and down counter question and submitted solution](../../images/Day%2009/148-exams__review2015_shiftcount.png)

## What the question is asking

One four-bit register performs two different operations. When shift_ena is asserted, the existing bits move toward the most-significant end and the serial data bit enters bit 0 through {register[2:0], data}. Supplying a four-bit word most-significant bit first therefore reconstructs that word after four enabled shifts.

When count_ena is asserted, the same storage acts as a modulo-16 down counter. Values 15 through 1 decrement normally, while 0 explicitly wraps to 15. Four-bit subtraction would also wrap naturally, but the terminal branch makes the intended rollover unambiguous.

The specification guarantees that shift_ena and count_ena are never high together, so their relative priority is intentionally irrelevant. The saved solution uses two independent if statements to reflect that contract. If both controls were asserted despite the contract, the later nonblocking assignment would win; a production interface without the guarantee should instead define priority explicitly with if/else if.

With both controls low, no assignment occurs and the register holds its value. There is no reset input, so the environment must shift in a complete value before relying on the state.

## Saved Verilog solution

```verilog
module top_module (
    input clk,
    input shift_ena,
    input count_ena,
    input data,
    output [3:0] q
);
    reg [3:0] shift_count;

    always @(posedge clk) begin
        if (shift_ena)
            shift_count <= {shift_count[2:0], data};
        if (count_ena) begin
            if (shift_count == 4'd0)
                shift_count <= 4'd15;
            else
                shift_count <= shift_count - 4'd1;
        end
    end

    assign q = shift_count;
endmodule
```

## What I learned

_Fill this in during revision._
