# 126 — Case statement

| Field | Value |
|---|---|
| Day | Day 06 |
| Last successful submission | 2026-06-28 1:28:42 AM |
| Course location | Verification: Reading Simulations → Finding bugs in code |
| HDLBits identifier | `bugs_case` |
| Attempts | 5 total: 2 incorrect, 2 compile error, 0 simulation error |
| Success rate | 20% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/bugs_case) |
| Files | Screenshot rendered below · [Verilog solution](../../solutions/Day%2006/126-bugs_case.sv) |

## Question and submitted solution

![Case statement question and submitted solution](../../images/Day%2006/126-bugs_case.png)

## What the question is asking

This decoder recognizes the PS/2 scan codes for decimal keys 0 through 9. Each recognized hexadecimal code assigns the corresponding 4-bit digit and asserts `valid`.

The critical repair is to provide defaults before the `case`: `out=0` and `valid=0`. Every recognized branch overrides both values. Any unlisted scan code therefore produces a deterministic invalid result instead of retaining the previous output and inferring latches.

Examples: `8'h45` maps to digit 0, `8'h16` to 1, and `8'h46` to 9. The `default` branch repeats the safe values, making the intended behaviour explicit.

**Debugging checklist:** verify literal width, hexadecimal code, digit mapping, and assignments to every combinational output on every path.

## Saved Verilog solution

```verilog
module top_module (
    input [7:0] code,
    output reg [3:0] out,
    output reg valid
);

    always @(*) begin
        out = 4'd0;
        valid = 1'b0;

        case (code)
            8'h45: begin out = 4'd0; valid = 1'b1; end
            8'h16: begin out = 4'd1; valid = 1'b1; end
            8'h1e: begin out = 4'd2; valid = 1'b1; end
            8'h26: begin out = 4'd3; valid = 1'b1; end
            8'h25: begin out = 4'd4; valid = 1'b1; end
            8'h2e: begin out = 4'd5; valid = 1'b1; end
            8'h36: begin out = 4'd6; valid = 1'b1; end
            8'h3d: begin out = 4'd7; valid = 1'b1; end
            8'h3e: begin out = 4'd8; valid = 1'b1; end
            8'h46: begin out = 4'd9; valid = 1'b1; end
            default: begin out = 4'd0; valid = 1'b0; end
        endcase
    end

endmodule
```

## What I learned

_Fill this in during revision._
