module top_module(
    input clk,
    input areset,
    input bump_left,
    input bump_right,
    output walk_left,
    output walk_right
);

    reg state, next_state;
    parameter left = 1'b0;
    parameter right = 1'b1;

    always @(*) begin
        next_state = state;
        case (state)
            left: next_state = bump_left ? right : left;
            right: next_state = bump_right ? left : right;
        endcase
    end

    always @(posedge clk or posedge areset) begin
        if (areset)
            state <= left;
        else
            state <= next_state;
    end

    assign walk_left = (state == left);
    assign walk_right = (state == right);

endmodule
