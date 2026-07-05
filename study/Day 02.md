# Day 02 — 2026-06-24

Completed problems: **34**

Each screenshot is embedded at the full width of the GitHub page. Select an image to open its original-resolution file.

## Index

| # | Time | Problem | Section | Problem note | Page contents | Source |
|---:|---|---:|---|---|---|---|
| 1 | 12:29:06 AM | [004](#problem-004) | Basics | [AND gate](problems/Day%2002/004-andgate.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/andgate) |
| 2 | 12:32:05 AM | [005](#problem-005) | Basics | [NOR gate](problems/Day%2002/005-norgate.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/norgate) |
| 3 | 12:33:10 AM | [006](#problem-006) | Basics | [XNOR gate](problems/Day%2002/006-xnorgate.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/xnorgate) |
| 4 | 12:35:55 AM | [007](#problem-007) | Basics | [Declaring wires](problems/Day%2002/007-wire_decl.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/wire_decl) |
| 5 | 12:26:24 AM | [017](#problem-017) | Vectors | [More replication](problems/Day%2002/017-vector5.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/vector5) |
| 6 | 1:24:31 PM | [018](#problem-018) | Modules: Hierarchy | [Modules](problems/Day%2002/018-module.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/module) |
| 7 | 1:28:26 PM | [019](#problem-019) | Modules: Hierarchy | [Connecting ports by position](problems/Day%2002/019-module_pos.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/module_pos) |
| 8 | 1:31:10 PM | [020](#problem-020) | Modules: Hierarchy | [Connecting ports by name](problems/Day%2002/020-module_name.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/module_name) |
| 9 | 1:37:32 PM | [021](#problem-021) | Modules: Hierarchy | [Three modules](problems/Day%2002/021-module_shift.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/module_shift) |
| 10 | 1:53:37 PM | [022](#problem-022) | Modules: Hierarchy | [Modules and vectors](problems/Day%2002/022-module_shift8.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/module_shift8) |
| 11 | 2:03:55 PM | [023](#problem-023) | Modules: Hierarchy | [Adder 1](problems/Day%2002/023-module_add.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/module_add) |
| 12 | 2:44:10 PM | [024](#problem-024) | Modules: Hierarchy | [Adder 2](problems/Day%2002/024-module_fadd.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/module_fadd) |
| 13 | 3:06:09 PM | [025](#problem-025) | Modules: Hierarchy | [Carry-select adder](problems/Day%2002/025-module_cseladd.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/module_cseladd) |
| 14 | 3:21:30 PM | [026](#problem-026) | Modules: Hierarchy | [Adder-subtractor](problems/Day%2002/026-module_addsub.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/module_addsub) |
| 15 | 3:23:21 PM | [027](#problem-027) | Procedures | [Always blocks (combinational)](problems/Day%2002/027-alwaysblock1.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/alwaysblock1) |
| 16 | 3:25:20 PM | [028](#problem-028) | Procedures | [Always blocks (clocked)](problems/Day%2002/028-alwaysblock2.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/alwaysblock2) |
| 17 | 3:30:54 PM | [029](#problem-029) | Procedures | [If statement](problems/Day%2002/029-always_if.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/always_if) |
| 18 | 4:18:47 PM | [030](#problem-030) | Procedures | [If statement latches](problems/Day%2002/030-always_if2.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/always_if2) |
| 19 | 4:22:44 PM | [031](#problem-031) | Procedures | [Case statement](problems/Day%2002/031-always_case.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/always_case) |
| 20 | 5:09:06 PM | [032](#problem-032) | Procedures | [Priority encoder](problems/Day%2002/032-always_case2.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/always_case2) |
| 21 | 5:44:37 PM | [033](#problem-033) | Procedures | [Priority encoder with casez](problems/Day%2002/033-always_casez.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/always_casez) |
| 22 | 6:00:14 PM | [034](#problem-034) | Procedures | [Avoiding latches](problems/Day%2002/034-always_nolatches.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/always_nolatches) |
| 23 | 6:09:15 PM | [035](#problem-035) | More Verilog Features | [Conditional ternary operator](problems/Day%2002/035-conditional.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/conditional) |
| 24 | 6:14:36 PM | [036](#problem-036) | More Verilog Features | [Reduction operators](problems/Day%2002/036-reduction.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/reduction) |
| 25 | 6:17:42 PM | [037](#problem-037) | More Verilog Features | [Reduction: Even wider gates](problems/Day%2002/037-gates100.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/gates100) |
| 26 | 6:22:35 PM | [038](#problem-038) | More Verilog Features | [Combinational for-loop: Vector reversal 2](problems/Day%2002/038-vector100r.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/vector100r) |
| 27 | 6:39:46 PM | [039](#problem-039) | More Verilog Features | [Combinational for-loop: 255-bit population count](problems/Day%2002/039-popcount255.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/popcount255) |
| 28 | 10:43:46 PM | [040](#problem-040) | More Verilog Features | [Generate for-loop: 100-bit binary adder 2](problems/Day%2002/040-adder100i.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/adder100i) |
| 29 | 11:31:58 PM | [042](#problem-042) | Combinational Logic | [Wire](problems/Day%2002/042-exams__m2014_q4h.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/exams/m2014_q4h) |
| 30 | 11:32:26 PM | [043](#problem-043) | Combinational Logic | [GND](problems/Day%2002/043-exams__m2014_q4i.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/exams/m2014_q4i) |
| 31 | 11:33:43 PM | [044](#problem-044) | Combinational Logic | [NOR](problems/Day%2002/044-exams__m2014_q4e.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/exams/m2014_q4e) |
| 32 | 11:33:25 PM | [045](#problem-045) | Combinational Logic | [Another gate](problems/Day%2002/045-exams__m2014_q4f.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/exams/m2014_q4f) |
| 33 | 11:58:42 PM | [046](#problem-046) | Combinational Logic | [Two gates](problems/Day%2002/046-exams__m2014_q4g.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/exams/m2014_q4g) |
| 34 | 10:21:26 PM | [065](#problem-065) | Combinational Logic | [Full adder](problems/Day%2002/065-fadd.md) | Screenshot + code rendered below | [HDLBits](https://hdlbits.01xz.net/wiki/fadd) |

---

<a id="problem-004"></a>
## 004 — AND gate

[Problem note](problems/Day%2002/004-andgate.md) · [Verilog file](solutions/Day%2002/004-andgate.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/andgate)

![AND gate question and submitted solution](images/Day%2002/004-andgate.png)

### What the question is asking

Produce an output that is high only when both input signals are high.

### Saved Verilog solution

```verilog
module top_module(
    input a,
    input b,
    output out
);
    and g1(out ,a , b);
endmodule
```

---

<a id="problem-005"></a>
## 005 — NOR gate

[Problem note](problems/Day%2002/005-norgate.md) · [Verilog file](solutions/Day%2002/005-norgate.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/norgate)

![NOR gate question and submitted solution](images/Day%2002/005-norgate.png)

### What the question is asking

Implement a NOR gate: OR the inputs and invert the result.

### Saved Verilog solution

```verilog
module top_module(
    input a,
    input b,
    output out );

endmodule
```

---

<a id="problem-006"></a>
## 006 — XNOR gate

[Problem note](problems/Day%2002/006-xnorgate.md) · [Verilog file](solutions/Day%2002/006-xnorgate.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/xnorgate)

![XNOR gate question and submitted solution](images/Day%2002/006-xnorgate.png)

### What the question is asking

Implement an XNOR gate whose output is high when the two inputs have equal values.

### Saved Verilog solution

```verilog
module top_module(
    input a,
    input b,
    output out
);
    assign out = ~(a ^b);

endmodule
```

---

<a id="problem-007"></a>
## 007 — Declaring wires

[Problem note](problems/Day%2002/007-wire_decl.md) · [Verilog file](solutions/Day%2002/007-wire_decl.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/wire_decl)

![Declaring wires question and submitted solution](images/Day%2002/007-wire_decl.png)

### What the question is asking

Declare intermediate wires and connect the supplied gates so the module matches the shown circuit diagram.

### Saved Verilog solution

```verilog
`default_nettype none
module top_module(
    input a,
    input b,
    input c,
    input d,
    output out,
    output out_n   );

endmodule
```

---

<a id="problem-017"></a>
## 017 — More replication

[Problem note](problems/Day%2002/017-vector5.md) · [Verilog file](solutions/Day%2002/017-vector5.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/vector5)

![More replication question and submitted solution](images/Day%2002/017-vector5.png)

### What the question is asking

Combine replication and concatenation to build widened vectors and compare them bit by bit.

### Saved Verilog solution

```verilog
module top_module (
    input a, b, c, d, e,
    output [24:0] out
);//
    wire [24:0] top = {5{a,b,c,d,e}};
    wire [24:0] bottom= {{5{a}},{5{b}},{5{c}}, {5{d}}, {5{e}}};
    assign out = ~(top ^ bottom);
endmodule
```

---

<a id="problem-018"></a>
## 018 — Modules

[Problem note](problems/Day%2002/018-module.md) · [Verilog file](solutions/Day%2002/018-module.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/module)

![Modules question and submitted solution](images/Day%2002/018-module.png)

### What the question is asking

Instantiate the provided submodule and connect its input and output ports to the top-level module.

### Saved Verilog solution

```verilog
module top_module ( input a, input b, output out );

endmodule
```

---

<a id="problem-019"></a>
## 019 — Connecting ports by position

[Problem note](problems/Day%2002/019-module_pos.md) · [Verilog file](solutions/Day%2002/019-module_pos.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/module_pos)

![Connecting ports by position question and submitted solution](images/Day%2002/019-module_pos.png)

### What the question is asking

Instantiate a module and connect its ports by position, keeping the connection order exactly correct.

### Saved Verilog solution

```verilog
module top_module (
    input a,
    input b,
    input c,
    input d,
    output out1,
    output out2
);
    mod_a instant(
        out1,out2,a,b,c,d
    );
endmodule
```

---

<a id="problem-020"></a>
## 020 — Connecting ports by name

[Problem note](problems/Day%2002/020-module_name.md) · [Verilog file](solutions/Day%2002/020-module_name.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/module_name)

![Connecting ports by name question and submitted solution](images/Day%2002/020-module_name.png)

### What the question is asking

Instantiate a module and connect its ports by name so each signal is matched explicitly.

### Saved Verilog solution

```verilog
module top_module (
    input a,
    input b,
    input c,
    input d,
    output out1,
    output out2
);

endmodule
```

---

<a id="problem-021"></a>
## 021 — Three modules

[Problem note](problems/Day%2002/021-module_shift.md) · [Verilog file](solutions/Day%2002/021-module_shift.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/module_shift)

![Three modules question and submitted solution](images/Day%2002/021-module_shift.png)

### What the question is asking

Chain three copies of the provided module so each stage feeds the next stage.

### Saved Verilog solution

```verilog
module top_module ( input clk, input d, output q );
    wire w1,w2,w3;
    my_dff d1(
        .clk(clk),
        .d(d),
        .q(w1)
    );
    my_dff d2(
        .clk(clk),
        .d(w1),
        .q(w2)
    );
    my_dff d3(
        .clk(clk),
        .d(w2),
        .q(q)
    );

endmodule
```

---

<a id="problem-022"></a>
## 022 — Modules and vectors

[Problem note](problems/Day%2002/022-module_shift8.md) · [Verilog file](solutions/Day%2002/022-module_shift8.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/module_shift8)

![Modules and vectors question and submitted solution](images/Day%2002/022-module_shift8.png)

### What the question is asking

Instantiate the supplied 8-bit module and connect vector signals correctly through the hierarchy.

### Saved Verilog solution

```verilog
module top_module (
    input clk,
    input [7:0] d,
    input [1:0] sel,
    output [7:0] q
);

endmodule
```

---

<a id="problem-023"></a>
## 023 — Adder 1

[Problem note](problems/Day%2002/023-module_add.md) · [Verilog file](solutions/Day%2002/023-module_add.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/module_add)

![Adder 1 question and submitted solution](images/Day%2002/023-module_add.png)

### What the question is asking

Instantiate two 16-bit adders to create a 32-bit adder, propagating the carry between the lower and upper halves.

### Saved Verilog solution

```verilog
module top_module(
    input [31:0] a,
    input [31:0] b,
    output [31:0] sum
);
    wire [15:0] a1Input=a[15:0];
    wire [15:0] b1Input=b[15:0];
    wire [15:0] a2Input=a[31:16];
    wire [15:0] b2Input=b[31:16];
    wire coutAdder1;
    wire coutAdder2;
    wire [15:0] sum1,sum2;
    add16 adder1(
        .a(a1Input),
        .b(b1Input),
        .cin(1'b0),
        .cout(coutAdder1),
        .sum(sum1)
    );
    add16 adder2(
        .a(a2Input),
        .b(b2Input),
        .cin(coutAdder1),
        .cout(coutAdder2),  // to ignore this
        .sum(sum2)
    );
    assign sum = {sum2,sum1};
endmodule
```

---

<a id="problem-024"></a>
## 024 — Adder 2

[Problem note](problems/Day%2002/024-module_fadd.md) · [Verilog file](solutions/Day%2002/024-module_fadd.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/module_fadd)

![Adder 2 question and submitted solution](images/Day%2002/024-module_fadd.png)

### What the question is asking

Build a ripple-carry adder from full-adder instances and expose the carry produced by every bit position.

### Saved Verilog solution

```verilog
module top_module (
    input [31:0] a,
    input [31:0] b,
    output [31:0] sum
);//

endmodule

module add1 ( input a, input b, input cin,   output sum, output cout );

// Full adder module here

endmodule
```

---

<a id="problem-025"></a>
## 025 — Carry-select adder

[Problem note](problems/Day%2002/025-module_cseladd.md) · [Verilog file](solutions/Day%2002/025-module_cseladd.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/module_cseladd)

![Carry-select adder question and submitted solution](images/Day%2002/025-module_cseladd.png)

### What the question is asking

Build a carry-select adder by computing both possible upper sums and selecting the correct one using the lower carry.

### Saved Verilog solution

```verilog
module top_module(
    input [31:0] a,
    input [31:0] b,
    output [31:0] sum
);

endmodule
```

---

<a id="problem-026"></a>
## 026 — Adder-subtractor

[Problem note](problems/Day%2002/026-module_addsub.md) · [Verilog file](solutions/Day%2002/026-module_addsub.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/module_addsub)

![Adder-subtractor question and submitted solution](images/Day%2002/026-module_addsub.png)

### What the question is asking

Create an adder-subtractor by conditionally inverting one operand and using the mode signal as the initial carry-in.

### Saved Verilog solution

```verilog
module top_module(
    input [31:0] a,
    input [31:0] b,
    input sub,
    output [31:0] sum
);
    wire [15:0] alower=a[15:0];
    wire [15:0] ahigher=a[31:16];
    //b will change , i.e blower and bupper will change, based, on sum ,
    //i can extend sub and then make them xor
    wire [15:0] blower = {16{sub}}^b[15:0];
    wire [15:0] bhigher = {16{sub}}^b[31:16];
    wire [15:0] sumlower,sumUpper;
    wire coutA , ignoreCoutB;
//instantiate twice, the module add16

    add16 a1(
        .a(alower),
        .b(blower),
        .cin(sub),
        .cout(coutA),
        .sum(sumlower)
    );
    add16 a2(
        .a(ahigher),
        .b(bhigher),
        .cin(coutA),
        .cout(ignoreCoutB),
        .sum(sumUpper)
    );
    assign sum = {sumUpper,sumlower};
endmodule
```

---

<a id="problem-027"></a>
## 027 — Always blocks (combinational)

[Problem note](problems/Day%2002/027-alwaysblock1.md) · [Verilog file](solutions/Day%2002/027-alwaysblock1.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/alwaysblock1)

![Always blocks (combinational) question and submitted solution](images/Day%2002/027-alwaysblock1.png)

### What the question is asking

Describe the same combinational logic with both a continuous assignment and an always block.

### Saved Verilog solution

```verilog
// synthesis verilog_input_version verilog_2001
module top_module(
    input a,
    input b,
    output wire out_assign,
    output reg out_alwaysblock
);
assign out_assign= a&b;
    always @(*)begin
        out_alwaysblock=a&b;
    end
endmodule
```

---

<a id="problem-028"></a>
## 028 — Always blocks (clocked)

[Problem note](problems/Day%2002/028-alwaysblock2.md) · [Verilog file](solutions/Day%2002/028-alwaysblock2.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/alwaysblock2)

![Always blocks (clocked) question and submitted solution](images/Day%2002/028-alwaysblock2.png)

### What the question is asking

Describe clocked storage in an always block so the output captures the input on each active clock edge.

### Saved Verilog solution

```verilog
// synthesis verilog_input_version verilog_2001
module top_module(
    input clk,
    input a,
    input b,
    output wire out_assign,
    output reg out_always_comb,
    output reg out_always_ff   );

endmodule
```

---

<a id="problem-029"></a>
## 029 — If statement

[Problem note](problems/Day%2002/029-always_if.md) · [Verilog file](solutions/Day%2002/029-always_if.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/always_if)

![If statement question and submitted solution](images/Day%2002/029-always_if.png)

### What the question is asking

Use an if/else statement in combinational logic to implement the requested multiplexer behaviour.

### Saved Verilog solution

```verilog
// synthesis verilog_input_version verilog_2001
module top_module(
    input a,
    input b,
    input sel_b1,
    input sel_b2,
    output wire out_assign,
    output reg out_always   );

endmodule
```

---

<a id="problem-030"></a>
## 030 — If statement latches

[Problem note](problems/Day%2002/030-always_if2.md) · [Verilog file](solutions/Day%2002/030-always_if2.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/always_if2)

![If statement latches question and submitted solution](images/Day%2002/030-always_if2.png)

### What the question is asking

Correct an incomplete combinational if statement by assigning every output on every path and thereby avoiding latches.

### Saved Verilog solution

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

---

<a id="problem-031"></a>
## 031 — Case statement

[Problem note](problems/Day%2002/031-always_case.md) · [Verilog file](solutions/Day%2002/031-always_case.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/always_case)

![Case statement question and submitted solution](images/Day%2002/031-always_case.png)

### What the question is asking

Use a case statement to select one of several input values according to the selector.

### Saved Verilog solution

```verilog
// synthesis verilog_input_version verilog_2001
module top_module (
    input [2:0] sel,
    input [3:0] data0,
    input [3:0] data1,
    input [3:0] data2,
    input [3:0] data3,
    input [3:0] data4,
    input [3:0] data5,
    output reg [3:0] out
);//

    always@(*) begin  // This is a combinational circuit
        case(sel)
            3'b000:out= data0;
            3'b001:out= data1;
            3'b010:out= data2;
            3'b011:out= data3;
            3'b100:out= data4;
            3'b101:out= data5;
            default :out= 4'b0000;
        endcase
    end

endmodule
```

---

<a id="problem-032"></a>
## 032 — Priority encoder

[Problem note](problems/Day%2002/032-always_case2.md) · [Verilog file](solutions/Day%2002/032-always_case2.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/always_case2)

![Priority encoder question and submitted solution](images/Day%2002/032-always_case2.png)

### What the question is asking

Implement a priority encoder whose output identifies the highest-priority asserted input bit.

### Saved Verilog solution

```verilog
// synthesis verilog_input_version verilog_2001
module top_module (
    input [3:0] in,
    output reg [1:0] pos  );

endmodule
```

---

<a id="problem-033"></a>
## 033 — Priority encoder with casez

[Problem note](problems/Day%2002/033-always_casez.md) · [Verilog file](solutions/Day%2002/033-always_casez.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/always_casez)

![Priority encoder with casez question and submitted solution](images/Day%2002/033-always_casez.png)

### What the question is asking

Implement the priority encoder compactly with casez patterns and don't-care bits.

### Saved Verilog solution

```verilog
// synthesis verilog_input_version verilog_2001
module top_module (
    input [7:0] in,
    output reg [2:0] pos
);
    always @(*)begin
        casez (in)
            8'b???????1:pos=3'b000;
            8'b??????10:pos=3'b001;
            8'b?????100:pos=3'b010;
            8'b????1000:pos=3'b011;
            8'b???10000:pos=3'b100;
            8'b??100000:pos=3'b101;
            8'b?1000000:pos=3'b110;
            8'b10000000:pos=3'b111;
            default : pos = 3'b000;

        endcase
    end
endmodule
```

---

<a id="problem-034"></a>
## 034 — Avoiding latches

[Problem note](problems/Day%2002/034-always_nolatches.md) · [Verilog file](solutions/Day%2002/034-always_nolatches.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/always_nolatches)

![Avoiding latches question and submitted solution](images/Day%2002/034-always_nolatches.png)

### What the question is asking

Complete the combinational case logic with safe defaults so no output retains an old value or infers a latch.

### Saved Verilog solution

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

---

<a id="problem-035"></a>
## 035 — Conditional ternary operator

[Problem note](problems/Day%2002/035-conditional.md) · [Verilog file](solutions/Day%2002/035-conditional.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/conditional)

![Conditional ternary operator question and submitted solution](images/Day%2002/035-conditional.png)

### What the question is asking

Use nested ternary operators to select the smallest unsigned value from several inputs.

### Saved Verilog solution

```verilog
module top_module (
    input [7:0] a, b, c, d,
    output [7:0] min);//

    // assign intermediate_result1 = compare? true: false;
    //to find, the mininum
    //compare a and b ,
    wire [7:0] minAB,minCD;
    assign minAB= (a<b)?a:b;
    assign minCD= (c<d)?c:d;
    assign min = (minAB<minCD)?minAB:minCD;
endmodule
```

---

<a id="problem-036"></a>
## 036 — Reduction operators

[Problem note](problems/Day%2002/036-reduction.md) · [Verilog file](solutions/Day%2002/036-reduction.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/reduction)

![Reduction operators question and submitted solution](images/Day%2002/036-reduction.png)

### What the question is asking

Compare bitwise and reduction operators by producing per-bit results and single-bit reductions from two vectors.

### Saved Verilog solution

```verilog
module top_module (
    input [7:0] in,
    output parity
);
assign parity= ^in;
//odd no of ones will be known by this
endmodule
```

---

<a id="problem-037"></a>
## 037 — Reduction: Even wider gates

[Problem note](problems/Day%2002/037-gates100.md) · [Verilog file](solutions/Day%2002/037-gates100.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/gates100)

![Reduction: Even wider gates question and submitted solution](images/Day%2002/037-gates100.png)

### What the question is asking

Apply reduction operators across a 100-bit vector to implement very wide AND, OR, and XOR gates.

### Saved Verilog solution

```verilog
module top_module(
    input [99:0] in,
    output out_and,
    output out_or,
    output out_xor
);
assign out_and = &in;
assign out_or = |in;
assign out_xor=^in;
endmodule
```

---

<a id="problem-038"></a>
## 038 — Combinational for-loop: Vector reversal 2

[Problem note](problems/Day%2002/038-vector100r.md) · [Verilog file](solutions/Day%2002/038-vector100r.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/vector100r)

![Combinational for-loop: Vector reversal 2 question and submitted solution](images/Day%2002/038-vector100r.png)

### What the question is asking

Use a combinational for loop to reverse all 100 bits of a vector.

### Saved Verilog solution

```verilog
module top_module(
    input [99:0] in,
    output [99:0] out
);
//to reverse the bit ordering
genvar i ;

    generate
        for(i=0;i<100;i=i+1)begin : reversingBits
               assign out[i]=in[99-i];
             end
    endgenerate
endmodule
```

---

<a id="problem-039"></a>
## 039 — Combinational for-loop: 255-bit population count

[Problem note](problems/Day%2002/039-popcount255.md) · [Verilog file](solutions/Day%2002/039-popcount255.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/popcount255)

![Combinational for-loop: 255-bit population count question and submitted solution](images/Day%2002/039-popcount255.png)

### What the question is asking

Count how many bits are high in a 255-bit input vector using combinational accumulation.

### Saved Verilog solution

```verilog
module top_module(
    input [254:0] in,
    output reg [7:0] out
);
//to count no of ones in the input vector
    integer i ;
    reg [7:0] count;
    always @(*)begin
        count=8'd0;
        for(i=0;i<255;i=i+1)begin
            count=count+ in[i];
        end
    end
    always @(*)begin
        out = count;

    end


endmodule
```

---

<a id="problem-040"></a>
## 040 — Generate for-loop: 100-bit binary adder 2

[Problem note](problems/Day%2002/040-adder100i.md) · [Verilog file](solutions/Day%2002/040-adder100i.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/adder100i)

![Generate for-loop: 100-bit binary adder 2 question and submitted solution](images/Day%2002/040-adder100i.png)

### What the question is asking

Generate a 100-bit ripple-carry adder and return both the sum and the carry from every bit stage.

### Saved Verilog solution

```verilog
module top_module(
    input [99:0] a, b,
    input cin,
    output [99:0] cout,
    output [99:0] sum
);
//instantiating 100 fa ,
    wire [100:0] carry;
    assign carry[0]=cin;
    assign cout=carry[100:1];
genvar i ;
    generate
        for(i=0;i<100;i=i+1)begin : adder100
            full_adder fa (
                .a(a[i]),
                .b(b[i]),
                .cin(carry[i]),
                .sum(sum[i]),
                .cout(carry[i+1])
            );
        end
    endgenerate
endmodule
module full_adder(
    input a, b, cin,
    output cout, sum
);
wire w1,w2,w3,w4;
    xor g1(sum, a,b,cin);
    //now the carry out part
    xor g2(w1,a,b);
    and g3(w2,w1,cin);
    and g4(w3,a,b);
    or g5(cout,w2,w3);
endmodule
```

---

<a id="problem-042"></a>
## 042 — Wire

[Problem note](problems/Day%2002/042-exams__m2014_q4h.md) · [Verilog file](solutions/Day%2002/042-exams__m2014_q4h.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/m2014_q4h)

![Wire question and submitted solution](images/Day%2002/042-exams__m2014_q4h.png)

### What the question is asking

Implement the shown circuit's output as a direct wire connection.

### Saved Verilog solution

```verilog
module top_module (
    input in,
    output out);
assign out = in
    ;

endmodule
```

---

<a id="problem-043"></a>
## 043 — GND

[Problem note](problems/Day%2002/043-exams__m2014_q4i.md) · [Verilog file](solutions/Day%2002/043-exams__m2014_q4i.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/m2014_q4i)

![GND question and submitted solution](images/Day%2002/043-exams__m2014_q4i.png)

### What the question is asking

Tie the requested output permanently low to represent ground.

### Saved Verilog solution

```verilog
module top_module (
    output out
);
assign out = 1'b0;
endmodule
```

---

<a id="problem-044"></a>
## 044 — NOR

[Problem note](problems/Day%2002/044-exams__m2014_q4e.md) · [Verilog file](solutions/Day%2002/044-exams__m2014_q4e.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/m2014_q4e)

![NOR question and submitted solution](images/Day%2002/044-exams__m2014_q4e.png)

### What the question is asking

Translate the shown gate symbol into the equivalent NOR logic expression.

### Saved Verilog solution

```verilog
module top_module (
    input in1,
    input in2,
    output out);
    nor g1(out, in1 , in2);
endmodule
```

---

<a id="problem-045"></a>
## 045 — Another gate

[Problem note](problems/Day%2002/045-exams__m2014_q4f.md) · [Verilog file](solutions/Day%2002/045-exams__m2014_q4f.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/m2014_q4f)

![Another gate question and submitted solution](images/Day%2002/045-exams__m2014_q4f.png)

### What the question is asking

Identify the function of the shown gate circuit and express it correctly in Verilog.

### Saved Verilog solution

```verilog
module top_module (
    input in1,
    input in2,
    output out
);
wire w1;
    not g1(w1,in2);
    and g2(out,w1,in1);
endmodule
```

---

<a id="problem-046"></a>
## 046 — Two gates

[Problem note](problems/Day%2002/046-exams__m2014_q4g.md) · [Verilog file](solutions/Day%2002/046-exams__m2014_q4g.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/exams/m2014_q4g)

![Two gates question and submitted solution](images/Day%2002/046-exams__m2014_q4g.png)

### What the question is asking

Translate the two-gate schematic into a single correct combinational output expression.

### Saved Verilog solution

```verilog
module top_module (
    input in1,
    input in2,
    input in3,
    output out
);
wire w1;
    xnor g1(w1,in1,in2);
    xor g2(out,in3,w1);
endmodule
```

---

<a id="problem-065"></a>
## 065 — Full adder

[Problem note](problems/Day%2002/065-fadd.md) · [Verilog file](solutions/Day%2002/065-fadd.sv) · [HDLBits problem](https://hdlbits.01xz.net/wiki/fadd)

![Full adder question and submitted solution](images/Day%2002/065-fadd.png)

### What the question is asking

Implement a full adder that includes carry-in and produces both sum and carry-out.

### Saved Verilog solution

```verilog
module top_module(
    input a, b, cin,
    output cout, sum
);
wire w1,w2,w3,w4;
    xor g1(sum, a,b,cin);
    //now the carry out part
    xor g2(w1,a,b);
    and g3(w2,w1,cin);
    and g4(w3,a,b);
    or g5(cout,w2,w3);
endmodule
```
