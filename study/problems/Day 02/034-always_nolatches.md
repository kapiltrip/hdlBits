# 034 — Avoiding latches

| Field | Value |
|---|---|
| Day | Day 02 |
| Last successful submission | 2026-06-24 6:00:14 PM |
| Course location | Verilog Language → Procedures |
| HDLBits identifier | `always_nolatches` |
| Attempts | 3 total: 0 incorrect, 2 compile error, 0 simulation error |
| Success rate | 33% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/always_nolatches) |
| Files | Screenshot rendered below · [Verilog solution](../../solutions/Day%2002/034-always_nolatches.sv) |

## Question and submitted solution

![Avoiding latches question and submitted solution](../../images/Day%2002/034-always_nolatches.png)

## What the question is asking

Complete the combinational case logic with safe defaults so no output retains an old value or infers a latch.

## Saved Verilog solution

```verilog
// synthesis verilog_input_version verilog_2001
module top_module (
    input [15:0] scancode,
    output reg left,
    output reg down,
    output reg right,
    output reg up
);
    always @(*)begin
        left=1'b0;
        right=1'b0;
        up=1'b0;
        down=1'b0;
        casez (scancode)
            16'he06b:left=1;
            16'he072:down=1;
            16'he074:right=1;
            16'he075:up=1;

        endcase
    end
endmodule
```

## What I learned

_Fill this in during revision._
