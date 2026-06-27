# 033 — Priority encoder with casez

| Field | Value |
|---|---|
| Day | Day 02 |
| Last successful submission | 2026-06-24 5:44:37 PM |
| Course location | Verilog Language → Procedures |
| HDLBits identifier | `always_casez` |
| Attempts | 2 total: 1 incorrect, 0 compile error, 0 simulation error |
| Success rate | 50% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/always_casez) |
| Files | [Screenshot](../../images/Day%2002/033-always_casez.png) · [Verilog solution](../../solutions/Day%2002/033-always_casez.sv) |

## Problem and saved submission

![Priority encoder with casez problem and saved submission](../../images/Day%2002/033-always_casez.png)

## Saved Verilog solution

```verilog
// synthesis verilog_input_version verilog_2001
module top_module (
    input [7:0] in,
    output reg [2:0] pos 
);
    always @(*)begin
        casez (in)
            8'b???????1:pos=3'b000;
            8'b??????10:pos=3'b001;
            8'b?????100:pos=3'b010;
            8'b????1000:pos=3'b011;
            8'b???10000:pos=3'b100;
            8'b??100000:pos=3'b101;
            8'b?1000000:pos=3'b110;
            8'b10000000:pos=3'b111;
            default : pos = 3'b000;
            
        endcase
    end
endmodule
```

## What I learned

_Fill this in during revision._
