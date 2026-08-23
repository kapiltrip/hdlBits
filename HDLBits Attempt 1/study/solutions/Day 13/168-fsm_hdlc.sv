module top_module(
    input clk,
    input reset,
    input in,
    output disc,
    output flag,
    output err
);

    reg [3:0] state, next_state;

    parameter s0    = 4'b0000;
    parameter s1    = 4'b0001;
    parameter s2    = 4'b0010;
    parameter s3    = 4'b0011;
    parameter s4    = 4'b0100;
    parameter s5    = 4'b0101;
    parameter s6    = 4'b0110;
    parameter discc = 4'b0111;
    parameter flagg = 4'b1000;
    parameter errr  = 4'b1001;

    always @(posedge clk) begin
        if (reset)
            state <= s0;
        else
            state <= next_state;
    end

    always @(*) begin
        case (state)
            s0:    next_state = in ? s1 : s0;
            s1:    next_state = in ? s2 : s0;
            s2:    next_state = in ? s3 : s0;
            s3:    next_state = in ? s4 : s0;
            s4:    next_state = in ? s5 : s0;
            s5:    next_state = in ? s6 : discc;
            discc: next_state = in ? s1 : s0;
            s6:    next_state = in ? errr : flagg;
            flagg: next_state = in ? s1 : s0;
            errr:  next_state = in ? errr : s0;
            default: next_state = s0;
        endcase
    end

    assign disc = (state == discc);
    assign flag = (state == flagg);
    assign err  = (state == errr);

endmodule
