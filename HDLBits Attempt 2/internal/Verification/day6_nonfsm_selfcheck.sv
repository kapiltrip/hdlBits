`timescale 1ns/1ps

module dualedge_mux_solution (
    input  wire clk,
    input  wire d,
    output wire q
);
    reg qpos;
    reg qneg;

    always @(posedge clk)
        qpos <= d;

    always @(negedge clk)
        qneg <= d;

    assign q = clk ? qpos : qneg;
endmodule

module dualedge_xor_solution (
    input  wire clk,
    input  wire d,
    output wire q
);
    // The cross-coupled XOR recurrence needs a known starting point.
    // Declaration initialization models the FPGA power-up assumption that
    // must be stated when this no-reset form is used.
    reg qpos = 1'b0;
    reg qneg = 1'b0;

    always @(posedge clk)
        qpos <= d ^ qneg;

    always @(negedge clk)
        qneg <= d ^ qpos;

    assign q = qpos ^ qneg;
endmodule

module dualedge_or_bug (
    input  wire clk,
    input  wire d,
    output wire q
);
    reg qpos;
    reg qneg;

    always @(posedge clk)
        qpos <= d;

    always @(negedge clk)
        qneg <= d;

    assign q = qpos | qneg;
endmodule

module circuit5_solution (
    input  wire [3:0] a,
    input  wire [3:0] b,
    input  wire [3:0] c,
    input  wire [3:0] d,
    input  wire [3:0] e,
    output reg  [3:0] q
);
    always @(*) begin
        case (c)
            4'd0:    q = b;
            4'd1:    q = e;
            4'd2:    q = a;
            4'd3:    q = d;
            default: q = 4'hf;
        endcase
    end
endmodule

module day6_nonfsm_selfcheck;
    reg clk = 1'b0;
    reg d_bit = 1'b0;
    wire q_mux;
    wire q_xor;
    wire q_or_bug;

    reg [3:0] a, b, c, d, e;
    wire [3:0] q;

    integer failures = 0;
    integer or_bug_divergences = 0;
    integer selector;
    reg [3:0] expected;

    dualedge_mux_solution mux_dut(.clk(clk), .d(d_bit), .q(q_mux));
    dualedge_xor_solution xor_dut(.clk(clk), .d(d_bit), .q(q_xor));
    dualedge_or_bug or_bug_dut(.clk(clk), .d(d_bit), .q(q_or_bug));
    circuit5_solution circuit_dut(.a(a), .b(b), .c(c), .d(d), .e(e), .q(q));

    task drive_posedge;
        input next_d;
        begin
            d_bit = next_d;
            #4;
            clk = 1'b1;
            #1;
            if (q_mux !== next_d) begin
                $display("FAIL mux at posedge: d=%b q=%b", next_d, q_mux);
                failures = failures + 1;
            end
            if (q_or_bug !== next_d)
                or_bug_divergences = or_bug_divergences + 1;
        end
    endtask

    task drive_negedge;
        input next_d;
        begin
            d_bit = next_d;
            #4;
            clk = 1'b0;
            #1;
            if (q_mux !== next_d) begin
                $display("FAIL mux at negedge: d=%b q=%b", next_d, q_mux);
                failures = failures + 1;
            end
            if (q_xor !== next_d) begin
                $display("FAIL xor at negedge: d=%b q=%b", next_d, q_xor);
                failures = failures + 1;
            end
            if (q_or_bug !== next_d)
                or_bug_divergences = or_bug_divergences + 1;
        end
    endtask

    initial begin
        a = 4'h9;
        b = 4'h3;
        c = 4'h0;
        d = 4'h7;
        e = 4'h5;

        // Initialize both XOR-feedback registers, then alternate data on
        // every edge so stale-value OR behavior is forced to fail.
        drive_posedge(1'b0);
        drive_negedge(1'b0);
        drive_posedge(1'b1);
        #0;
        if (q_xor !== 1'b1) failures = failures + 1;
        drive_negedge(1'b0);
        drive_posedge(1'b0);
        #0;
        if (q_xor !== 1'b0) failures = failures + 1;
        drive_negedge(1'b1);
        drive_posedge(1'b1);
        #0;
        if (q_xor !== 1'b1) failures = failures + 1;
        drive_negedge(1'b0);

        if (or_bug_divergences == 0) begin
            $display("FAIL: OR-based dual-edge bug never diverged");
            failures = failures + 1;
        end

        for (selector = 0; selector < 16; selector = selector + 1) begin
            c = selector[3:0];
            #1;
            case (selector)
                0: expected = b;
                1: expected = e;
                2: expected = a;
                3: expected = d;
                default: expected = 4'hf;
            endcase
            if (q !== expected) begin
                $display("FAIL circuit5: c=%0d expected=%h got=%h", selector, expected, q);
                failures = failures + 1;
            end
        end

        if (failures == 0)
            $display("PASS: Dualedge MUX/XOR solutions and all 16 Circuit5 selector values passed; OR bug diverged as expected.");
        else
            $display("FAIL: Day 6 non-FSM self-check found %0d error(s).", failures);

        $finish;
    end
endmodule
