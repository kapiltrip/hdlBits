`timescale 1ns/1ps

module q3fsm_correct (
    input  wire clk,
    input  wire reset,
    input  wire s,
    input  wire w,
    output wire z
);
    localparam A = 1'b0;
    localparam B = 1'b1;

    reg state, next_state;
    reg [1:0] ticks;
    reg [1:0] ones;
    reg zreg;

    always @(*) begin
        next_state = state;
        case (state)
            A:       next_state = s ? B : A;
            B:       next_state = B;
            default: next_state = A;
        endcase
    end

    always @(posedge clk) begin
        if (reset) begin
            state <= A;
            ticks <= 2'd0;
            ones  <= 2'd0;
            zreg  <= 1'b0;
        end else begin
            state <= next_state;
            zreg  <= 1'b0;

            if (state == A) begin
                ticks <= 2'd0;
                ones  <= 2'd0;
            end else if (ticks == 2'd2) begin
                zreg  <= ((ones + {1'b0, w}) == 2'd2);
                ticks <= 2'd0;
                ones  <= 2'd0;
            end else begin
                ticks <= ticks + 2'd1;
                if (w)
                    ones <= ones + 2'd1;
            end
        end
    end

    assign z = zreg;
endmodule

// Preserves the near-correct bug discussed in the saved Q&A: the window
// counters reset only when the classification result is true.
module q3fsm_reset_only_on_match_bug (
    input  wire clk,
    input  wire reset,
    input  wire s,
    input  wire w,
    output wire z
);
    localparam A = 1'b0;
    localparam B = 1'b1;

    reg state;
    reg [1:0] ticks;
    reg [1:0] ones;
    reg zreg;

    always @(posedge clk) begin
        if (reset) begin
            state <= A;
            ticks <= 2'd0;
            ones  <= 2'd0;
            zreg  <= 1'b0;
        end else begin
            zreg <= 1'b0;
            if (state == A) begin
                if (s)
                    state <= B;
                ticks <= 2'd0;
                ones  <= 2'd0;
            end else if (ticks == 2'd2) begin
                if ((ones + {1'b0, w}) == 2'd2) begin
                    zreg  <= 1'b1;
                    ticks <= 2'd0;
                    ones  <= 2'd0;
                end
            end else begin
                ticks <= ticks + 2'd1;
                if (w)
                    ones <= ones + 2'd1;
            end
        end
    end

    assign z = zreg;
endmodule

module day6_q3fsm_selfcheck;
    reg clk = 1'b0;
    reg reset = 1'b0;
    reg s = 1'b0;
    reg w = 1'b0;
    wire z_correct;
    wire z_bug;
    integer failures = 0;
    integer bug_divergences = 0;

    q3fsm_correct dut_correct (
        .clk(clk), .reset(reset), .s(s), .w(w), .z(z_correct)
    );

    q3fsm_reset_only_on_match_bug dut_bug (
        .clk(clk), .reset(reset), .s(s), .w(w), .z(z_bug)
    );

    always #5 clk = ~clk;

    task sample_group;
        input [2:0] samples;
        integer expected;
        integer k;
        begin
            for (k = 2; k >= 0; k = k - 1) begin
                @(negedge clk);
                w = samples[k];
                @(posedge clk);
                #1;
            end

            expected = (samples[2] + samples[1] + samples[0] == 2);
            if (z_correct !== expected[0]) begin
                $display("FAIL correct: samples=%b expected z=%0d got z=%b", samples, expected, z_correct);
                failures = failures + 1;
            end
            if (z_bug !== expected[0])
                bug_divergences = bug_divergences + 1;
        end
    endtask

    initial begin
        reset = 1'b1;
        repeat (2) @(posedge clk);
        #1;
        reset = 1'b0;

        // The edge that observes s=1 only enters state B. Sampling w starts
        // on the following edge, exactly as the problem statement requires.
        @(negedge clk);
        s = 1'b1;
        @(posedge clk);
        #1;
        s = 1'b0;

        // Exhaustive three-bit windows, placed back-to-back.
        sample_group(3'b000);
        sample_group(3'b001);
        sample_group(3'b010);
        sample_group(3'b011);
        sample_group(3'b100);
        sample_group(3'b101);
        sample_group(3'b110);
        sample_group(3'b111);

        // A repeated mixed sequence stresses continuous grouping.
        sample_group(3'b101);
        sample_group(3'b111);
        sample_group(3'b110);

        if (bug_divergences == 0) begin
            $display("FAIL: preserved buggy design never diverged from the reference result");
            failures = failures + 1;
        end

        if (failures == 0)
            $display("PASS: q3fsm correct design passed all exhaustive and back-to-back windows; buggy reset placement diverged as expected.");
        else
            $display("FAIL: q3fsm self-check found %0d error(s).", failures);

        $finish;
    end
endmodule
