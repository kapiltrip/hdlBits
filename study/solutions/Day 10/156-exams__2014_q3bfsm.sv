module top_module (
    input clk,
    input reset,
    input x,
    output z
);
    localparam S0 = 3'd0, S1 = 3'd1, S2 = 3'd2,
               S3 = 3'd3, S4 = 3'd4;
    reg [2:0] state, next_state;

    always @(posedge clk) begin
        if (reset)
            state <= S0;
        else
            state <= next_state;
    end

    always @(*) begin
        case (state)
            S0: next_state = x ? S1 : S0;
            S1: next_state = x ? S4 : S1;
            S2: next_state = x ? S1 : S2;
            S3: next_state = x ? S2 : S1;
            S4: next_state = x ? S4 : S3;
            default: next_state = S0;
        endcase
    end

    assign z = (state == S3) || (state == S4);
endmodule
