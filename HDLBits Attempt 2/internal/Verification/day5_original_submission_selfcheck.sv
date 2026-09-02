`timescale 1ns/1ps

module edgedetect_review (
    input  logic       clk,
    input  logic [7:0] in,
    output logic [7:0] pedge
);
    logic [7:0] previous;

    always_ff @(posedge clk) begin
        previous <= in;
        pedge    <= in & ~previous;
    end
endmodule

module q8_mealy_101_review (
    input  logic clk,
    input  logic aresetn,
    input  logic x,
    output logic z
);
    localparam logic [1:0] S_NONE = 2'b00;
    localparam logic [1:0] S_1    = 2'b01;
    localparam logic [1:0] S_10   = 2'b10;

    logic [1:0] state, next_state;

    always_ff @(posedge clk or negedge aresetn) begin
        if (!aresetn)
            state <= S_NONE;
        else
            state <= next_state;
    end

    always_comb begin
        next_state = state;
        z = 1'b0;

        case (state)
            S_NONE: next_state = x ? S_1 : S_NONE;
            S_1:    next_state = x ? S_1 : S_10;
            S_10: begin
                if (x) begin
                    next_state = S_1;
                    z = 1'b1;
                end else begin
                    next_state = S_NONE;
                end
            end
            default: next_state = S_NONE;
        endcase
    end
endmodule

module gates4_review (
    input  logic [3:0] in,
    output logic       out_and,
    output logic       out_or,
    output logic       out_xor
);
    assign out_and = &in;
    assign out_or  = |in;
    assign out_xor = ^in;
endmodule

module q5a_moore_twos_complement_review (
    input  logic clk,
    input  logic areset,
    input  logic x,
    output logic z
);
    localparam logic [1:0] COPY_ZERO = 2'b00;
    localparam logic [1:0] OUTPUT_1  = 2'b01;
    localparam logic [1:0] OUTPUT_0  = 2'b10;

    logic [1:0] state, next_state;

    always_ff @(posedge clk or posedge areset) begin
        if (areset)
            state <= COPY_ZERO;
        else
            state <= next_state;
    end

    always_comb begin
        case (state)
            COPY_ZERO: next_state = x ? OUTPUT_1 : COPY_ZERO;
            OUTPUT_1:  next_state = x ? OUTPUT_0 : OUTPUT_1;
            OUTPUT_0:  next_state = x ? OUTPUT_0 : OUTPUT_1;
            default:   next_state = COPY_ZERO;
        endcase
    end

    assign z = (state == OUTPUT_1);
endmodule

module circuit4_review (
    input  logic a,
    input  logic b,
    input  logic c,
    input  logic d,
    output logic q
);
    assign q = b | c;
endmodule

module vector3_review (
    input  logic [4:0] a,
    input  logic [4:0] b,
    input  logic [4:0] c,
    input  logic [4:0] d,
    input  logic [4:0] e,
    input  logic [4:0] f,
    output logic [7:0] w,
    output logic [7:0] x,
    output logic [7:0] y,
    output logic [7:0] z
);
    assign {w, x, y, z} = {a, b, c, d, e, f, 2'b11};
endmodule

module edgecapture_review (
    input  logic        clk,
    input  logic        reset,
    input  logic [31:0] in,
    output logic [31:0] out
);
    logic [31:0] previous;

    always_ff @(posedge clk) begin
        previous <= in;
        if (reset)
            out <= 32'b0;
        else
            out <= out | (previous & ~in);
    end
endmodule

module ringer_review (
    input  logic ring,
    input  logic vibrate_mode,
    output logic ringer,
    output logic motor
);
    assign ringer = ring & ~vibrate_mode;
    assign motor  = ring &  vibrate_mode;
endmodule

module q5b_mealy_twos_complement_onehot_review (
    input  logic clk,
    input  logic areset,
    input  logic x,
    output logic z
);
    localparam logic [1:0] BEFORE_FIRST_ONE = 2'b01;
    localparam logic [1:0] AFTER_FIRST_ONE  = 2'b10;

    logic [1:0] state, next_state;

    always_ff @(posedge clk or posedge areset) begin
        if (areset)
            state <= BEFORE_FIRST_ONE;
        else
            state <= next_state;
    end

    always @(*) begin
        next_state = state;
        z = 1'b0;

        case (1'b1)
            state[0]: begin
                z = x;
                if (x)
                    next_state = AFTER_FIRST_ONE;
            end
            state[1]: begin
                z = ~x;
                next_state = AFTER_FIRST_ONE;
            end
            default: begin
                next_state = BEFORE_FIRST_ONE;
                z = x;
            end
        endcase
    end
endmodule

module tb;
    logic clk = 1'b0;
    integer failures = 0;
    integer i;

    logic [7:0] edge_in = 8'b0;
    logic [7:0] edge_pulse;
    logic [7:0] edge_model_previous = 8'b0;

    logic q8_aresetn = 1'b0;
    logic q8_x = 1'b0;
    logic q8_z;

    logic [3:0] gates_in = 4'b0;
    logic gates_and, gates_or, gates_xor;

    logic q5a_areset = 1'b1;
    logic q5a_x = 1'b0;
    logic q5a_z;
    logic q5a_seen_one = 1'b0;

    logic circuit_a = 1'b0;
    logic circuit_b = 1'b0;
    logic circuit_c = 1'b0;
    logic circuit_d = 1'b0;
    logic circuit_q;

    logic [4:0] vector_a = 5'b0;
    logic [4:0] vector_b = 5'b0;
    logic [4:0] vector_c = 5'b0;
    logic [4:0] vector_d = 5'b0;
    logic [4:0] vector_e = 5'b0;
    logic [4:0] vector_f = 5'b0;
    logic [7:0] vector_w, vector_x, vector_y, vector_z;
    logic [31:0] vector_expected;

    logic capture_reset = 1'b1;
    logic [31:0] capture_in = 32'b0;
    logic [31:0] capture_out;
    logic [31:0] capture_model_previous = 32'b0;
    logic [31:0] capture_model_out = 32'b0;

    logic ring = 1'b0;
    logic vibrate_mode = 1'b0;
    logic ringer;
    logic motor;

    logic q5b_areset = 1'b1;
    logic q5b_x = 1'b0;
    logic q5b_z;
    logic q5b_seen_one = 1'b0;

    always #5 clk = ~clk;

    edgedetect_review dut_edge (
        .clk(clk), .in(edge_in), .pedge(edge_pulse)
    );

    q8_mealy_101_review dut_q8 (
        .clk(clk), .aresetn(q8_aresetn), .x(q8_x), .z(q8_z)
    );

    gates4_review dut_gates (
        .in(gates_in), .out_and(gates_and), .out_or(gates_or), .out_xor(gates_xor)
    );

    q5a_moore_twos_complement_review dut_q5a (
        .clk(clk), .areset(q5a_areset), .x(q5a_x), .z(q5a_z)
    );

    circuit4_review dut_circuit4 (
        .a(circuit_a), .b(circuit_b), .c(circuit_c), .d(circuit_d), .q(circuit_q)
    );

    vector3_review dut_vector3 (
        .a(vector_a), .b(vector_b), .c(vector_c), .d(vector_d), .e(vector_e), .f(vector_f),
        .w(vector_w), .x(vector_x), .y(vector_y), .z(vector_z)
    );

    edgecapture_review dut_capture (
        .clk(clk), .reset(capture_reset), .in(capture_in), .out(capture_out)
    );

    ringer_review dut_ringer (
        .ring(ring), .vibrate_mode(vibrate_mode), .ringer(ringer), .motor(motor)
    );

    q5b_mealy_twos_complement_onehot_review dut_q5b (
        .clk(clk), .areset(q5b_areset), .x(q5b_x), .z(q5b_z)
    );

    task automatic check_bit(input logic actual, input logic expected, input string label);
        if (actual !== expected) begin
            failures = failures + 1;
            $display("FAIL %s: expected=%b actual=%b", label, expected, actual);
        end
    endtask

    task automatic check8(input logic [7:0] actual, input logic [7:0] expected, input string label);
        if (actual !== expected) begin
            failures = failures + 1;
            $display("FAIL %s: expected=%h actual=%h", label, expected, actual);
        end
    endtask

    task automatic check32(input logic [31:0] actual, input logic [31:0] expected, input string label);
        if (actual !== expected) begin
            failures = failures + 1;
            $display("FAIL %s: expected=%h actual=%h", label, expected, actual);
        end
    endtask

    task automatic step_edge(input logic [7:0] next_input);
        logic [7:0] expected;
        begin
            expected = next_input & ~edge_model_previous;
            @(negedge clk);
            edge_in = next_input;
            @(posedge clk);
            #1;
            check8(edge_pulse, expected, "entry 74 sampled 0-to-1 pulse");
            edge_model_previous = next_input;
        end
    endtask

    task automatic step_q8(input logic next_x, input logic expected_z);
        begin
            @(negedge clk);
            q8_x = next_x;
            #1;
            check_bit(q8_z, expected_z, "entry 75 Mealy 101 output");
            @(posedge clk);
            #1;
        end
    endtask

    task automatic step_q5a(input logic next_x);
        logic expected_z;
        begin
            expected_z = q5a_seen_one ? ~next_x : next_x;
            @(negedge clk);
            q5a_x = next_x;
            @(posedge clk);
            #1;
            check_bit(q5a_z, expected_z, "entry 80 Moore serial two's complement");
            if (next_x)
                q5a_seen_one = 1'b1;
        end
    endtask

    task automatic step_capture(input logic [31:0] next_input, input logic next_reset);
        begin
            @(negedge clk);
            capture_in = next_input;
            capture_reset = next_reset;
            @(posedge clk);
            #1;
            if (next_reset)
                capture_model_out = 32'b0;
            else
                capture_model_out = capture_model_out | (capture_model_previous & ~next_input);
            capture_model_previous = next_input;
            check32(capture_out, capture_model_out, "entry 83 sticky 1-to-0 capture");
        end
    endtask

    task automatic step_q5b(input logic next_x);
        logic expected_z;
        begin
            expected_z = q5b_seen_one ? ~next_x : next_x;
            @(negedge clk);
            q5b_x = next_x;
            #1;
            check_bit(q5b_z, expected_z, "entry 85 Mealy serial two's complement");
            check_bit($onehot(dut_q5b.state), 1'b1, "entry 85 one-hot state invariant");
            @(posedge clk);
            #1;
            if (next_x)
                q5b_seen_one = 1'b1;
        end
    endtask

    initial begin
        // Entries 77, 81, 82, and 84 are exhaustively or directly checked combinationally.
        for (i = 0; i < 16; i = i + 1) begin
            gates_in = i[3:0];
            {circuit_a, circuit_b, circuit_c, circuit_d} = i[3:0];
            #1;
            check_bit(gates_and, &gates_in, "entry 77 reduction AND");
            check_bit(gates_or,  |gates_in, "entry 77 reduction OR");
            check_bit(gates_xor, ^gates_in, "entry 77 reduction XOR");
            check_bit(circuit_q, circuit_b | circuit_c, "entry 81 waveform-derived OR");
        end

        for (i = 0; i < 4; i = i + 1) begin
            {ring, vibrate_mode} = i[1:0];
            #1;
            check_bit(ringer, ring & ~vibrate_mode, "entry 84 ringer output");
            check_bit(motor, ring & vibrate_mode, "entry 84 motor output");
            check_bit(ringer & motor, 1'b0, "entry 84 mutual exclusion");
        end

        for (i = 0; i < 200; i = i + 1) begin
            vector_a = $urandom;
            vector_b = $urandom;
            vector_c = $urandom;
            vector_d = $urandom;
            vector_e = $urandom;
            vector_f = $urandom;
            vector_expected = {vector_a, vector_b, vector_c, vector_d, vector_e, vector_f, 2'b11};
            #1;
            check32({vector_w, vector_x, vector_y, vector_z}, vector_expected,
                    "entry 82 30-bit concatenation plus two ones");
        end

        // Prime the unreset previous-sample register, then check multiple sampled transitions.
        repeat (2) @(posedge clk);
        #1;
        edge_model_previous = edge_in;
        step_edge(8'h12);
        step_edge(8'h16);
        step_edge(8'h16);
        step_edge(8'hff);
        step_edge(8'h00);

        // The 101 detector must overlap: 10101 produces two detection pulses.
        @(negedge clk);
        q8_aresetn = 1'b1;
        step_q8(1'b1, 1'b0);
        step_q8(1'b0, 1'b0);
        step_q8(1'b1, 1'b1);
        step_q8(1'b0, 1'b0);
        step_q8(1'b1, 1'b1);
        #2;
        q8_aresetn = 1'b0;
        #1;
        check_bit(q8_z, 1'b0, "entry 75 asynchronous reset assertion");

        // The Moore implementation produces the bit after the sampling edge.
        @(negedge clk);
        q5a_areset = 1'b0;
        step_q5a(1'b0);
        step_q5a(1'b0);
        step_q5a(1'b1);
        step_q5a(1'b0);
        step_q5a(1'b1);
        step_q5a(1'b1);
        step_q5a(1'b0);
        step_q5a(1'b1);

        // Capture bits stay set until synchronous reset, while previous input is sampled every edge.
        step_capture(32'hffff_ffff, 1'b1);
        step_capture(32'hffff_0ff0, 1'b0);
        step_capture(32'hffff_ffff, 1'b0);
        step_capture(32'h0fff_ffff, 1'b0);
        step_capture(32'h0000_0000, 1'b1);
        step_capture(32'h0000_0000, 1'b0);

        // The corrected Mealy implementation uses two genuinely one-hot states.
        @(negedge clk);
        q5b_areset = 1'b0;
        step_q5b(1'b0);
        step_q5b(1'b0);
        step_q5b(1'b1);
        step_q5b(1'b0);
        step_q5b(1'b1);
        step_q5b(1'b1);
        step_q5b(1'b0);
        step_q5b(1'b1);

        if (failures == 0)
            $display("PASS: Chrome-audit follow-up behavior checks passed (entries 74, 75, 77, 80-85).");
        else
            $fatal(1, "FAIL: %0d original-submission review checks failed.", failures);

        $finish;
    end
endmodule
