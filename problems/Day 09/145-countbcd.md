# 145 — 4-digit decimal counter

| Field | Value |
|---|---|
| Day | Day 09 |
| Last successful submission | 2026-07-02 12:08:54 AM |
| Course location | Circuits → Sequential Logic → Counters |
| HDLBits identifier | `countbcd` |
| Attempts | 11 total: 1 incorrect, 9 compile error, 0 simulation error |
| Success rate | 9% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/countbcd) |
| Files | [Open screenshot at full resolution](../../images/Day%2009/145-countbcd.png) · [Verilog solution](../../solutions/Day%2009/145-countbcd.sv) |

## Question and submitted solution

<a href="../../images/Day%2009/145-countbcd.png"><img src="../../images/Day%2009/145-countbcd.png" alt="4-digit decimal counter question and submitted solution" width="100%"></a>

## What the question is asking

This is a four-digit synchronous BCD counter. Each four-bit digit stores only 0 through 9, and every digit is clocked by the same rising edge. The ones digit advances on every enabled cycle of the overall design. Each higher digit advances only when every less-significant digit is currently 9.

The enable outputs expose those carry conditions: `ena[1]` is high at x9, `ena[2]` at x99, and `ena[3]` at x999. Because nonblocking assignments evaluate their right-hand sides from the old state, the same edge that changes 0099 to 0100 sees both lower digits at 9, clears them, and increments the hundreds digit.

The output concatenation `{digit3,digit2,digit1,digit0}` places the thousands nibble in q[15:12] and the ones nibble in q[3:0]. Reset is synchronous and clears all four digits together. The key pitfall is checking an already-updated lower digit; synchronous carry must be derived from the values present immediately before the active edge.

## Saved Verilog solution

```verilog
module top_module (
    input clk,
    input reset,
    output [3:1] ena,
    output [15:0] q
);
    reg [3:0] digit0, digit1, digit2, digit3;

    assign ena[1] = (digit0 == 4'd9);
    assign ena[2] = (digit0 == 4'd9) && (digit1 == 4'd9);
    assign ena[3] = (digit0 == 4'd9) && (digit1 == 4'd9) && (digit2 == 4'd9);

    always @(posedge clk) begin
        if (reset) begin
            digit0 <= 4'd0;
            digit1 <= 4'd0;
            digit2 <= 4'd0;
            digit3 <= 4'd0;
        end
        else begin
            if (digit0 == 4'd9)
                digit0 <= 4'd0;
            else
                digit0 <= digit0 + 1'b1;

            if (ena[1]) begin
                if (digit1 == 4'd9)
                    digit1 <= 4'd0;
                else
                    digit1 <= digit1 + 1'b1;
            end

            if (ena[2]) begin
                if (digit2 == 4'd9)
                    digit2 <= 4'd0;
                else
                    digit2 <= digit2 + 1'b1;
            end

            if (ena[3]) begin
                if (digit3 == 4'd9)
                    digit3 <= 4'd0;
                else
                    digit3 <= digit3 + 1'b1;
            end
        end
    end

    assign q = {digit3, digit2, digit1, digit0};
endmodule
```

## What I learned

_Fill this in during revision._
