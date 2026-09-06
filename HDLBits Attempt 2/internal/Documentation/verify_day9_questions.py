from pathlib import Path
import sys, subprocess
sys.path.append(r'C:/Users/kapil/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/Lib/site-packages')
import fitz
ROOT=Path(__file__).resolve().parents[2]; TMP=ROOT/'internal/tmp/day9_questions_20260907'
def sim(name,source,tb):
 t=TMP/(name+'_tb.sv');t.write_text(tb)
 exe=TMP/(name+'.vvp')
 subprocess.run(['iverilog','-g2012','-s','tb','-o',str(exe),str(TMP/source),str(t)],check=True)
 print(subprocess.run(['vvp',str(exe)],check=True,capture_output=True,text=True).stdout)
sim('latches','always_if2.v',r'''
module tb;
reg hot, arrived, empty; wire off, drive;
reg buggy;
top_module dut(hot,off,arrived,empty,drive);
always @(*) if (~arrived) buggy=~empty;
integer i;
initial begin
 for(i=0;i<8;i=i+1) begin
  {hot,arrived,empty}=i; #1;
  if(off !== hot || drive !== (!arrived && !empty)) $fatal(1,"truth table");
 end
 arrived=0;empty=0;hot=1;#1;
 if(drive!==1 || buggy!==1 || off!==1) $fatal(1,"initial drive");
 arrived=1;hot=0;#1;
 if(drive!==0 || buggy!==1 || off!==0) $fatal(1,"arrival hold");
 empty=1;#1;
 if(drive!==0 || buggy!==1) $fatal(1,"held value changed");
 $display("PASS: 8 input combinations, shutdown recovery and arrival latch trace");
 $finish;
end
endmodule
''')
sim('sequence','fsmseq_clean.v',r'''
module tb;
reg clk=0,reset=1,data=0;
wire found;
top_module dut(clk,reset,data,found);
integer stream,i;reg [3:0] hist;reg expected;
task tick; begin #1;clk=1;#1;clk=0;#1;end endtask
initial begin
 for(stream=0;stream<4096;stream=stream+1) begin
  reset=1;tick;hist=0;expected=0;
  if(found!==0) $fatal(1,"reset");
  reset=0;
  for(i=11;i>=0;i=i-1) begin
   data=(stream>>i)&1;hist={hist[2:0],data};
   if(i<=8 && hist==4'b1101) expected=1;
   tick;
   if(found!==expected) $fatal(1,"stream %d bit %d",stream,i);
  end
 end
 // Last stream may not detect: force 1101, then reset between edges.
 reset=1;tick;reset=0;
 data=1;tick;data=1;tick;data=0;tick;data=1;tick;
 if(found!==1) $fatal(1,"detect");
 reset=1;#1;if(found!==1) $fatal(1,"reset became asynchronous");
 tick;if(found!==0) $fatal(1,"synchronous reset failed");
 $display("PASS: all 4096 twelve-bit streams, sticky detection and synchronous reset");
 $finish;
end
endmodule
''')
pdf=ROOT/'HDLBits_Day9_QA_Latches_and_Sequence_FSM.pdf'
d=fitz.open(pdf);print('PDF pages',len(d))
assert len(d)==5
for i,pg in enumerate(d):
 text=pg.get_text();assert len(text)>300
 for b in pg.get_text('blocks'):
  assert b[0]>=35 and b[2]<=pg.rect.width-35,(i,b)
 subprocess.run(['pdftoppm','-f',str(i+1),'-l',str(i+1),'-scale-to','1150','-png','-singlefile',str(pdf),str(TMP/f'pdf_page_{i+1}')],check=True,capture_output=True)
print('Rendered all five pages')
