# Day 04 — 2026-06-26

Completed problems: **19**

Each screenshot is embedded at the full width of the GitHub page. Select an image to open its original-resolution file.

## Index

| # | Time | Problem | Section | Problem note | Solution | Source |
|---:|---|---:|---|---|---|---|
| 1 | 12:09:54 AM | [089](#problem-089) | Sequential Logic | [Mux and DFF](problems/Day%2004/089-mt2015_muxdff.md) | [Code](solutions/Day%2004/089-mt2015_muxdff.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/mt2015_muxdff) |
| 2 | 12:25:46 AM | [090](#problem-090) | Sequential Logic | [Mux and DFF](problems/Day%2004/090-exams__2014_q4a.md) | [Code](solutions/Day%2004/090-exams__2014_q4a.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/exams/2014_q4a) |
| 3 | 12:00:31 AM | [091](#problem-091) | Sequential Logic | [DFFs and gates](problems/Day%2004/091-exams__ece241_2014_q4.md) | [Code](solutions/Day%2004/091-exams__ece241_2014_q4.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/exams/ece241_2014_q4) |
| 4 | 2:12:29 PM | [092](#problem-092) | Sequential Logic | [Create circuit from truth table](problems/Day%2004/092-exams__ece241_2013_q7.md) | [Code](solutions/Day%2004/092-exams__ece241_2013_q7.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/exams/ece241_2013_q7) |
| 5 | 2:28:20 PM | [093](#problem-093) | Sequential Logic | [Detect an edge](problems/Day%2004/093-edgedetect.md) | [Code](solutions/Day%2004/093-edgedetect.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/edgedetect) |
| 6 | 2:31:22 PM | [094](#problem-094) | Sequential Logic | [Detect both edges](problems/Day%2004/094-edgedetect2.md) | [Code](solutions/Day%2004/094-edgedetect2.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/edgedetect2) |
| 7 | 2:50:42 PM | [095](#problem-095) | Sequential Logic | [Edge capture register](problems/Day%2004/095-edgecapture.md) | [Code](solutions/Day%2004/095-edgecapture.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/edgecapture) |
| 8 | 3:07:56 PM | [096](#problem-096) | Sequential Logic | [Dual-edge triggered flip-flop](problems/Day%2004/096-dualedge.md) | [Code](solutions/Day%2004/096-dualedge.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/dualedge) |
| 9 | 1:01:36 AM | [097](#problem-097) | Sequential Logic | [Four-bit binary counter](problems/Day%2004/097-count15.md) | [Code](solutions/Day%2004/097-count15.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/count15) |
| 10 | 1:12:51 AM | [098](#problem-098) | Sequential Logic | [Decade counter](problems/Day%2004/098-count10.md) | [Code](solutions/Day%2004/098-count10.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/count10) |
| 11 | 1:21:20 AM | [099](#problem-099) | Sequential Logic | [Decade counter again](problems/Day%2004/099-count1to10.md) | [Code](solutions/Day%2004/099-count1to10.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/count1to10) |
| 12 | 1:31:52 AM | [100](#problem-100) | Sequential Logic | [Slow decade counter](problems/Day%2004/100-countslow.md) | [Code](solutions/Day%2004/100-countslow.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/countslow) |
| 13 | 4:10:18 PM | [101](#problem-101) | Sequential Logic | [4-bit shift register](problems/Day%2004/101-shift4.md) | [Code](solutions/Day%2004/101-shift4.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/shift4) |
| 14 | 4:23:55 PM | [102](#problem-102) | Sequential Logic | [Left/right rotator](problems/Day%2004/102-rotate100.md) | [Code](solutions/Day%2004/102-rotate100.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/rotate100) |
| 15 | 4:42:03 PM | [103](#problem-103) | Sequential Logic | [Left/right arithmetic shift by 1 or 8](problems/Day%2004/103-shift18.md) | [Code](solutions/Day%2004/103-shift18.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/shift18) |
| 16 | 5:21:13 PM | [104](#problem-104) | Sequential Logic | [5-bit LFSR](problems/Day%2004/104-lfsr5.md) | [Code](solutions/Day%2004/104-lfsr5.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/lfsr5) |
| 17 | 11:37:29 PM | [105](#problem-105) | Sequential Logic | [3-bit LFSR](problems/Day%2004/105-mt2015_lfsr.md) | [Code](solutions/Day%2004/105-mt2015_lfsr.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/mt2015_lfsr) |
| 18 | 11:03:20 PM | [106](#problem-106) | Sequential Logic | [32-bit LFSR](problems/Day%2004/106-lfsr32.md) | [Code](solutions/Day%2004/106-lfsr32.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/lfsr32) |
| 19 | 11:20:08 PM | [107](#problem-107) | Sequential Logic | [Shift register](problems/Day%2004/107-exams__m2014_q4k.md) | [Code](solutions/Day%2004/107-exams__m2014_q4k.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/exams/m2014_q4k) |

---

<a id="problem-089"></a>
## 089 — Mux and DFF

[Problem note](problems/Day%2004/089-mt2015_muxdff.md) · [Open screenshot at full resolution](images/Day%2004/089-mt2015_muxdff.png) · [Verilog file](solutions/Day%2004/089-mt2015_muxdff.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/mt2015_muxdff)

<a href="images/Day%2004/089-mt2015_muxdff.png"><img src="images/Day%2004/089-mt2015_muxdff.png" alt="Mux and DFF question and submitted solution" width="100%"></a>

### What the question is asking

Implement the circuit in which a multiplexer chooses the value captured by a D flip-flop.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input L,
    input r_in,
    input q_in,
    output reg Q
);

    always @(posedge clk)begin
         Q <= (L)?r_in:q_in;
    end
endmodule
```

---

<a id="problem-090"></a>
## 090 — Mux and DFF

[Problem note](problems/Day%2004/090-exams__2014_q4a.md) · [Open screenshot at full resolution](images/Day%2004/090-exams__2014_q4a.png) · [Verilog file](solutions/Day%2004/090-exams__2014_q4a.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/2014_q4a)

<a href="images/Day%2004/090-exams__2014_q4a.png"><img src="images/Day%2004/090-exams__2014_q4a.png" alt="Mux and DFF question and submitted solution" width="100%"></a>

### What the question is asking

Translate the exam's multiplexer-and-DFF schematic into equivalent sequential Verilog.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input w, R, E, L,
    output Q
);
    always @(posedge clk)begin
        Q<= (L)?R:(E)?w:Q;
    end
endmodule
```

---

<a id="problem-091"></a>
## 091 — DFFs and gates

[Problem note](problems/Day%2004/091-exams__ece241_2014_q4.md) · [Open screenshot at full resolution](images/Day%2004/091-exams__ece241_2014_q4.png) · [Verilog file](solutions/Day%2004/091-exams__ece241_2014_q4.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/ece241_2014_q4)

<a href="images/Day%2004/091-exams__ece241_2014_q4.png"><img src="images/Day%2004/091-exams__ece241_2014_q4.png" alt="DFFs and gates question and submitted solution" width="100%"></a>

### What the question is asking

Implement the shown network of D flip-flops and logic gates with the correct cycle-to-cycle behaviour.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input x,
    output z
);
reg q1,q2,q3;
    initial begin
        q1<=1'b0;
        q2<=1'b0;
        q3<=1'b0;
    end
    always @(posedge clk)begin
        q1<=q1^x;
        q2<=~q2 & x ;
        q3<= ~q3 | x;
    end
    assign z= ~(q1 | q2 | q3);
endmodule
```

---

<a id="problem-092"></a>
## 092 — Create circuit from truth table

[Problem note](problems/Day%2004/092-exams__ece241_2013_q7.md) · [Open screenshot at full resolution](images/Day%2004/092-exams__ece241_2013_q7.png) · [Verilog file](solutions/Day%2004/092-exams__ece241_2013_q7.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/ece241_2013_q7)

<a href="images/Day%2004/092-exams__ece241_2013_q7.png"><img src="images/Day%2004/092-exams__ece241_2013_q7.png" alt="Create circuit from truth table question and submitted solution" width="100%"></a>

### What the question is asking

Build the sequential circuit described by the state/output truth table, including its registered state.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input j,
    input k,
    output Q);

endmodule
```

---

<a id="problem-093"></a>
## 093 — Detect an edge

[Problem note](problems/Day%2004/093-edgedetect.md) · [Open screenshot at full resolution](images/Day%2004/093-edgedetect.png) · [Verilog file](solutions/Day%2004/093-edgedetect.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/edgedetect)

<a href="images/Day%2004/093-edgedetect.png"><img src="images/Day%2004/093-edgedetect.png" alt="Detect an edge question and submitted solution" width="100%"></a>

### What the question is asking

Generate a one-cycle pulse whenever each input bit makes a 0-to-1 transition.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input [7:0] in,
    output [7:0] pedge
);
    reg [7:0] prev;
    always @(posedge clk)begin
        prev<=in;
        pedge<=~prev&in;
    end
endmodule
```

---

<a id="problem-094"></a>
## 094 — Detect both edges

[Problem note](problems/Day%2004/094-edgedetect2.md) · [Open screenshot at full resolution](images/Day%2004/094-edgedetect2.png) · [Verilog file](solutions/Day%2004/094-edgedetect2.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/edgedetect2)

<a href="images/Day%2004/094-edgedetect2.png"><img src="images/Day%2004/094-edgedetect2.png" alt="Detect both edges question and submitted solution" width="100%"></a>

### What the question is asking

Generate a one-cycle pulse whenever each input bit changes in either direction.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input [7:0] in,
    output [7:0] anyedge
);
    reg [7:0] positive;
    reg [7:0] negative ;
    always @(posedge clk)begin
        positive<=in;
        negative<=in;
        anyedge <= (~positive& in) | (negative& ~ in);
    end
endmodule
```

---

<a id="problem-095"></a>
## 095 — Edge capture register

[Problem note](problems/Day%2004/095-edgecapture.md) · [Open screenshot at full resolution](images/Day%2004/095-edgecapture.png) · [Verilog file](solutions/Day%2004/095-edgecapture.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/edgecapture)

<a href="images/Day%2004/095-edgecapture.png"><img src="images/Day%2004/095-edgecapture.png" alt="Edge capture register question and submitted solution" width="100%"></a>

### What the question is asking

Set a register bit when a falling edge occurs and keep it set until a synchronous reset clears it.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input reset,
    input [31:0] in,
    output [31:0] out
);

endmodule
```

---

<a id="problem-096"></a>
## 096 — Dual-edge triggered flip-flop

[Problem note](problems/Day%2004/096-dualedge.md) · [Open screenshot at full resolution](images/Day%2004/096-dualedge.png) · [Verilog file](solutions/Day%2004/096-dualedge.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/dualedge)

<a href="images/Day%2004/096-dualedge.png"><img src="images/Day%2004/096-dualedge.png" alt="Dual-edge triggered flip-flop question and submitted solution" width="100%"></a>

### What the question is asking

Emulate dual-edge-triggered storage using logic that captures data on both rising and falling clock edges.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input d,
    output q
);
reg pos,neg;
    always @(posedge clk)begin
        pos<=d;
    end
    always @(negedge clk)begin
        neg<=d;
    end
    assign q= (clk) ?  pos:neg;
endmodule
```

---

<a id="problem-097"></a>
## 097 — Four-bit binary counter

[Problem note](problems/Day%2004/097-count15.md) · [Open screenshot at full resolution](images/Day%2004/097-count15.png) · [Verilog file](solutions/Day%2004/097-count15.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/count15)

<a href="images/Day%2004/097-count15.png"><img src="images/Day%2004/097-count15.png" alt="Four-bit binary counter question and submitted solution" width="100%"></a>

### What the question is asking

Implement a 4-bit binary counter with synchronous reset that naturally wraps after 15.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input reset,      // Synchronous active-high reset
    output [3:0] q
);
    reg [3:0] count;
    always @(posedge clk)begin
        if(reset) begin
            count<=4'b0000;
        end

        else begin
            if(count==4'b1111)
                count<=4'b0000;
            else
                count<=count+1'b1;
        end
    end
    assign q=count;
endmodule
```

---

<a id="problem-098"></a>
## 098 — Decade counter

[Problem note](problems/Day%2004/098-count10.md) · [Open screenshot at full resolution](images/Day%2004/098-count10.png) · [Verilog file](solutions/Day%2004/098-count10.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/count10)

<a href="images/Day%2004/098-count10.png"><img src="images/Day%2004/098-count10.png" alt="Decade counter question and submitted solution" width="100%"></a>

### What the question is asking

Implement a decade counter that counts from 0 through 9 and then wraps to 0.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input reset,        // Synchronous active-high reset
    output [3:0] q
);
    reg [3:0] count;
//counts from 0 to 9 8421  1001 1010
    always @(posedge clk)begin
        if(reset)begin
            count<=4'b0000;
        end else begin
            if(count>=4'b1001)
                count<=4'b0000;
            else
                count<=count+1'b1;
        end
    end
    assign q=count;
endmodule
```

---

<a id="problem-099"></a>
## 099 — Decade counter again

[Problem note](problems/Day%2004/099-count1to10.md) · [Open screenshot at full resolution](images/Day%2004/099-count1to10.png) · [Verilog file](solutions/Day%2004/099-count1to10.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/count1to10)

<a href="images/Day%2004/099-count1to10.png"><img src="images/Day%2004/099-count1to10.png" alt="Decade counter again question and submitted solution" width="100%"></a>

### What the question is asking

Implement the specified 1-to-10 decade count sequence with the required reset and enable behaviour.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input reset,
    output [3:0] q);

endmodule
```

---

<a id="problem-100"></a>
## 100 — Slow decade counter

[Problem note](problems/Day%2004/100-countslow.md) · [Open screenshot at full resolution](images/Day%2004/100-countslow.png) · [Verilog file](solutions/Day%2004/100-countslow.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/countslow)

<a href="images/Day%2004/100-countslow.png"><img src="images/Day%2004/100-countslow.png" alt="Slow decade counter question and submitted solution" width="100%"></a>

### What the question is asking

Create a decade counter that advances only when the slow-enable input is asserted.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input slowena,
    input reset,
    output [3:0] q
);
//0 to 9 inclusive
    reg [3:0] count;
    always @(posedge clk)begin
        if(reset)begin
            count <= 4'b0000;
        end else begin
            if(count>= 4'b1001 && slowena)
                count<=4'b0000;
            else if(slowena)
                count<=count+1'b1;

        end
    end
    assign q=count ;

endmodule
```

---

<a id="problem-101"></a>
## 101 — 4-bit shift register

[Problem note](problems/Day%2004/101-shift4.md) · [Open screenshot at full resolution](images/Day%2004/101-shift4.png) · [Verilog file](solutions/Day%2004/101-shift4.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/shift4)

<a href="images/Day%2004/101-shift4.png"><img src="images/Day%2004/101-shift4.png" alt="4-bit shift register question and submitted solution" width="100%"></a>

### What the question is asking

Build a 4-bit shift register with the specified load/shift controls and expose the requested stage output.

### Saved Verilog solution

```verilog
module top_module(
    input clk,
    input areset,  // async active-high reset to zero
    input load,
    input ena,
    input [3:0] data,
    output reg [3:0] q);

endmodule
```

---

<a id="problem-102"></a>
## 102 — Left/right rotator

[Problem note](problems/Day%2004/102-rotate100.md) · [Open screenshot at full resolution](images/Day%2004/102-rotate100.png) · [Verilog file](solutions/Day%2004/102-rotate100.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/rotate100)

<a href="images/Day%2004/102-rotate100.png"><img src="images/Day%2004/102-rotate100.png" alt="Left/right rotator question and submitted solution" width="100%"></a>

### What the question is asking

Build a 100-bit register that can hold, load, rotate left, or rotate right according to the controls.

### Saved Verilog solution

```verilog
module top_module(
    input clk,
    input load,
    input [1:0] ena,
    input [99:0] data,
    output reg [99:0] q);

endmodule
```

---

<a id="problem-103"></a>
## 103 — Left/right arithmetic shift by 1 or 8

[Problem note](problems/Day%2004/103-shift18.md) · [Open screenshot at full resolution](images/Day%2004/103-shift18.png) · [Verilog file](solutions/Day%2004/103-shift18.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/shift18)

<a href="images/Day%2004/103-shift18.png"><img src="images/Day%2004/103-shift18.png" alt="Left/right arithmetic shift by 1 or 8 question and submitted solution" width="100%"></a>

### What the question is asking

Build a 64-bit register that can load or perform left/right arithmetic shifts by either 1 or 8 positions.

### Saved Verilog solution

```verilog
module top_module(
    input clk,
    input load,
    input ena,
    input [1:0] amount,
    input [63:0] data,
    output reg [63:0] q
);
    always @(posedge clk)begin
        if(load)begin
            q<=data;
        end else if(ena)begin
            case (amount)
                2'b00:q<={q[62:0],1'b0};
                2'b01:q<= {q[55:0],8'd0};
                2'b10:q<={q[63],q[63:1]};
                2'b11:q<={{8{q[63]}},q[63:8]};

            endcase
        end
    end
endmodule
```

---

<a id="problem-104"></a>
## 104 — 5-bit LFSR

[Problem note](problems/Day%2004/104-lfsr5.md) · [Open screenshot at full resolution](images/Day%2004/104-lfsr5.png) · [Verilog file](solutions/Day%2004/104-lfsr5.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/lfsr5)

<a href="images/Day%2004/104-lfsr5.png"><img src="images/Day%2004/104-lfsr5.png" alt="5-bit LFSR question and submitted solution" width="100%"></a>

### What the question is asking

Implement the specified 5-bit linear-feedback shift register using the given feedback taps and reset state.

### Saved Verilog solution

```verilog
module top_module(
    input clk,
    input reset,    // Active-high synchronous reset to 5'h1
    output [4:0] q
);
    always @(posedge clk)begin
        if(reset)
            q<=5'h1;
        else begin
            q[4]<=q[0];
            q[3]<=q[4];
            q[2]<=q[3]^q[0];
            q[1]<=q[2];
            q[0]<=q[1];
        end
    end
endmodule
```

---

<a id="problem-105"></a>
## 105 — 3-bit LFSR

[Problem note](problems/Day%2004/105-mt2015_lfsr.md) · [Open screenshot at full resolution](images/Day%2004/105-mt2015_lfsr.png) · [Verilog file](solutions/Day%2004/105-mt2015_lfsr.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/mt2015_lfsr)

<a href="images/Day%2004/105-mt2015_lfsr.png"><img src="images/Day%2004/105-mt2015_lfsr.png" alt="3-bit LFSR question and submitted solution" width="100%"></a>

### What the question is asking

Implement the shown 3-bit LFSR and reproduce its required feedback sequence.

### Saved Verilog solution

```verilog
module top_module (
    input [2:0] SW,      // R
    input [1:0] KEY,     // L and clk
    output [2:0] LEDR
);
    reg q2,q1,q0;
    always @(posedge KEY[0])begin

        q2<=(KEY[1])?SW[2]:q1^q2;
        q1<=(KEY[1])?SW[1]:q0;
        q0<=(KEY[1])?SW[0]:q2;
    end
    assign LEDR={q2,q1,q0};
endmodule
```

---

<a id="problem-106"></a>
## 106 — 32-bit LFSR

[Problem note](problems/Day%2004/106-lfsr32.md) · [Open screenshot at full resolution](images/Day%2004/106-lfsr32.png) · [Verilog file](solutions/Day%2004/106-lfsr32.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/lfsr32)

<a href="images/Day%2004/106-lfsr32.png"><img src="images/Day%2004/106-lfsr32.png" alt="32-bit LFSR question and submitted solution" width="100%"></a>

### What the question is asking

Implement a 32-bit linear-feedback shift register with the specified tap positions.

### Saved Verilog solution

```verilog
module top_module(
    input clk,
    input reset,    // Active-high synchronous reset to 32'h1
    output [31:0] q
);

endmodule
```

---

<a id="problem-107"></a>
## 107 — Shift register

[Problem note](problems/Day%2004/107-exams__m2014_q4k.md) · [Open screenshot at full resolution](images/Day%2004/107-exams__m2014_q4k.png) · [Verilog file](solutions/Day%2004/107-exams__m2014_q4k.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/m2014_q4k)

<a href="images/Day%2004/107-exams__m2014_q4k.png"><img src="images/Day%2004/107-exams__m2014_q4k.png" alt="Shift register question and submitted solution" width="100%"></a>

### What the question is asking

Translate the exam shift-register schematic into clocked Verilog with the same data movement.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input resetn,   // synchronous reset
    input in,
    output out
);
reg q1,q2,q3,q4;
    always @(posedge clk)begin
        if(!resetn)begin
            q1<=1'b0;
            q2<=1'b0;
            q3<=1'b0;
            q4<=1'b0;
        end else begin
            q4<=q3;
            q2<=q1;
            q3<=q2;
            q1<=in;
        end
    end
    assign out= q4;
endmodule
```
