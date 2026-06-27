module top_module(clk, reset, in, out);
    input clk;
    input reset;    // Synchronous reset to state B
    input in;
    output out;

    reg present_state, next_state;

    parameter A = 1'b0;
    parameter B = 1'b1;

    // State transition logic
    always @(*) begin
        case (present_state)
            A: next_state = in ? A : B;
            B: next_state = in ? B : A;
            default: next_state = B;
        endcase
    end

    // State flip-flop
    always @(posedge clk) begin
        if (reset)
            present_state <= B;
        else
            present_state <= next_state;
    end

    // Output logic
    assign out = (present_state == B);

endmodule
