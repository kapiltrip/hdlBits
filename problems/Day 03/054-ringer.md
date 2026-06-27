# 054 — Ring or vibrate?

| Field | Value |
|---|---|
| Day | Day 03 |
| Last successful submission | 2026-06-25 12:48:24 AM |
| Course location | Circuits → Combinational Logic → Basic Gates |
| HDLBits identifier | `ringer` |
| Attempts | 5 total: 1 incorrect, 3 compile error, 0 simulation error |
| Success rate | 20% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/ringer) |
| Files | [Screenshot](../../images/Day%2003/054-ringer.png) · [Verilog solution](../../solutions/Day%2003/054-ringer.sv) |

## Problem and saved submission

![Ring or vibrate? problem and saved submission](../../images/Day%2003/054-ringer.png)

## Saved Verilog solution

```verilog
module top_module (
    input ring,
    input vibrate_mode,
    output ringer,       // Make sound
    output motor         // Vibrate
);
    assign ringer = ring & ~vibrate_mode;
    assign motor  = ring & vibrate_mode;
endmodule
```

## What I learned

_Fill this in during revision._
