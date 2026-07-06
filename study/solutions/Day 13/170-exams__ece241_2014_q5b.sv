module top_module (
    input clk,
    input areset,
    input x,
    output z
);
    reg zr;
    reg [1:0] state, next_state;
    parameter s0 = 2'b00;
    parameter s1 = 2'b01;

    always @(posedge clk or posedge areset) begin
        if (areset)
            state <= s0;
        else
            state <= next_state;
    end

    always @(*) begin
        case (state)
            s0: begin
                if (x) begin
                    next_state = s1;
                    zr = x;
                end
                else begin
                    next_state = s0;
                    zr = 1'b0;
                end
            end
            s1: begin
                next_state = s1;
                zr = ~x;
            end
            default: begin
                next_state = s0;
                zr = 1'b0;
            end
        endcase
    end

    assign z = zr;
endmodule
