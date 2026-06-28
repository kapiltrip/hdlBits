module top_module(
    input clk,
    input in,
    input reset,
    output out
);

    parameter A = 2'b00;
    parameter B = 2'b01;
    parameter C = 2'b10;
    parameter D = 2'b11;
    reg [1:0] state, next_state;

    always @(*) begin
        next_state = state;
        case (state)
            A: next_state = in ? B : A;
            B: next_state = in ? B : C;
            C: next_state = in ? D : A;
            D: next_state = in ? B : C;
        endcase
    end

    always @(posedge clk) begin
        if (reset)
            state <= A;
        else
            state <= next_state;
    end

    assign out = (state == D);

endmodule
