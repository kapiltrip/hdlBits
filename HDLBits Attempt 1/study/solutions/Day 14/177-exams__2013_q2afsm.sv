module top_module (
    input clk,
    input resetn,
    input [3:1] r,
    output [3:1] g
);
    reg [1:0] state, next_state;
    parameter idle = 2'b00;
    parameter s1 = 2'b01;
    parameter s2 = 2'b10;
    parameter s3 = 2'b11;

    always @(posedge clk) begin
        if (!resetn)
            state <= idle;
        else
            state <= next_state;
    end

    always @(*) begin
        case (state)
            idle: begin
                if (r[1])
                    next_state = s1;
                else if (r[2])
                    next_state = s2;
                else if (r[3])
                    next_state = s3;
                else
                    next_state = idle;
            end
            s1: next_state = r[1] ? s1 : idle;
            s2: next_state = r[2] ? s2 : idle;
            s3: next_state = r[3] ? s3 : idle;
            default: next_state = idle;
        endcase
    end

    assign g[1] = (state == s1);
    assign g[2] = (state == s2);
    assign g[3] = (state == s3);
endmodule
