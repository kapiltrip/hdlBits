module top_module(
    input clk,
    input areset,
    input bump_left,
    input bump_right,
    input ground,
    input dig,
    output walk_left,
    output walk_right,
    output aaah,
    output digging
);

    reg [3:0] state, next_state;
    parameter left             = 3'b000;
    parameter right            = 3'b001;
    parameter fallRight        = 3'b010;
    parameter fallLeft         = 3'b011;
    parameter digWorkFromLeft  = 3'b100;
    parameter digWorkFromRight = 3'b101;
    parameter digWorkFallRight = 3'b110;
    parameter digWorkFallLeft  = 3'b111;

    always @(*) begin
        case (state)
            left: begin
                if (!ground)
                    next_state = fallLeft;
                else if (dig && ground)
                    next_state = digWorkFromLeft;
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
                else if (dig && ground)
                    next_state = digWorkFromRight;
                else if (bump_right && bump_left)
                    next_state = left;
                else if (bump_right)
                    next_state = left;
                else
                    next_state = right;
            end
            fallRight: next_state = !ground ? fallRight : right;
            fallLeft:  next_state = !ground ? fallLeft : left;
            digWorkFromLeft:
                next_state = ground ? digWorkFromLeft : digWorkFallLeft;
            digWorkFromRight:
                next_state = ground ? digWorkFromRight : digWorkFallRight;
            digWorkFallLeft:
                next_state = ground ? left : digWorkFallLeft;
            digWorkFallRight:
                next_state = ground ? right : digWorkFallRight;
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
    assign aaah = (state == digWorkFallLeft) ||
                  (state == digWorkFallRight) ||
                  (state == fallRight) ||
                  (state == fallLeft);
    assign digging = (state == digWorkFromLeft) ||
                     (state == digWorkFromRight);

endmodule
