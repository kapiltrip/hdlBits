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
