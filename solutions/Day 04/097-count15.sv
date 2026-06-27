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
