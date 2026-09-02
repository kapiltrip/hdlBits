// Working HDLBits solution for: https://hdlbits.01xz.net/wiki/Fsm_hdlc
// Ten-state Moore FSM: outputs depend only on the registered current state.

module top_module (
    input  clk,
    input  reset,    // Synchronous reset
    input  in,
    output disc,
    output flag,
    output err
);

    reg [3:0] state, next_state;

    parameter s0             = 4'b0000;
    parameter s1             = 4'b0001;
    parameter s2             = 4'b0010;
    parameter s3             = 4'b0011;
    parameter s4             = 4'b0100;
    parameter discarded      = 4'b0101;
    parameter flagged        = 4'b0110;
    parameter errorFound     = 4'b0111;
    parameter discardedFinal = 4'b1000;
    parameter flaggedFinal   = 4'b1001;

    always @(posedge clk) begin
        if (reset)
            state <= s0;
        else
            state <= next_state;
    end

    always @(*) begin
        next_state = state;

        case (state)
            s0:             next_state = (in) ? s1         : s0;             // 0 ones
            s1:             next_state = (in) ? s2         : s0;             // 1 one
            s2:             next_state = (in) ? s3         : s0;             // 2 ones
            s3:             next_state = (in) ? s4         : s0;             // 3 ones
            s4:             next_state = (in) ? discarded  : s0;             // 4 ones
            discarded:      next_state = (in) ? flagged    : discardedFinal; // 5 ones
            discardedFinal: next_state = (in) ? s1         : s0;             // disc pulse
            flagged:        next_state = (in) ? errorFound : flaggedFinal;   // 6 ones
            flaggedFinal:   next_state = (in) ? s1         : s0;             // flag pulse
            errorFound:     next_state = (in) ? errorFound : s0;             // 7+ ones
            default:        next_state = s0;
        endcase
    end

    assign disc = (state == discardedFinal);
    assign flag = (state == flaggedFinal);
    assign err  = (state == errorFound);

endmodule
