module top_module (
    input clk,
    input reset,
    input data,
    output start_shifting
);
    localparam S0   = 3'b000;
    localparam S1   = 3'b001;
    localparam S2   = 3'b010;
    localparam S3   = 3'b011;
    localparam DONE = 3'b100;

    reg [2:0] state;
    reg [2:0] next_state;

    always @(posedge clk) begin
        if (reset)
            state <= S0;
        else
            state <= next_state;
    end

    always @(*) begin
        case (state)
            S0:      next_state = data ? S1 : S0;
            S1:      next_state = data ? S2 : S0;
            S2:      next_state = data ? S2 : S3;
            S3:      next_state = data ? DONE : S0;
            DONE:    next_state = DONE;
            default: next_state = S0;
        endcase
    end

    assign start_shifting = (state == DONE);
endmodule
