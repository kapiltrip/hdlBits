# 146 — 12-hour clock

| Field | Value |
|---|---|
| Day | Day 09 |
| Last successful submission | 2026-07-02 2:55:03 PM |
| Course location | Circuits → Sequential Logic → Counters |
| HDLBits identifier | `count_clock` |
| Attempts | 6 total: 0 incorrect, 4 compile error, 0 simulation error |
| Success rate | 33% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/count_clock) |
| Files | [Open screenshot at full resolution](../../images/Day%2009/146-count_clock.png) · [Verilog solution](../../solutions/Day%2009/146-count_clock.sv) |

## Question and submitted solution

<a href="../../images/Day%2009/146-count_clock.png"><img src="../../images/Day%2009/146-count_clock.png" alt="12-hour clock question and submitted solution" width="100%"></a>

## What the question is asking

The clock contains six BCD digits plus one AM/PM state bit. The outer enable gates the entire time update, while synchronous reset has priority and loads the required 12:00:00 AM state. If enable is low, every register retains its previous value.

Seconds normally increment their ones nibble. At x9, the ones nibble clears and the tens nibble increments; at 59, the complete seconds byte clears and the same edge advances minutes. Minutes use the identical BCD rollover pattern. Only when both seconds and minutes are 59 does the hour update.

Hours require a non-decimal sequence: 01 through 12. The 09-to-10 transition uses the BCD nibble carry, 11 advances to 12 and toggles PM, and 12 rolls to 01 without toggling PM. This places the AM/PM transition at 11:59:59 to 12:00:00, not at 12:59:59 to 01:00:00.

All state changes use nonblocking assignments in one clocked process, so each decision observes the same pre-edge time. That property lets the nested terminal-count tests propagate a one-cycle carry from seconds through minutes into hours without generating derived clocks.

## Saved Verilog solution

```verilog
module top_module (
    input clk,
    input reset,
    input ena,
    output reg pm,
    output reg [7:0] hh,
    output reg [7:0] mm,
    output reg [7:0] ss
);
    always @(posedge clk) begin
        if (reset) begin
            pm <= 1'b0;
            hh <= 8'h12;
            mm <= 8'h00;
            ss <= 8'h00;
        end
        else if (ena) begin
            if (ss == 8'h59) begin
                ss <= 8'h00;

                if (mm == 8'h59) begin
                    mm <= 8'h00;

                    if (hh == 8'h11) begin
                        hh <= 8'h12;
                        pm <= ~pm;
                    end
                    else if (hh == 8'h12) begin
                        hh <= 8'h01;
                    end
                    else if (hh[3:0] == 4'd9) begin
                        hh[3:0] <= 4'd0;
                        hh[7:4] <= hh[7:4] + 4'd1;
                    end
                    else begin
                        hh[3:0] <= hh[3:0] + 4'd1;
                    end
                end
                else if (mm[3:0] == 4'd9) begin
                    mm[3:0] <= 4'd0;
                    mm[7:4] <= mm[7:4] + 4'd1;
                end
                else begin
                    mm[3:0] <= mm[3:0] + 4'd1;
                end
            end
            else if (ss[3:0] == 4'd9) begin
                ss[3:0] <= 4'd0;
                ss[7:4] <= ss[7:4] + 4'd1;
            end
            else begin
                ss[3:0] <= ss[3:0] + 4'd1;
            end
        end
    end
endmodule
```

## What I learned

_Fill this in during revision._
