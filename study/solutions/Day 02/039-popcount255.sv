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
