module top_module (
    input clk,
    input load,
    input [255:0] data,
    output reg [255:0] q
);
    reg [255:0] next_q;
    integer row, col, up, down, left, right, count;

    always @(*) begin
        next_q = q;
        for (row = 0; row < 16; row = row + 1) begin
            for (col = 0; col < 16; col = col + 1) begin
                up    = (row == 0)  ? 15 : row - 1;
                down  = (row == 15) ? 0  : row + 1;
                left  = (col == 0)  ? 15 : col - 1;
                right = (col == 15) ? 0  : col + 1;
                count = q[up*16+left] + q[up*16+col]
                      + q[up*16+right] + q[row*16+left]
                      + q[row*16+right] + q[down*16+left]
                      + q[down*16+col] + q[down*16+right];
                if (count == 2)
                    next_q[row*16+col] = q[row*16+col];
                else if (count == 3)
                    next_q[row*16+col] = 1'b1;
                else
                    next_q[row*16+col] = 1'b0;
            end
        end
    end

    always @(posedge clk) begin
        if (load) q <= data;
        else      q <= next_q;
    end
endmodule
