# 030 — If statement latches

| Field | Value |
|---|---|
| Day | Day 02 |
| Last successful submission | 2026-06-24 4:18:47 PM |
| Course location | Verilog Language → Procedures |
| HDLBits identifier | `always_if2` |
| Attempts | 5 total: 3 incorrect, 0 compile error, 0 simulation error |
| Success rate | 40% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/always_if2) |
| Files | [Screenshot](../../images/Day%2002/030-always_if2.png) · [Verilog solution](../../solutions/Day%2002/030-always_if2.sv) |

## Problem and saved submission

![If statement latches problem and saved submission](../../images/Day%2002/030-always_if2.png)

## Saved Verilog solution

```verilog
// synthesis verilog_input_version verilog_2001
module top_module (
    input      cpu_overheated,
    output reg shut_off_computer,
    input      arrived,
    input      gas_tank_empty,
    output reg keep_driving  ); //

    always @(*) begin
        if (cpu_overheated)
           shut_off_computer = 1;
    end

    always @(*) begin
        if (~arrived)
           keep_driving = ~gas_tank_empty;
    end

endmodule
```

## What I learned

_Fill this in during revision._
