module top_module ();
    reg [1:0] in;
    wire out;
    integer i;

    andgate dut_instance (
        .in(in),
        .out(out)
    );

    initial begin
        for (i = 0; i < 4; i = i + 1) begin
            in = i[1:0];
            #10;
        end
    end
endmodule
