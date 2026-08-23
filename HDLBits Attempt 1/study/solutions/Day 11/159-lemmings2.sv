module top_module(
    input clk,
    input areset,
    input bump_left,
    input bump_right,
    input ground,
    output walk_left,
    output walk_right,
    output aaah
);

    reg [1:0] state, next_state;
    parameter left      = 2'b00;
    parameter right     = 2'b01;
    parameter fallRight = 2'b10;
    parameter fallLeft  = 2'b11;

    always @(*) begin
        case (state)
            left: begin
                if (!ground)
                    next_state = fallLeft;
                else if (bump_right && bump_left)
                    next_state = right;
                else if (bump_left)
                    next_state = right;
                else
                    next_state = left;
            end
            right: begin
                if (!ground)
                    next_state = fallRight;
                else if (bump_right && bump_left)
                    next_state = left;
                else if (bump_right)
                    next_state = left;
                else
                    next_state = right;
            end
            fallRight: begin
                if (!ground)
                    next_state = fallRight;
                else
                    next_state = right;
            end
            fallLeft: begin
                if (!ground)
                    next_state = fallLeft;
                else
                    next_state = left;
            end
            default: next_state = left;
        endcase
    end

    always @(posedge clk or posedge areset) begin
        if (areset)
            state <= left;
        else
            state <= next_state;
    end

    assign walk_left  = (state == left);
    assign walk_right = (state == right);
    assign aaah = (state == fallRight) || (state == fallLeft);

endmodule
