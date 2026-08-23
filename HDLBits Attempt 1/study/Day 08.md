# Day 08 — 2026-06-30

Completed problems: **1**

Each screenshot is embedded at the full width of the GitHub page. Select an image to open its original-resolution file.

## Index

| # | Time | Problem | Section | Problem note | Page contents | Source |
|---:|---|---:|---|---|---|---|
| 1 | 4:36:01 PM | [143](#problem-143) | Sequential Logic | [Counter 1-12](problems/Day%2008/143-exams__ece241_2014_q7a.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/exams/ece241_2014_q7a) |

---

<a id="problem-143"></a>
## 143 — Counter 1-12

[Problem note](problems/Day%2008/143-exams__ece241_2014_q7a.md) · [Verilog file](solutions/Day%2008/143-exams__ece241_2014_q7a.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/ece241_2014_q7a)

![Counter 1-12 question and submitted solution](images/Day%2008/143-exams__ece241_2014_q7a.png)

### What the question is asking

This problem does not ask for a new counter datapath. HDLBits supplies a four-bit counter and asks for the control signals that make it behave as a synchronous 1-through-12 counter. The datapath always loads the constant 1, so `c_d = 4'd1`. Its enable input follows the external enable, while its load input is asserted for either reset or the enabled rollover condition at Q=12.

Load has higher priority than enable inside the supplied `count4`. Therefore, when Q is 12 and enable is high, the same rising edge loads 1 instead of incrementing to 13. When Q is 12 and enable is low, neither load nor counting occurs, so the counter correctly holds 12. Reset forces `c_load` high independently of enable and synchronously loads 1 at the next rising edge.

**Control trace:** reset=1 loads 1; Q=7 with enable=1 advances to 8; Q=12 with enable=1 loads 1; Q=12 with enable=0 remains 12. A common error is making rollover depend only on Q=12, which would reload continuously even while the counter is disabled.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input reset,
    input enable,
    output [3:0] Q,
    output c_enable,
    output c_load,
    output [3:0] c_d
);
    assign c_enable = enable;
    assign c_load = reset | (enable & (Q == 4'd12));
    assign c_d = 4'd1;

    count4 the_counter (
        .clk(clk),
        .enable(enable),
        .load(c_load),
        .d(c_d),
        .Q(Q)
    );
endmodule
```
