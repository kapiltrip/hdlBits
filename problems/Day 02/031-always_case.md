# 031 — Case statement

| Field | Value |
|---|---|
| Day | Day 02 |
| Last successful submission | 2026-06-24 4:22:44 PM |
| Course location | Verilog Language → Procedures |
| HDLBits identifier | `always_case` |
| Attempts | 2 total: 0 incorrect, 1 compile error, 0 simulation error |
| Success rate | 50% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/always_case) |
| Files | [Open screenshot at full resolution](../../images/Day%2002/031-always_case.png) · [Verilog solution](../../solutions/Day%2002/031-always_case.sv) |

## Question and submitted solution

<a href="../../images/Day%2002/031-always_case.png"><img src="../../images/Day%2002/031-always_case.png" alt="Case statement question and submitted solution" width="100%"></a>

## What the question is asking

Use a case statement to select one of several input values according to the selector.

## Saved Verilog solution

```verilog
// synthesis verilog_input_version verilog_2001
module top_module (
    input [2:0] sel,
    input [3:0] data0,
    input [3:0] data1,
    input [3:0] data2,
    input [3:0] data3,
    input [3:0] data4,
    input [3:0] data5,
    output reg [3:0] out
);//

    always@(*) begin  // This is a combinational circuit
        case(sel)
            3'b000:out= data0;
            3'b001:out= data1;
            3'b010:out= data2;
            3'b011:out= data3;
            3'b100:out= data4;
            3'b101:out= data5;
            default :out= 4'b0000;
        endcase
    end

endmodule
```

## What I learned

_Fill this in during revision._
