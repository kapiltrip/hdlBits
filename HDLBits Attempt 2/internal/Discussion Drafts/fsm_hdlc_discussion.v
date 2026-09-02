// Discussion draft saved from Kapil's HDLBits Attempt 2 work.
// The FSM logic is preserved; only pasted Markdown/escape artifacts were removed.

module top_module (
    input  clk,
    input  reset,    // Synchronous reset
    input  in,
    output disc,
    output flag,
    output err
);

    reg discReg = 0;
    reg flagReg = 0;
    reg errReg = 0;

    reg [2:0] state, next_state;
    parameter s0    = 3'b000;
    parameter s1    = 3'b001;
    parameter s2    = 3'b010;
    parameter s3    = 3'b011;
    parameter s4    = 3'b100;
    parameter discS = 3'b101;
    parameter flagg = 3'b110;
    parameter error = 3'b111;

    always @(posedge clk) begin
        if (reset)
            state <= s0;
        else
            state <= next_state;
    end

    always @(*) begin
        next_state = state;
        discReg = 0;
        flagReg = 0;
        errReg = 0;

        case (state)
            s0: next_state = (in) ? s1 : s0;
            s1: next_state = (in) ? s2 : s0; // 1
            s2: next_state = (in) ? s3 : s0; // 11
            s3: next_state = (in) ? s4 : s0; // 111
            s4: next_state = (in) ? discS : s0; // 1111

            discS: begin
                if (!in) begin
                    discReg = 1;
                    next_state = s0;
                end else begin
                    next_state = flagg;
                    discReg = 0;
                end
            end

            flagg: begin
                if (!in) begin
                    next_state = s0;
                    flagReg = 1;
                end else begin
                    next_state = error;
                    flagReg = 0;
                end
            end

            error: begin
                if (in) begin
                    next_state = error;
                    errReg = 1;
                end else begin
                    next_state = s0;
                    errReg = 0;
                end
            end

            default: next_state = s0;
        endcase
    end

    assign disc = discReg;
    assign flag = flagReg;
    assign err = errReg;

endmodule
