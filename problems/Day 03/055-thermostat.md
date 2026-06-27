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
| Files | [Open screenshot at full resolution](../../images/Day%2003/055-thermostat.png) · [Verilog solution](../../solutions/Day%2003/055-thermostat.sv) |

## Question and submitted solution

<a href="../../images/Day%2003/055-thermostat.png"><img src="../../images/Day%2003/055-thermostat.png" alt="Thermostat question and submitted solution" width="100%"></a>

## What the question is asking

Implement the thermostat's heater, air-conditioner, and fan control rules from the temperature and mode inputs.

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
