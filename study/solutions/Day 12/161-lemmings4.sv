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
    parameter left             = 4'b0000;
    parameter right            = 4'b0001;
    parameter fallRight        = 4'b0010;
    parameter fallLeft         = 4'b0011;
    parameter digWorkFromLeft  = 4'b0100;
    parameter digWorkFromRight = 4'b0101;
    parameter digWorkFallRight = 4'b0110;
    parameter digWorkFallLeft  = 4'b0111;
    parameter splatter         = 4'b1000;

    reg [4:0] willCount;

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
            fallRight: begin
                if (!ground)
                    next_state = fallRight;
                else if (willCount >= 5'd20)
                    next_state = splatter;
                else
                    next_state = right;
            end
            fallLeft: begin
                if (!ground)
                    next_state = fallLeft;
                else if (willCount >= 5'd20)
                    next_state = splatter;
                else
                    next_state = left;
            end
            digWorkFromLeft:
                next_state = ground ? digWorkFromLeft : digWorkFallLeft;
            digWorkFromRight:
                next_state = ground ? digWorkFromRight : digWorkFallRight;
            digWorkFallLeft:
                next_state = ground ? left : digWorkFallLeft;
            digWorkFallRight:
                next_state = ground ? right : digWorkFallRight;
            splatter: next_state = splatter;
            default: next_state = left;
        endcase
    end

    always @(posedge clk or posedge areset) begin
        if (areset)
            state <= left;
        else
            state <= next_state;
    end

    always @(posedge clk or posedge areset) begin
        if (areset)
            willCount <= 5'd0;
        else if (state == fallLeft || state == fallRight) begin
            if (willCount == 5'd21)
                willCount <= willCount;
            else
                willCount <= willCount + 5'd1;
        end
        else
            willCount <= 5'd0;
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
