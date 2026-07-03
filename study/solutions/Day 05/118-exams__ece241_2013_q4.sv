module top_module (
    input clk,
    input reset,
    input [3:1] s,
    output reg fr3,
    output reg fr2,
    output reg fr1,
    output reg dfr
);
    reg [2:0] state, next_state;

    parameter belows1 = 3'd0;
    parameter s3s2fall = 3'd1;
    parameter s3s2rise = 3'd2;
    parameter s2s1fall = 3'd3;
    parameter s2s1rise = 3'd4;
    parameter s3above = 3'd5;

    always @(posedge clk) begin
        if (reset)
            state <= belows1;
        else
            state <= next_state;
    end

    always @(*) begin
        next_state = state;
        case (state)
            belows1: begin
                if (s[3])
                    next_state = s3above;
                else if (s[2])
                    next_state = s3s2rise;
                else if (s[1])
                    next_state = s2s1rise;
                else
                    next_state = belows1;
            end
            s2s1rise: begin
                if (s[3])
                    next_state = s3above;
                else if (s[2])
                    next_state = s3s2rise;
                else if (s[1])
                    next_state = s2s1rise;
                else
                    next_state = belows1;
            end
            s2s1fall: begin
                if (s[3])
                    next_state = s3above;
                else if (s[2])
                    next_state = s3s2rise;
                else if (s[1])
                    next_state = s2s1fall;
                else
                    next_state = belows1;
            end
            s3s2rise: begin
                if (s[3])
                    next_state = s3above;
                else if (s[2])
                    next_state = s3s2rise;
                else if (s[1])
                    next_state = s2s1fall;
                else
                    next_state = belows1;
            end
            s3s2fall: begin
                if (s[3])
                    next_state = s3above;
                else if (s[2])
                    next_state = s3s2fall;
                else if (s[1])
                    next_state = s2s1fall;
                else
                    next_state = belows1;
            end
            s3above: begin
                if (s[3])
                    next_state = s3above;
                else if (s[2])
                    next_state = s3s2fall;
                else if (s[1])
                    next_state = s2s1fall;
                else
                    next_state = belows1;
            end
            default: next_state = belows1;
        endcase
    end

    always @(*) begin
        case (state)
            belows1: {fr3, fr2, fr1, dfr} = 4'b1111;
            s2s1rise: {fr3, fr2, fr1, dfr} = 4'b0110;
            s2s1fall: {fr3, fr2, fr1, dfr} = 4'b0111;
            s3s2rise: {fr3, fr2, fr1, dfr} = 4'b0010;
            s3s2fall: {fr3, fr2, fr1, dfr} = 4'b0011;
            s3above: {fr3, fr2, fr1, dfr} = 4'b0000;
            default: {fr3, fr2, fr1, dfr} = 4'b1111;
        endcase
    end

endmodule
