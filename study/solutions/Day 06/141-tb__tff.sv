module top_module ();
    reg clk;
    reg reset;
    reg t;
    wire q;

    tff dut_instance (
        .clk(clk),
        .reset(reset),
        .t(t),
        .q(q)
    );

    initial begin
        clk = 1'b0;
        forever #5 clk = ~clk;
    end

    initial begin
        reset = 1'b1;
        t = 1'b0;
        #10 begin
            reset = 1'b0;
            t = 1'b1;
        end
    end
endmodule
