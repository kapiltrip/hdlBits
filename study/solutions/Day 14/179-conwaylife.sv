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
