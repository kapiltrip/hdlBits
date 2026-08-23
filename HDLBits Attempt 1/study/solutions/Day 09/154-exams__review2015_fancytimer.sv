module top_module (
    input clk,
    input reset,
    input data,
    output [3:0] count,
    output counting,
    output done,
    input ack
);
    localparam S     = 4'd0;
    localparam S1    = 4'd1;
    localparam S11   = 4'd2;
    localparam S110  = 4'd3;
    localparam B0    = 4'd4;
    localparam B1    = 4'd5;
    localparam B2    = 4'd6;
    localparam B3    = 4'd7;
    localparam COUNT = 4'd8;
    localparam WAIT  = 4'd9;

    reg [3:0] state;
    reg [3:0] next_state;
    reg [3:0] delay;
    reg [3:0] count_remaining;
    reg [9:0] count_1000;

    wire shift_ena = (state == B0) || (state == B1) ||
                     (state == B2) || (state == B3);
    wire finished = (count_1000 == 10'd999) &&
                    (count_remaining == 4'd0);

    always @(posedge clk) begin
        if (reset)
            state <= S;
        else
            state <= next_state;
    end

    always @(*) begin
        case (state)
            S:     next_state = data ? S1 : S;
            S1:    next_state = data ? S11 : S;
            S11:   next_state = data ? S11 : S110;
            S110:  next_state = data ? B0 : S;
            B0:    next_state = B1;
            B1:    next_state = B2;
            B2:    next_state = B3;
            B3:    next_state = COUNT;
            COUNT: next_state = finished ? WAIT : COUNT;
            WAIT:  next_state = ack ? S : WAIT;
            default: next_state = S;
        endcase
    end

    always @(posedge clk) begin
        if (reset) begin
            delay <= 4'd0;
            count_remaining <= 4'd0;
            count_1000 <= 10'd0;
        end
        else begin
            if (shift_ena)
                delay <= {delay[2:0], data};

            if (state == B3) begin
                count_remaining <= {delay[2:0], data};
                count_1000 <= 10'd0;
            end
            else if (counting) begin
                if (count_1000 == 10'd999) begin
                    count_1000 <= 10'd0;
                    if (count_remaining != 4'd0)
                        count_remaining <= count_remaining - 4'd1;
                end
                else begin
                    count_1000 <= count_1000 + 10'd1;
                end
            end
        end
    end

    assign count = count_remaining;
    assign counting = (state == COUNT);
    assign done = (state == WAIT);
endmodule
