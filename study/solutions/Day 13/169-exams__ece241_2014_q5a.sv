module top_module (
    input clk,
    input areset,
    input x,
    output z
);
    reg [1:0] state, next_state;
    parameter s0 = 2'b00;
    parameter s1 = 2'b01;
    parameter s2 = 2'b10;

    always @(posedge clk or posedge areset) begin
        if (areset)
            state <= s0;
        else
            state <= next_state;
    end

    always @(*) begin
        case (state)
            s0: next_state = x ? s1 : s0;
            s1: next_state = x ? s2 : s1;
            s2: next_state = x ? s2 : s1;
            default: next_state = s0;
        endcase
    end

    assign z = (state == s1);
endmodule
