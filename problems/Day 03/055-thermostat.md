# 055 — Thermostat

| Field | Value |
|---|---|
| Day | Day 03 |
| Last successful submission | 2026-06-25 4:47:58 PM |
| Course location | Circuits → Combinational Logic → Basic Gates |
| HDLBits identifier | `thermostat` |
| Attempts | 2 total: 0 incorrect, 1 compile error, 0 simulation error |
| Success rate | 50% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/thermostat) |
| Files | [Screenshot](../../images/Day%2003/055-thermostat.png) · [Verilog solution](../../solutions/Day%2003/055-thermostat.sv) |

## Problem and saved submission

![Thermostat problem and saved submission](../../images/Day%2003/055-thermostat.png)

## Saved Verilog solution

```verilog
module top_module (
    input too_cold,
    input too_hot,
    input mode,
    input fan_on,
    output heater,
    output aircon,
    output fan
); 
    assign heater = mode & too_cold;
    assign aircon = ~mode & too_hot;
    assign fan    = fan_on | heater | aircon;
endmodule
//wand , wor to resolve, teh conditions
```

## What I learned

_Fill this in during revision._
