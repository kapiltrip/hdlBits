module conway_reference_tb;
    reg clk=0, load=0;
    reg [255:0] data=0;
    wire [255:0] q;
    reg [255:0] seed, expected, held;
    integer checks=0, pattern, bitno, dr, dc, idx, trial, generation;
    top_module dut(clk, load, data, q);

    // Independent flat-index model with signed coordinate offsets.
    function automatic [255:0] reference(input [255:0] board);
        integer k, dy, dx, nr, nc, n;
        begin
            reference = 0;
            for(k=0; k<256; k=k+1) begin
                n=0;
                for(dy=-1; dy<=1; dy=dy+1)
                    for(dx=-1; dx<=1; dx=dx+1)
                        if(dy!=0 || dx!=0) begin
                            nr=(k/16+dy+16)%16;
                            nc=(k%16+dx+16)%16;
                            n=n+board[nr*16+nc];
                        end
                reference[k]=(n==3) || ((n==2) && board[k]);
            end
        end
    endfunction

    task tick(input [255:0] want);
        begin
            #2; clk=1; #1;
            if(q !== want) $fatal(1,"Mismatch at check %0d: got %h expected %h",checks,q,want);
            checks=checks+1;
            clk=0; #1;
        end
    endtask
    task load_seed(input [255:0] s);
        begin
            load=1; data=s;
            tick(s); // load overrides any combinational evolution
            load=0;
        end
    endtask
    task evolve;
        begin
            expected=reference(q);
            tick(expected);
        end
    endtask

    initial begin
        load_seed(0); evolve();
        load_seed({256{1'b1}}); evolve();
        if(q !== 0) $fatal(1,"Dense board did not die");
        load_seed(1); evolve();
        if(q !== 0) $fatal(1,"Isolated cell survived");
        seed=(256'b1<<85)|(256'b1<<86)|(256'b1<<101)|(256'b1<<102);
        load_seed(seed); evolve(); evolve();
        if(q !== seed) $fatal(1,"Block changed");
        load_seed(7); evolve();
        if(q !== ((256'b1<<241)|(256'b1<<1)|(256'b1<<17))) $fatal(1,"Seam blinker wrong");
        evolve();
        if(q !== 7) $fatal(1,"Blinker period wrong");
        // Both center states and every combination of its eight neighbors.
        for(pattern=0; pattern<512; pattern=pattern+1) begin
            seed=0; seed[0]=(pattern>>8)&1; bitno=0;
            for(dr=-1; dr<=1; dr=dr+1)
                for(dc=-1; dc<=1; dc=dc+1)
                    if(dr!=0 || dc!=0) begin
                        idx=((dr+16)%16)*16+(dc+16)%16;
                        seed[idx]=(pattern>>bitno)&1;
                        bitno=bitno+1;
                    end
            load_seed(seed); evolve();
        end
        for(trial=0; trial<100; trial=trial+1) begin
            seed={$random,$random,$random,$random,$random,$random,$random,$random};
            load_seed(seed);
            for(generation=0; generation<5; generation=generation+1) evolve();
        end
        held=q; data=~q; load=1; #2;
        if(q !== held) $fatal(1,"q changed without a rising edge");
        tick(data); data=7; tick(data); // successive high-load edges
        $display("PASS: %0d post-edge full-grid checks; 512 local patterns, 100 random five-generation runs, boundary and load tests",checks);
        $finish;
    end
endmodule
