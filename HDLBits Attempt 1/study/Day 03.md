# Day 03 — 2026-06-25

Completed problems: **42**

Each screenshot is embedded at the full width of the GitHub page. Select an image to open its original-resolution file.

## Index

| # | Time | Problem | Section | Problem note | Page contents | Source |
|---:|---|---:|---|---|---|---|
| 1 | 12:00:14 AM | [041](#problem-041) | More Verilog Features | [Generate for-loop: 100-digit BCD adder](problems/Day%2003/041-bcdadd100.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/bcdadd100) |
| 2 | 12:04:10 AM | [047](#problem-047) | Combinational Logic | [More logic gates](problems/Day%2003/047-gates.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/gates) |
| 3 | 12:05:55 AM | [048](#problem-048) | Combinational Logic | [7420 chip](problems/Day%2003/048-7420.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/7420) |
| 4 | 12:12:33 AM | [049](#problem-049) | Combinational Logic | [Truth tables](problems/Day%2003/049-truthtable1.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/truthtable1) |
| 5 | 12:14:30 AM | [050](#problem-050) | Combinational Logic | [Two-bit equality](problems/Day%2003/050-mt2015_eq2.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/mt2015_eq2) |
| 6 | 12:15:29 AM | [051](#problem-051) | Combinational Logic | [Simple circuit A](problems/Day%2003/051-mt2015_q4a.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/mt2015_q4a) |
| 7 | 12:16:24 AM | [052](#problem-052) | Combinational Logic | [Simple circuit B](problems/Day%2003/052-mt2015_q4b.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/mt2015_q4b) |
| 8 | 12:33:06 AM | [053](#problem-053) | Combinational Logic | [Combine circuits A and B](problems/Day%2003/053-mt2015_q4.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/mt2015_q4) |
| 9 | 12:48:24 AM | [054](#problem-054) | Combinational Logic | [Ring or vibrate?](problems/Day%2003/054-ringer.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/ringer) |
| 10 | 4:47:58 PM | [055](#problem-055) | Combinational Logic | [Thermostat](problems/Day%2003/055-thermostat.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/thermostat) |
| 11 | 12:58:42 AM | [056](#problem-056) | Combinational Logic | [3-bit population count](problems/Day%2003/056-popcount3.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/popcount3) |
| 12 | 9:45:17 PM | [057](#problem-057) | Combinational Logic | [Gates and vectors](problems/Day%2003/057-gatesv.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/gatesv) |
| 13 | 10:13:17 PM | [058](#problem-058) | Combinational Logic | [Even longer vectors](problems/Day%2003/058-gatesv100.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/gatesv100) |
| 14 | 1:06:47 AM | [059](#problem-059) | Combinational Logic | [2-to-1 multiplexer](problems/Day%2003/059-mux2to1.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/mux2to1) |
| 15 | 1:07:52 AM | [060](#problem-060) | Combinational Logic | [2-to-1 bus multiplexer](problems/Day%2003/060-mux2to1v.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/mux2to1v) |
| 16 | 2:44:03 PM | [061](#problem-061) | Combinational Logic | [9-to-1 multiplexer](problems/Day%2003/061-mux9to1v.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/mux9to1v) |
| 17 | 2:42:55 PM | [062](#problem-062) | Combinational Logic | [256-to-1 multiplexer](problems/Day%2003/062-mux256to1.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/mux256to1) |
| 18 | 2:46:53 PM | [063](#problem-063) | Combinational Logic | [256-to-1 4-bit multiplexer](problems/Day%2003/063-mux256to1v.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/mux256to1v) |
| 19 | 3:25:33 PM | [064](#problem-064) | Combinational Logic | [Half adder](problems/Day%2003/064-hadd.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/hadd) |
| 20 | 3:24:38 PM | [066](#problem-066) | Combinational Logic | [3-bit binary adder](problems/Day%2003/066-adder3.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/adder3) |
| 21 | 3:20:07 PM | [067](#problem-067) | Combinational Logic | [Adder](problems/Day%2003/067-exams__m2014_q4j.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/exams/m2014_q4j) |
| 22 | 5:28:33 PM | [068](#problem-068) | Combinational Logic | [Signed addition overflow](problems/Day%2003/068-exams__ece241_2014_q1c.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/exams/ece241_2014_q1c) |
| 23 | 5:26:53 PM | [069](#problem-069) | Combinational Logic | [100-bit binary adder](problems/Day%2003/069-adder100.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/adder100) |
| 24 | 5:16:55 PM | [070](#problem-070) | Combinational Logic | [4-digit BCD adder](problems/Day%2003/070-bcdadd4.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/bcdadd4) |
| 25 | 5:31:33 PM | [071](#problem-071) | Combinational Logic | [3-variable](problems/Day%2003/071-kmap1.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/kmap1) |
| 26 | 5:35:18 PM | [072](#problem-072) | Combinational Logic | [4-variable](problems/Day%2003/072-kmap2.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/kmap2) |
| 27 | 3:39:22 PM | [073](#problem-073) | Combinational Logic | [4-variable](problems/Day%2003/073-kmap3.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/kmap3) |
| 28 | 3:49:07 PM | [074](#problem-074) | Combinational Logic | [4-variable](problems/Day%2003/074-kmap4.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/kmap4) |
| 29 | 6:04:35 PM | [075](#problem-075) | Combinational Logic | [Minimum SOP and POS](problems/Day%2003/075-exams__ece241_2013_q2.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/exams/ece241_2013_q2) |
| 30 | 5:39:50 PM | [076](#problem-076) | Combinational Logic | [Karnaugh map](problems/Day%2003/076-exams__m2014_q3.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/exams/m2014_q3) |
| 31 | 10:17:24 PM | [077](#problem-077) | Combinational Logic | [Karnaugh map](problems/Day%2003/077-exams__2012_q1g.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/exams/2012_q1g) |
| 32 | 10:07:59 PM | [078](#problem-078) | Combinational Logic | [K-map implemented with a multiplexer](problems/Day%2003/078-exams__ece241_2014_q3.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/exams/ece241_2014_q3) |
| 33 | 10:21:47 PM | [079](#problem-079) | Sequential Logic | [D flip-flop](problems/Day%2003/079-dff.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/dff) |
| 34 | 10:22:47 PM | [080](#problem-080) | Sequential Logic | [D flip-flops](problems/Day%2003/080-dff8.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/dff8) |
| 35 | 10:25:54 PM | [081](#problem-081) | Sequential Logic | [DFF with reset](problems/Day%2003/081-dff8r.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/dff8r) |
| 36 | 10:28:00 PM | [082](#problem-082) | Sequential Logic | [DFF with reset value](problems/Day%2003/082-dff8p.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/dff8p) |
| 37 | 10:29:11 PM | [083](#problem-083) | Sequential Logic | [DFF with asynchronous reset](problems/Day%2003/083-dff8ar.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/dff8ar) |
| 38 | 10:53:33 PM | [084](#problem-084) | Sequential Logic | [DFF with byte enable](problems/Day%2003/084-dff16e.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/dff16e) |
| 39 | 11:13:53 PM | [085](#problem-085) | Sequential Logic | [D Latch](problems/Day%2003/085-exams__m2014_q4a.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/exams/m2014_q4a) |
| 40 | 10:43:06 PM | [086](#problem-086) | Sequential Logic | [DFF](problems/Day%2003/086-exams__m2014_q4b.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/exams/m2014_q4b) |
| 41 | 10:56:24 PM | [087](#problem-087) | Sequential Logic | [DFF](problems/Day%2003/087-exams__m2014_q4c.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/exams/m2014_q4c) |
| 42 | 11:16:12 PM | [088](#problem-088) | Sequential Logic | [DFF+gate](problems/Day%2003/088-exams__m2014_q4d.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/exams/m2014_q4d) |

---

<a id="problem-041"></a>
## 041 — Generate for-loop: 100-digit BCD adder

[Problem note](problems/Day%2003/041-bcdadd100.md) · [Verilog file](solutions/Day%2003/041-bcdadd100.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/bcdadd100)

![Generate for-loop: 100-digit BCD adder question and submitted solution](images/Day%2003/041-bcdadd100.png)

### What the question is asking

Chain 100 one-digit BCD adders to add two 100-digit decimal numbers with carry propagation.

### Saved Verilog solution

```verilog
module top_module(
    input [399:0] a, b,
    input cin,
    output cout,
    output [399:0] sum );

endmodule
```

---

<a id="problem-047"></a>
## 047 — More logic gates

[Problem note](problems/Day%2003/047-gates.md) · [Verilog file](solutions/Day%2003/047-gates.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/gates)

![More logic gates question and submitted solution](images/Day%2003/047-gates.png)

### What the question is asking

Implement several basic gates at once, including bitwise outputs and their logical complements.

### Saved Verilog solution

```verilog
module top_module(
    input a, b,
    output out_and,
    output out_or,
    output out_xor,
    output out_nand,
    output out_nor,
    output out_xnor,
    output out_anotb
);
    assign out_and=a&b;
    assign out_or = a|b;
    assign out_xor =a^b;
    assign out_nand = ~(a&b);
    assign out_nor = ~(a|b);
    assign out_xnor= ~(a^b);
    assign out_anotb = a & ~(b);
endmodule
```

---

<a id="problem-048"></a>
## 048 — 7420 chip

[Problem note](problems/Day%2003/048-7420.md) · [Verilog file](solutions/Day%2003/048-7420.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/7420)

![7420 chip question and submitted solution](images/Day%2003/048-7420.png)

### What the question is asking

Model a 7420 chip containing two independent four-input NAND gates.

### Saved Verilog solution

```verilog
module top_module (
    input p1a, p1b, p1c, p1d,
    output p1y,
    input p2a, p2b, p2c, p2d,
    output p2y );


endmodule
```

---

<a id="problem-049"></a>
## 049 — Truth tables

[Problem note](problems/Day%2003/049-truthtable1.md) · [Verilog file](solutions/Day%2003/049-truthtable1.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/truthtable1)

![Truth tables question and submitted solution](images/Day%2003/049-truthtable1.png)

### What the question is asking

Convert the supplied truth table into combinational Verilog that produces the specified output for every input combination.

### Saved Verilog solution

```verilog
module top_module(
    input x3,
    input x2,
    input x1,  // three inputs
    output f   // one output
);

endmodule
```

---

<a id="problem-050"></a>
## 050 — Two-bit equality

[Problem note](problems/Day%2003/050-mt2015_eq2.md) · [Verilog file](solutions/Day%2003/050-mt2015_eq2.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/mt2015_eq2)

![Two-bit equality question and submitted solution](images/Day%2003/050-mt2015_eq2.png)

### What the question is asking

Compare two 2-bit inputs and assert the output only when both vectors are equal.

### Saved Verilog solution

```verilog
module top_module ( input [1:0] A, input [1:0] B, output z );

endmodule
```

---

<a id="problem-051"></a>
## 051 — Simple circuit A

[Problem note](problems/Day%2003/051-mt2015_q4a.md) · [Verilog file](solutions/Day%2003/051-mt2015_q4a.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/mt2015_q4a)

![Simple circuit A question and submitted solution](images/Day%2003/051-mt2015_q4a.png)

### What the question is asking

Implement the first small combinational circuit exactly as shown in the diagram.

### Saved Verilog solution

```verilog
module top_module (input x, input y, output z);
wire w1;
    xor g1(w1,x,y);
    and g2(z,w1,x);
endmodule
```

---

<a id="problem-052"></a>
## 052 — Simple circuit B

[Problem note](problems/Day%2003/052-mt2015_q4b.md) · [Verilog file](solutions/Day%2003/052-mt2015_q4b.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/mt2015_q4b)

![Simple circuit B question and submitted solution](images/Day%2003/052-mt2015_q4b.png)

### What the question is asking

Implement the second small combinational circuit exactly as shown in the diagram.

### Saved Verilog solution

```verilog
module top_module ( input x, input y, output z );
    xnor g1(z,x,y);
endmodule
```

---

<a id="problem-053"></a>
## 053 — Combine circuits A and B

[Problem note](problems/Day%2003/053-mt2015_q4.md) · [Verilog file](solutions/Day%2003/053-mt2015_q4.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/mt2015_q4)

![Combine circuits A and B question and submitted solution](images/Day%2003/053-mt2015_q4.png)

### What the question is asking

Instantiate or combine circuits A and B so they operate together with the requested top-level connections.

### Saved Verilog solution

```verilog
module top_module (input x, input y, output z);

    wire za1, zb1, za2, zb2;
    wire or_out, and_out;

    A IA1 (
        .x(x),
        .y(y),
        .z(za1)
    );

    B IB1 (
        .x(x),
        .y(y),
        .z(zb1)
    );

    A IA2 (
        .x(x),
        .y(y),
        .z(za2)
    );

    B IB2 (
        .x(x),
        .y(y),
        .z(zb2)
    );

    or  g1(or_out,  za1, zb1);
    and g2(and_out, za2, zb2);
    xor g3(z,       or_out, and_out);

endmodule


module A (input x, input y, output z);
    assign z = (x ^ y) & x;
endmodule


module B (input x, input y, output z);
    assign z = ~(x ^ y);
endmodule
```

---

<a id="problem-054"></a>
## 054 — Ring or vibrate?

[Problem note](problems/Day%2003/054-ringer.md) · [Verilog file](solutions/Day%2003/054-ringer.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/ringer)

![Ring or vibrate? question and submitted solution](images/Day%2003/054-ringer.png)

### What the question is asking

Choose whether a phone should ring or vibrate from the incoming-call and silent-mode control signals.

### Saved Verilog solution

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

---

<a id="problem-055"></a>
## 055 — Thermostat

[Problem note](problems/Day%2003/055-thermostat.md) · [Verilog file](solutions/Day%2003/055-thermostat.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/thermostat)

![Thermostat question and submitted solution](images/Day%2003/055-thermostat.png)

### What the question is asking

Implement the thermostat's heater, air-conditioner, and fan control rules from the temperature and mode inputs.

### Saved Verilog solution

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

---

<a id="problem-056"></a>
## 056 — 3-bit population count

[Problem note](problems/Day%2003/056-popcount3.md) · [Verilog file](solutions/Day%2003/056-popcount3.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/popcount3)

![3-bit population count question and submitted solution](images/Day%2003/056-popcount3.png)

### What the question is asking

Count the number of asserted bits in a 3-bit input and return that count as a binary value.

### Saved Verilog solution

```verilog
module top_module(
    input [2:0] in,
    output reg [1:0] out
);
    integer i;
    always @(*)begin
        out = 2'b00;
        for(i=0;i<3;i=i+1)begin
            out=out +in[i];
        end
    end
endmodule
```

---

<a id="problem-057"></a>
## 057 — Gates and vectors

[Problem note](problems/Day%2003/057-gatesv.md) · [Verilog file](solutions/Day%2003/057-gatesv.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/gatesv)

![Gates and vectors question and submitted solution](images/Day%2003/057-gatesv.png)

### What the question is asking

For two vectors, compute bitwise gate results and also indicate whether the vectors differ at any or every position.

### Saved Verilog solution

```verilog
module top_module(
    input [3:0] in,
    output [2:0] out_both,
    output [3:1] out_any,
    output [3:0] out_different
);
    assign out_both= in[3:1] & in[2:0]; // out_both[2] should indicate if in[2] and in[3] are both 1
    assign out_any= in[3:1] | in[2:0];//out_any[2] should indicate if either in[2] or in[1] are 1
    assign out_different= in^ {in[0],in[3:1]};//out_different[2] should indicate if in[2] is different from in[3] , msb and lsb are neighbours
endmodule
```

---

<a id="problem-058"></a>
## 058 — Even longer vectors

[Problem note](problems/Day%2003/058-gatesv100.md) · [Verilog file](solutions/Day%2003/058-gatesv100.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/gatesv100)

![Even longer vectors question and submitted solution](images/Day%2003/058-gatesv100.png)

### What the question is asking

Extend the vector-gate comparison to 100-bit inputs, including per-bit outputs and wide reduction results.

### Saved Verilog solution

```verilog
module top_module(
    input [99:0] in,
    output [98:0] out_both,
    output [99:1] out_any,
    output [99:0] out_different );

endmodule
```

---

<a id="problem-059"></a>
## 059 — 2-to-1 multiplexer

[Problem note](problems/Day%2003/059-mux2to1.md) · [Verilog file](solutions/Day%2003/059-mux2to1.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/mux2to1)

![2-to-1 multiplexer question and submitted solution](images/Day%2003/059-mux2to1.png)

### What the question is asking

Implement a one-bit 2-to-1 multiplexer that selects one input according to the select signal.

### Saved Verilog solution

```verilog
module top_module(
    input a, b, sel,
    output out );

endmodule
```

---

<a id="problem-060"></a>
## 060 — 2-to-1 bus multiplexer

[Problem note](problems/Day%2003/060-mux2to1v.md) · [Verilog file](solutions/Day%2003/060-mux2to1v.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/mux2to1v)

![2-to-1 bus multiplexer question and submitted solution](images/Day%2003/060-mux2to1v.png)

### What the question is asking

Implement a 2-to-1 multiplexer that selects an entire vector rather than a single bit.

### Saved Verilog solution

```verilog
module top_module(
    input [99:0] a, b,
    input sel,
    output [99:0] out );

endmodule
```

---

<a id="problem-061"></a>
## 061 — 9-to-1 multiplexer

[Problem note](problems/Day%2003/061-mux9to1v.md) · [Verilog file](solutions/Day%2003/061-mux9to1v.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/mux9to1v)

![9-to-1 multiplexer question and submitted solution](images/Day%2003/061-mux9to1v.png)

### What the question is asking

Select one of nine 16-bit inputs; produce the required default value when the selector is outside the valid range.

### Saved Verilog solution

```verilog
module top_module(
    input [15:0] a, b, c, d, e, f, g, h, i,
    input [3:0] sel,
    output [15:0] out );

endmodule
```

---

<a id="problem-062"></a>
## 062 — 256-to-1 multiplexer

[Problem note](problems/Day%2003/062-mux256to1.md) · [Verilog file](solutions/Day%2003/062-mux256to1.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/mux256to1)

![256-to-1 multiplexer question and submitted solution](images/Day%2003/062-mux256to1.png)

### What the question is asking

Select one bit from a 256-bit input vector using an 8-bit selector as the index.

### Saved Verilog solution

```verilog
module top_module(
    input [255:0] in,
    input [7:0] sel,
    output out );

endmodule
```

---

<a id="problem-063"></a>
## 063 — 256-to-1 4-bit multiplexer

[Problem note](problems/Day%2003/063-mux256to1v.md) · [Verilog file](solutions/Day%2003/063-mux256to1v.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/mux256to1v)

![256-to-1 4-bit multiplexer question and submitted solution](images/Day%2003/063-mux256to1v.png)

### What the question is asking

Select one 4-bit word from 256 packed words by calculating the correct vector slice from the selector.

### Saved Verilog solution

```verilog
module top_module(
    input [1023:0] in,
    input [7:0] sel,
    output [3:0] out
);
    assign out = in[sel*4+:4];
endmodule
```

---

<a id="problem-064"></a>
## 064 — Half adder

[Problem note](problems/Day%2003/064-hadd.md) · [Verilog file](solutions/Day%2003/064-hadd.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/hadd)

![Half adder question and submitted solution](images/Day%2003/064-hadd.png)

### What the question is asking

Implement a half adder that produces a one-bit sum and carry from two input bits.

### Saved Verilog solution

```verilog
module top_module(
    input a, b,
    output cout, sum
);
assign cout = a &b;
    assign sum = a^b;
endmodule
```

---

<a id="problem-066"></a>
## 066 — 3-bit binary adder

[Problem note](problems/Day%2003/066-adder3.md) · [Verilog file](solutions/Day%2003/066-adder3.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/adder3)

![3-bit binary adder question and submitted solution](images/Day%2003/066-adder3.png)

### What the question is asking

Chain three full adders to add two 3-bit numbers and expose the intermediate carry signals.

### Saved Verilog solution

```verilog
module top_module(
    input [2:0] a, b,
    input cin,
    output [2:0] cout,
    output [2:0] sum
);
//4 bit addition
    wire [3:0] carry;
    assign carry[0]=cin;

    genvar i;
    generate
        for(i=0;i<3;i=i+1)begin : generating
            fa fullAdders(
                .a(a[i]),
                .b(b[i]),
                .cin(carry[i]),
                .sum(sum[i]),
                .cout(carry[i+1])
            );
        end
    endgenerate
    assign cout=carry[3:1];
endmodule
module fa(
    input wire a,b,cin,
    output wire cout, sum
);
    assign sum= a^b^cin;
    assign cout = a&b | b&cin | a &cin ;

endmodule
```

---

<a id="problem-067"></a>
## 067 — Adder

[Problem note](problems/Day%2003/067-exams__m2014_q4j.md) · [Verilog file](solutions/Day%2003/067-exams__m2014_q4j.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/m2014_q4j)

![Adder question and submitted solution](images/Day%2003/067-exams__m2014_q4j.png)

### What the question is asking

Implement the adder circuit shown in the exam diagram with the requested sum and carry behaviour.

### Saved Verilog solution

```verilog
module top_module (
    input [3:0] x,
    input [3:0] y,
    output [4:0] sum
);
//4 bit addition
    wire [4:0] carry;
    assign carry[0]=0;

    genvar i;
    generate
        for(i=0;i<4;i=i+1)begin : generating
            fa fullAdders(
                .a(x[i]),
                .b(y[i]),
                .cin(carry[i]),
                .sum(sum[i]),
                .cout(carry[i+1])
            );
        end
    endgenerate
    assign sum[4]= carry[4];
endmodule
module fa(
    input wire a,b,cin,
    output wire cout, sum
);
    assign sum= a^b^cin;
    assign cout = a&b | b&cin | a &cin ;

endmodule
```

---

<a id="problem-068"></a>
## 068 — Signed addition overflow

[Problem note](problems/Day%2003/068-exams__ece241_2014_q1c.md) · [Verilog file](solutions/Day%2003/068-exams__ece241_2014_q1c.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/ece241_2014_q1c)

![Signed addition overflow question and submitted solution](images/Day%2003/068-exams__ece241_2014_q1c.png)

### What the question is asking

Add two signed values and assert overflow when the mathematical result cannot fit in the signed output width.

### Saved Verilog solution

```verilog
module top_module (
    input [7:0] a,
    input [7:0] b,
    output [7:0] s,
    output overflow
); //

    assign s= a+b;
    assign overflow = (a[7]==b[7]) && (a[7] != s[7]);

endmodule
```

---

<a id="problem-069"></a>
## 069 — 100-bit binary adder

[Problem note](problems/Day%2003/069-adder100.md) · [Verilog file](solutions/Day%2003/069-adder100.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/adder100)

![100-bit binary adder question and submitted solution](images/Day%2003/069-adder100.png)

### What the question is asking

Implement a 100-bit combinational adder and return the final carry-out together with the sum.

### Saved Verilog solution

```verilog
module top_module(
    input [99:0] a, b,
    input cin,
    output cout,
    output [99:0] sum
);
genvar i ;
    wire [100:0] carry ;
    assign carry[0]=cin;
    generate
        for(i=0;i<100;i++)begin : calling
            fa fa1(
                .a(a[i]),
                .b(b[i]),
                .cin(carry[i]),
                .cout(carry[i+1]),
                .sum(sum[i])
            );
        end
    endgenerate
    assign cout = carry [100];
endmodule
module fa(
    input wire a,b,cin,
    output wire cout,sum
);
    assign sum = a^b^cin ;
    assign cout = a&b | b&cin| a&cin;
endmodule
```

---

<a id="problem-070"></a>
## 070 — 4-digit BCD adder

[Problem note](problems/Day%2003/070-bcdadd4.md) · [Verilog file](solutions/Day%2003/070-bcdadd4.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/bcdadd4)

![4-digit BCD adder question and submitted solution](images/Day%2003/070-bcdadd4.png)

### What the question is asking

Chain four BCD full adders to add two four-digit decimal values and propagate decimal carry between digits.

### Saved Verilog solution

```verilog
module top_module (
    input [15:0] a, b,
    input cin,
    output cout,
    output [15:0] sum
);
    wire [4:0] carry;
    assign carry[0]= cin;
genvar i ;
    generate
        for(i=0;i<4;i=i+1)begin : callingTheAdder
            bcd_fadd call(
                .a(a[4*i+:4]),
                .b(b[4*i+:4]),
                .cin(carry[i]),
                .cout(carry[i+1]),
                .sum(sum[i*4+:4])
            );
        end
    endgenerate
    assign cout = carry [4];
endmodule
```

---

<a id="problem-071"></a>
## 071 — 3-variable

[Problem note](problems/Day%2003/071-kmap1.md) · [Verilog file](solutions/Day%2003/071-kmap1.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/kmap1)

![3-variable question and submitted solution](images/Day%2003/071-kmap1.png)

### What the question is asking

Derive and implement the simplified logic function represented by the supplied 3-variable Karnaugh map.

### Saved Verilog solution

```verilog
module top_module(
    input a,
    input b,
    input c,
    output out  );
assign out = a  | b | c;
endmodule
```

---

<a id="problem-072"></a>
## 072 — 4-variable

[Problem note](problems/Day%2003/072-kmap2.md) · [Verilog file](solutions/Day%2003/072-kmap2.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/kmap2)

![4-variable question and submitted solution](images/Day%2003/072-kmap2.png)

### What the question is asking

Derive a minimal combinational expression from the supplied 4-variable Karnaugh map.

### Saved Verilog solution

```verilog
module top_module(
    input a,
    input b,
    input c,
    input d,
    output out
);
    assign out = c & d & (a | b ) | ~b & ~c | ~a & ~ d;
endmodule
```

---

<a id="problem-073"></a>
## 073 — 4-variable

[Problem note](problems/Day%2003/073-kmap3.md) · [Verilog file](solutions/Day%2003/073-kmap3.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/kmap3)

![4-variable question and submitted solution](images/Day%2003/073-kmap3.png)

### What the question is asking

Implement the 4-variable Karnaugh-map function while using the indicated don't-care cells for simplification.

### Saved Verilog solution

```verilog
module top_module(
    input a,
    input b,
    input c,
    input d,
    output out  );

endmodule
```

---

<a id="problem-074"></a>
## 074 — 4-variable

[Problem note](problems/Day%2003/074-kmap4.md) · [Verilog file](solutions/Day%2003/074-kmap4.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/kmap4)

![4-variable question and submitted solution](images/Day%2003/074-kmap4.png)

### What the question is asking

Translate the supplied 4-variable Karnaugh map into a correct simplified Verilog expression.

### Saved Verilog solution

```verilog
module top_module(
    input a,
    input b,
    input c,
    input d,
    output out
);
wire w1,w2,w3,w4,w5;
    not g1(w1,c); //c bar
    not g2(w2,d);
    assign out= w1 & w2 & (a ^b) | w1 & d & ~(a ^ b ) | c & d & (a ^b)| c & w2 & ~(a ^ b);
endmodule
```

---

<a id="problem-075"></a>
## 075 — Minimum SOP and POS

[Problem note](problems/Day%2003/075-exams__ece241_2013_q2.md) · [Verilog file](solutions/Day%2003/075-exams__ece241_2013_q2.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/ece241_2013_q2)

![Minimum SOP and POS question and submitted solution](images/Day%2003/075-exams__ece241_2013_q2.png)

### What the question is asking

Implement both the minimum sum-of-products and minimum product-of-sums forms for the given logic function.

### Saved Verilog solution

```verilog
module top_module (
    input a,
    input b,
    input c,
    input d,
    output out_sop,
    output out_pos
);
    assign out_sop = ~a & ~b & c & (d | ~d) | (a | ~a ) & (b | ~b ) & c&d;
 assign out_pos = c & (b | ~a) & (d | ~b);

endmodule
```

---

<a id="problem-076"></a>
## 076 — Karnaugh map

[Problem note](problems/Day%2003/076-exams__m2014_q3.md) · [Verilog file](solutions/Day%2003/076-exams__m2014_q3.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/m2014_q3)

![Karnaugh map question and submitted solution](images/Day%2003/076-exams__m2014_q3.png)

### What the question is asking

Simplify the exam Karnaugh map and implement the resulting combinational output.

### Saved Verilog solution

```verilog
module top_module (
    input [4:1] x,
    output f
);
    assign f= x[4] & x[2] | x[3] & ~x[1];
endmodule
```

---

<a id="problem-077"></a>
## 077 — Karnaugh map

[Problem note](problems/Day%2003/077-exams__2012_q1g.md) · [Verilog file](solutions/Day%2003/077-exams__2012_q1g.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/2012_q1g)

![Karnaugh map question and submitted solution](images/Day%2003/077-exams__2012_q1g.png)

### What the question is asking

Convert the supplied Karnaugh map, including any don't-care conditions, into simplified logic.

### Saved Verilog solution

```verilog
module top_module (
    input [4:1] x,
    output f
);
    assign f = ~x[1] & x[3] | ~x[2] & ~x[4] | x[3] & x[4] & x[2];
endmodule
```

---

<a id="problem-078"></a>
## 078 — K-map implemented with a multiplexer

[Problem note](problems/Day%2003/078-exams__ece241_2014_q3.md) · [Verilog file](solutions/Day%2003/078-exams__ece241_2014_q3.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/ece241_2014_q3)

![K-map implemented with a multiplexer question and submitted solution](images/Day%2003/078-exams__ece241_2014_q3.png)

### What the question is asking

Implement the Karnaugh-map function using the specified multiplexer structure and input assignments.

### Saved Verilog solution

```verilog
module top_module (
    input c,
    input d,
    output [3:0] mux_in
);

endmodule
```

---

<a id="problem-079"></a>
## 079 — D flip-flop

[Problem note](problems/Day%2003/079-dff.md) · [Verilog file](solutions/Day%2003/079-dff.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/dff)

![D flip-flop question and submitted solution](images/Day%2003/079-dff.png)

### What the question is asking

Create a positive-edge-triggered D flip-flop that stores the input value on each rising clock edge.

### Saved Verilog solution

```verilog
module top_module (
    input clk,    // Clocks are used in sequential circuits
    input d,
    output reg q );//

    // Use a clocked always block
    //   copy d to q at every positive edge of clk
    //   Clocked always blocks should use non-blocking assignments
    always @(posedge clk)begin
        q<=d;
    end
endmodule
```

---

<a id="problem-080"></a>
## 080 — D flip-flops

[Problem note](problems/Day%2003/080-dff8.md) · [Verilog file](solutions/Day%2003/080-dff8.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/dff8)

![D flip-flops question and submitted solution](images/Day%2003/080-dff8.png)

### What the question is asking

Create eight D flip-flops in parallel so an entire 8-bit vector is registered on the rising clock edge.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input [7:0] d,
    output reg [7:0] q
);
    always @(posedge clk)begin
        q<=d;
    end
endmodule
```

---

<a id="problem-081"></a>
## 081 — DFF with reset

[Problem note](problems/Day%2003/081-dff8r.md) · [Verilog file](solutions/Day%2003/081-dff8r.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/dff8r)

![DFF with reset question and submitted solution](images/Day%2003/081-dff8r.png)

### What the question is asking

Add a synchronous reset to an 8-bit register so reset is sampled on the active clock edge.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input reset,            // Synchronous reset
    input [7:0] d,
    output [7:0] q
);

endmodule
```

---

<a id="problem-082"></a>
## 082 — DFF with reset value

[Problem note](problems/Day%2003/082-dff8p.md) · [Verilog file](solutions/Day%2003/082-dff8p.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/dff8p)

![DFF with reset value question and submitted solution](images/Day%2003/082-dff8p.png)

### What the question is asking

Create an 8-bit register whose synchronous reset loads the specified non-zero reset value.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input reset,
    input [7:0] d,
    output reg [7:0] q
);
    always @(negedge clk )begin
        if(reset)
            q<=8'h34;
        else
            q<=d;
    end
endmodule
```

---

<a id="problem-083"></a>
## 083 — DFF with asynchronous reset

[Problem note](problems/Day%2003/083-dff8ar.md) · [Verilog file](solutions/Day%2003/083-dff8ar.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/dff8ar)

![DFF with asynchronous reset question and submitted solution](images/Day%2003/083-dff8ar.png)

### What the question is asking

Create an 8-bit register with asynchronous reset, allowing reset to change the output without waiting for a clock edge.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input areset,   // active high asynchronous reset
    input [7:0] d,
    output reg [7:0] q
);
    always @(posedge clk or posedge areset)begin
        if(areset)
            q<=8'd0;
        else
            q<=d;
    end
endmodule
```

---

<a id="problem-084"></a>
## 084 — DFF with byte enable

[Problem note](problems/Day%2003/084-dff16e.md) · [Verilog file](solutions/Day%2003/084-dff16e.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/dff16e)

![DFF with byte enable question and submitted solution](images/Day%2003/084-dff16e.png)

### What the question is asking

Build a 16-bit register with synchronous reset and independent byte-enable controls for its upper and lower bytes.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input resetn,
    input [1:0] byteena,
    input [15:0] d,
    output reg [15:0] q
);
    always @(posedge clk)begin
        if(!resetn)begin
            q<=16'd0;
        end
        else begin
            if(byteena[1])
                q[15:8]<=d[15:8];
            if(byteena[0])
                q[7:0]<=d[7:0];

        end

    end
endmodule
```

---

<a id="problem-085"></a>
## 085 — D Latch

[Problem note](problems/Day%2003/085-exams__m2014_q4a.md) · [Verilog file](solutions/Day%2003/085-exams__m2014_q4a.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/m2014_q4a)

![D Latch question and submitted solution](images/Day%2003/085-exams__m2014_q4a.png)

### What the question is asking

Model the level-sensitive D latch shown in the exam circuit.

### Saved Verilog solution

```verilog
module top_module (
    input d,
    input ena,
    output reg q
);
    always @(*)begin
        if(ena)
            q<=d;
    end
endmodule
```

---

<a id="problem-086"></a>
## 086 — DFF

[Problem note](problems/Day%2003/086-exams__m2014_q4b.md) · [Verilog file](solutions/Day%2003/086-exams__m2014_q4b.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/m2014_q4b)

![DFF question and submitted solution](images/Day%2003/086-exams__m2014_q4b.png)

### What the question is asking

Model the positive-edge-triggered D flip-flop shown in the exam circuit.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input d,
    input ar,   // asynchronous reset
    output reg q
);
    always @(posedge clk or posedge ar)begin
        if(ar)begin
            q<=0;
        end else begin
            q<=d;
        end
    end
endmodule
```

---

<a id="problem-087"></a>
## 087 — DFF

[Problem note](problems/Day%2003/087-exams__m2014_q4c.md) · [Verilog file](solutions/Day%2003/087-exams__m2014_q4c.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/m2014_q4c)

![DFF question and submitted solution](images/Day%2003/087-exams__m2014_q4c.png)

### What the question is asking

Model the specified D flip-flop behaviour and its control connection from the diagram.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input d,
    input r,   // synchronous reset
    output reg q
);
    always @(posedge clk)begin
        if(r)
            q<=0;
        else
            q<=d;
    end
endmodule
```

---

<a id="problem-088"></a>
## 088 — DFF+gate

[Problem note](problems/Day%2003/088-exams__m2014_q4d.md) · [Verilog file](solutions/Day%2003/088-exams__m2014_q4d.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/m2014_q4d)

![DFF+gate question and submitted solution](images/Day%2003/088-exams__m2014_q4d.png)

### What the question is asking

Implement the shown combination of a D flip-flop and combinational gate.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input in,
    output reg out
);

    always @(posedge clk)begin
        out<=in ^ out;
    end
endmodule
```
