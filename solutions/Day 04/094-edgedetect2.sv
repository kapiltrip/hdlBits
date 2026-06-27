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
