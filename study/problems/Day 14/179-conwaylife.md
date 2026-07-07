# 179 — Conway's Game of Life 16x16

| Field | Value |
|---|---|
| Day | Day 14 |
| Last successful submission | 2026-07-07 1:36:17 PM |
| Course location | Circuits → Sequential Logic → More Circuits |
| HDLBits identifier | `conwaylife` |
| Attempts | 6 total: 1 incorrect, 3 compile error, 0 simulation error |
| Success rate | 33% |
| Source | [Open original HDLBits problem](https://hdlbits.01xz.net/wiki/conwaylife) |
| Files | Screenshot rendered below · [Mistake review](../../Mistakes.md#24-conway-life-wrap-the-grid-before-counting-neighbours) · [Verilog solution](../../solutions/Day%2014/179-conwaylife.sv) |

## Question and submitted solution

![Conway's Game of Life 16x16 question and submitted solution](../../images/Day%2014/179-conwaylife-question-and-successful-submission.png)

## Supporting review screenshot

![Conwaylife highlighted prompt and toroidal-grid question](../../images/Mistakes/Screenshot%202026-07-07%20125205.png)

For a corner cell, the edge does not stop the neighbourhood. Cell `(0,0)` uses wrapped neighbours `(15,15)`, `(15,0)`, `(15,1)`, `(0,15)`, `(0,1)`, `(1,15)`, `(1,0)`, and `(1,1)`. The code computes those wrapped row and column indices before counting.

## What the question is asking

The Game of Life state is a 16 by 16 toroidal grid packed into `q[255:0]`, with each row occupying a 16-bit slice. A cell's next value depends on the count of its eight neighbours, while the load input synchronously replaces the whole grid with `data` for initialization.

The toroidal boundary condition is the important part: row 0's upper neighbour is row 15, row 15's lower neighbour is row 0, column 0's left neighbour is column 15, and column 15's right neighbour is column 0. The implementation computes those wrapped row and column indices for every cell, accumulates the eight one-bit neighbour values into an integer count, and writes the corresponding bit of `next_q`.

The update rule follows the problem statement exactly. A cell becomes alive when it has exactly three neighbours. With exactly two neighbours it keeps its previous state, so the expression is `neighbours == 3 || (q[index] && neighbours == 2)`. All `next_q` bits are computed combinationally from the old registered `q`, then one clock edge commits the whole generation with a nonblocking assignment. This avoids accidentally updating one cell early and letting that new value affect another cell in the same generation.

## Saved Verilog solution

```verilog
module top_module(
    input clk,
    input load,
    input [255:0] data,
    output reg [255:0] q
);
    reg [255:0] next_q;
    integer row;
    integer col;
    integer up;
    integer down;
    integer left;
    integer right;
    integer index;
    integer neighbours;

    always @(*) begin
        next_q = 256'b0;
        for (row = 0; row < 16; row = row + 1) begin
            for (col = 0; col < 16; col = col + 1) begin
                up = (row == 0) ? 15 : row - 1;
                down = (row == 15) ? 0 : row + 1;
                left = (col == 0) ? 15 : col - 1;
                right = (col == 15) ? 0 : col + 1;
                index = row * 16 + col;

                neighbours = 0;
                neighbours = neighbours + q[up * 16 + left];
                neighbours = neighbours + q[up * 16 + col];
                neighbours = neighbours + q[up * 16 + right];
                neighbours = neighbours + q[row * 16 + left];
                neighbours = neighbours + q[row * 16 + right];
                neighbours = neighbours + q[down * 16 + left];
                neighbours = neighbours + q[down * 16 + col];
                neighbours = neighbours + q[down * 16 + right];

                next_q[index] = (neighbours == 3) ||
                                (q[index] && (neighbours == 2));
            end
        end
    end

    always @(posedge clk) begin
        if (load)
            q <= data;
        else
            q <= next_q;
    end
endmodule
```

## What I learned

_Fill this in during revision._
