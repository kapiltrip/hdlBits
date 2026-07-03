# Day 01 — 2026-06-23

Completed problems: **12**

Each screenshot is embedded at the full width of the GitHub page. Select an image to open its original-resolution file.

## Index

| # | Time | Problem | Section | Problem note | Solution | Source |
|---:|---|---:|---|---|---|---|
| 1 | 5:47:07 PM | [001](#problem-001) | Basics | [Simple wire](problems/Day%2001/001-wire.md) | [Code](solutions/Day%2001/001-wire.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/wire) |
| 2 | 5:50:30 PM | [002](#problem-002) | Basics | [Four wires](problems/Day%2001/002-wire4.md) | [Code](solutions/Day%2001/002-wire4.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/wire4) |
| 3 | 5:52:19 PM | [003](#problem-003) | Basics | [Inverter](problems/Day%2001/003-notgate.md) | [Code](solutions/Day%2001/003-notgate.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/notgate) |
| 4 | 6:15:38 PM | [008](#problem-008) | Basics | [7458 chip](problems/Day%2001/008-7458.md) | [Code](solutions/Day%2001/008-7458.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/7458) |
| 5 | 6:24:20 PM | [009](#problem-009) | Vectors | [Vectors](problems/Day%2001/009-vector0.md) | [Code](solutions/Day%2001/009-vector0.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/vector0) |
| 6 | 9:45:09 PM | [010](#problem-010) | Vectors | [Vectors in more detail](problems/Day%2001/010-vector1.md) | [Code](solutions/Day%2001/010-vector1.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/vector1) |
| 7 | 9:56:38 PM | [011](#problem-011) | Vectors | [Vector part select](problems/Day%2001/011-vector2.md) | [Code](solutions/Day%2001/011-vector2.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/vector2) |
| 8 | 10:04:38 PM | [012](#problem-012) | Vectors | [Bitwise operators](problems/Day%2001/012-vectorgates.md) | [Code](solutions/Day%2001/012-vectorgates.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/vectorgates) |
| 9 | 10:24:24 PM | [013](#problem-013) | Vectors | [Four-input gates](problems/Day%2001/013-gates4.md) | [Code](solutions/Day%2001/013-gates4.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/gates4) |
| 10 | 10:56:44 PM | [014](#problem-014) | Vectors | [Vector concatenation operator](problems/Day%2001/014-vector3.md) | [Code](solutions/Day%2001/014-vector3.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/vector3) |
| 11 | 11:34:51 PM | [015](#problem-015) | Vectors | [Vector reversal 1](problems/Day%2001/015-vectorr.md) | [Code](solutions/Day%2001/015-vectorr.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/vectorr) |
| 12 | 11:49:31 PM | [016](#problem-016) | Vectors | [Replication operator](problems/Day%2001/016-vector4.md) | [Code](solutions/Day%2001/016-vector4.sv) | [HDLBits](https://hdlbits.01xz.net/wiki/vector4) |

---

<a id="problem-001"></a>
## 001 — Simple wire

[Problem note](problems/Day%2001/001-wire.md) · [Open screenshot at full resolution](images/Day%2001/001-wire.png) · [Verilog file](solutions/Day%2001/001-wire.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/wire)

<a href="images/Day%2001/001-wire.png"><img src="images/Day%2001/001-wire.png" alt="Simple wire question and submitted solution" width="100%"></a>

### What the question is asking

Connect the single input directly to the output so the module behaves exactly like a wire.

### Saved Verilog solution

```verilog
module top_module( input in, output out );

endmodule
```

---

<a id="problem-002"></a>
## 002 — Four wires

[Problem note](problems/Day%2001/002-wire4.md) · [Open screenshot at full resolution](images/Day%2001/002-wire4.png) · [Verilog file](solutions/Day%2001/002-wire4.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/wire4)

<a href="images/Day%2001/002-wire4.png"><img src="images/Day%2001/002-wire4.png" alt="Four wires question and submitted solution" width="100%"></a>

### What the question is asking

Create the requested one-to-one and fan-out wire connections between the named inputs and outputs.

### Saved Verilog solution

```verilog
module top_module(
    input a,b,c,
    output w,x,y,z );

endmodule
```

---

<a id="problem-003"></a>
## 003 — Inverter

[Problem note](problems/Day%2001/003-notgate.md) · [Open screenshot at full resolution](images/Day%2001/003-notgate.png) · [Verilog file](solutions/Day%2001/003-notgate.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/notgate)

<a href="images/Day%2001/003-notgate.png"><img src="images/Day%2001/003-notgate.png" alt="Inverter question and submitted solution" width="100%"></a>

### What the question is asking

Drive the output with the logical inverse of the input, implementing a NOT gate.

### Saved Verilog solution

```verilog
module top_module( input in, output out );
    not g1(out , in );
endmodule
```

---

<a id="problem-008"></a>
## 008 — 7458 chip

[Problem note](problems/Day%2001/008-7458.md) · [Open screenshot at full resolution](images/Day%2001/008-7458.png) · [Verilog file](solutions/Day%2001/008-7458.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/7458)

<a href="images/Day%2001/008-7458.png"><img src="images/Day%2001/008-7458.png" alt="7458 chip question and submitted solution" width="100%"></a>

### What the question is asking

Recreate the 7458-style sum-of-products circuit by combining several AND terms into two OR outputs.

### Saved Verilog solution

```verilog
module top_module (
    input p1a, p1b, p1c, p1d, p1e, p1f,
    output p1y,
    input p2a, p2b, p2c, p2d,
    output p2y );


endmodule
```

---

<a id="problem-009"></a>
## 009 — Vectors

[Problem note](problems/Day%2001/009-vector0.md) · [Open screenshot at full resolution](images/Day%2001/009-vector0.png) · [Verilog file](solutions/Day%2001/009-vector0.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/vector0)

<a href="images/Day%2001/009-vector0.png"><img src="images/Day%2001/009-vector0.png" alt="Vectors question and submitted solution" width="100%"></a>

### What the question is asking

Declare vector ports with the required widths and connect the complete input bus to the output bus.

### Saved Verilog solution

```verilog
module top_module (
    input wire [2:0] vec,
    output wire [2:0] outv,
    output wire o2,
    output wire o1,
    output wire o0
); // Module body starts after module declaration
    assign outv = vec;
    assign o2=vec[2];
    assign o1=vec[1];
    assign o0=vec[0];

endmodule
```

---

<a id="problem-010"></a>
## 010 — Vectors in more detail

[Problem note](problems/Day%2001/010-vector1.md) · [Open screenshot at full resolution](images/Day%2001/010-vector1.png) · [Verilog file](solutions/Day%2001/010-vector1.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/vector1)

<a href="images/Day%2001/010-vector1.png"><img src="images/Day%2001/010-vector1.png" alt="Vectors in more detail question and submitted solution" width="100%"></a>

### What the question is asking

Practice vector declarations, bit ordering, and selecting individual bits from buses with different index directions.

### Saved Verilog solution

```verilog
`default_nettype none     // Disable implicit nets. Reduces some types of bugs.
module top_module(
    input wire [15:0] in,
    output wire [7:0] out_hi,
    output wire [7:0] out_lo
);


        assign out_hi=  in[15:8];
        assign out_lo =  in[7:0];

endmodule
```

---

<a id="problem-011"></a>
## 011 — Vector part select

[Problem note](problems/Day%2001/011-vector2.md) · [Open screenshot at full resolution](images/Day%2001/011-vector2.png) · [Verilog file](solutions/Day%2001/011-vector2.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/vector2)

<a href="images/Day%2001/011-vector2.png"><img src="images/Day%2001/011-vector2.png" alt="Vector part select question and submitted solution" width="100%"></a>

### What the question is asking

Split a 16-bit input vector into its upper and lower 8-bit halves and route them to separate outputs.

### Saved Verilog solution

```verilog
module top_module(
    input [31:0] in,
    output [31:0] out );//

    // assign out[31:24] = ...;
    wire [7:0] a,b,c,d;
    assign a=in[31:24];//msb
    assign b=in[23:16];
    assign c=in[15:8];
    assign d=in[7:0];
   assign  out ={d,c,b,a};
endmodule
```

---

<a id="problem-012"></a>
## 012 — Bitwise operators

[Problem note](problems/Day%2001/012-vectorgates.md) · [Open screenshot at full resolution](images/Day%2001/012-vectorgates.png) · [Verilog file](solutions/Day%2001/012-vectorgates.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/vectorgates)

<a href="images/Day%2001/012-vectorgates.png"><img src="images/Day%2001/012-vectorgates.png" alt="Bitwise operators question and submitted solution" width="100%"></a>

### What the question is asking

Apply bitwise OR, logical OR, and bitwise inversion to vectors so their different behaviours are visible.

### Saved Verilog solution

```verilog
module top_module(
    input [2:0] a,
    input [2:0] b,
    output [2:0] out_or_bitwise,
    output out_or_logical,
    output [5:0] out_not
);
    assign out_or_bitwise= a |b;
    assign out_or_logical= a ||b;
    assign out_not= {~b,~a};
endmodule
```

---

<a id="problem-013"></a>
## 013 — Four-input gates

[Problem note](problems/Day%2001/013-gates4.md) · [Open screenshot at full resolution](images/Day%2001/013-gates4.png) · [Verilog file](solutions/Day%2001/013-gates4.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/gates4)

<a href="images/Day%2001/013-gates4.png"><img src="images/Day%2001/013-gates4.png" alt="Four-input gates question and submitted solution" width="100%"></a>

### What the question is asking

Use reduction operators to compute one-bit AND, OR, and XOR results across all four input bits.

### Saved Verilog solution

```verilog
module top_module(
    input [3:0] in,
    output out_and,
    output out_or,
    output out_xor
);
assign out_and = &in;
assign out_or = |in ;
assign out_xor  =^in;

endmodule
```

---

<a id="problem-014"></a>
## 014 — Vector concatenation operator

[Problem note](problems/Day%2001/014-vector3.md) · [Open screenshot at full resolution](images/Day%2001/014-vector3.png) · [Verilog file](solutions/Day%2001/014-vector3.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/vector3)

<a href="images/Day%2001/014-vector3.png"><img src="images/Day%2001/014-vector3.png" alt="Vector concatenation operator question and submitted solution" width="100%"></a>

### What the question is asking

Use concatenation to regroup the input vectors and assign the requested output vectors in the specified bit order.

### Saved Verilog solution

```verilog
module top_module (
    input [4:0] a, b, c, d, e, f,
    output [7:0] w, x, y, z );//

    // assign { ... } = { ... };

endmodule
```

---

<a id="problem-015"></a>
## 015 — Vector reversal 1

[Problem note](problems/Day%2001/015-vectorr.md) · [Open screenshot at full resolution](images/Day%2001/015-vectorr.png) · [Verilog file](solutions/Day%2001/015-vectorr.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/vectorr)

<a href="images/Day%2001/015-vectorr.png"><img src="images/Day%2001/015-vectorr.png" alt="Vector reversal 1 question and submitted solution" width="100%"></a>

### What the question is asking

Reverse the bit order of the input vector so the most-significant and least-significant positions swap.

### Saved Verilog solution

```verilog
module top_module(
    input [7:0] in,
    output [7:0] out
);
genvar i ;
    generate
        for(i=0;i<8;i=i+1) begin : revloop
            assign out[i]=in[7-i];
        end
    endgenerate
endmodule
```

---

<a id="problem-016"></a>
## 016 — Replication operator

[Problem note](problems/Day%2001/016-vector4.md) · [Open screenshot at full resolution](images/Day%2001/016-vector4.png) · [Verilog file](solutions/Day%2001/016-vector4.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/vector4)

<a href="images/Day%2001/016-vector4.png"><img src="images/Day%2001/016-vector4.png" alt="Replication operator question and submitted solution" width="100%"></a>

### What the question is asking

Use the replication operator to repeat a bit pattern and form the required wider output vector.

### Saved Verilog solution

```verilog
module top_module (
    input [7:0] in,
    output [31:0] out );//

    // assign out = { replicate-sign-bit , the-input };
    //msb of in will be in[7]
    assign out= {{24{in[7]}},in};
endmodule
```
