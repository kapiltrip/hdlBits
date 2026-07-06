module top_module (
    input clk,
    input load,
    input [511:0] data,
    output reg [511:0] q
);
    integer i;
    reg lsb, center, msb;

    always @(posedge clk) begin
        if (load)
            q <= data;
        else begin
            for (i = 0; i < 512; i = i + 1) begin
                if (i == 0)
                    lsb = 1'b0;
                else
                    lsb = q[i-1];

                center = q[i];
                if (i == 511)
                    msb = 1'b0;
                else
                    msb = q[i+1];

                case ({msb, center, lsb})
                    3'b000: q[i] <= 1'b0;
                    3'b001: q[i] <= 1'b1;
                    3'b010: q[i] <= 1'b1;
                    3'b011: q[i] <= 1'b1;
                    3'b100: q[i] <= 1'b0;
                    3'b101: q[i] <= 1'b1;
                    3'b110: q[i] <= 1'b1;
                    3'b111: q[i] <= 1'b0;
                endcase
            end
        end
    end
endmodule
