module top_module (
    input clk,
    input slowena,
    input reset,
    output [3:0] q
);
//0 to 9 inclusive 
    reg [3:0] count;
    always @(posedge clk)begin
        if(reset)begin
            count <= 4'b0000;
        end else begin
            if(count>= 4'b1001 && slowena)
                count<=4'b0000;
            else if(slowena)
                count<=count+1'b1;
            
        end
    end
    assign q=count ;
    
endmodule
