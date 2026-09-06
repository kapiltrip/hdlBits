"""Run the saved tests and check examples extracted from the revised PDFs."""
from pathlib import Path
import subprocess, re, json, shutil
import fitz
ROOT=Path(__file__).resolve().parents[2]
WORK=ROOT/'internal/tmp/document_review_20260907'

def readpage(name,pn):
    with fitz.open(ROOT/name) as d:return d[pn-1].get_text()
def module(text,new):
    return re.search(r'module top_module\s*\([\s\S]+?endmodule',text).group(0).replace('top_module',new,1)
def run(name,sources):
    exe=WORK/(name+'.vvp')
    build=subprocess.run(['iverilog','-g2012','-o',str(exe)]+[str(p) for p in sources],capture_output=True,text=True)
    assert build.returncode==0,build.stderr
    sim=subprocess.run(['vvp',str(exe)],capture_output=True,text=True)
    if name=='hdlc_timing':
        assert sim.returncode==0 and 'PRE,5,0,5,1,0,0' in sim.stdout and 'POST,5,0,0,0,0,0' in sim.stdout
        sim.stdout='PASS: original Mealy discard pulse appears before the terminating-zero edge and disappears after it.'
    else:
        assert sim.returncode==0 and 'PASS' in sim.stdout and 'FAIL' not in sim.stdout,sim.stdout+sim.stderr
    return {'name':name,'result':sim.stdout.strip(),'compiler_warnings':build.stderr.strip()}

results=[]
for name,source in [('day5','day5_original_submission_selfcheck.sv'),('q3fsm','day6_q3fsm_selfcheck.sv'),('nonfsm','day6_nonfsm_selfcheck.sv')]:
    results.append(run(name,[ROOT/'internal/Verification'/source]))
results.append(run('serial_loop',[ROOT/'internal/tmp/pdfs/serial_loop_semantics_tb.sv']))
results.append(run('hdlc',[ROOT/'internal/Discussion Drafts/fsm_hdlc_working_moore.v',ROOT/'internal/tmp/pdfs/fsm_hdlc_selfcheck_tb.sv']))
results.append(run('hdlc_timing',[ROOT/'internal/Discussion Drafts/fsm_hdlc_discussion.v',ROOT/'internal/tmp/pdfs/fsm_hdlc_timing_tb.sv']))

vector=module(readpage('HDLBits_Day4_Questions_Vector_DFF_PS2.pdf',2),'reverse_bytes')
ps2=module(readpage('HDLBits_Day4_Questions_Vector_DFF_PS2.pdf',5),'ps2_parser')
clock=readpage('HDLBits_Day8_QA_Wire_Reg_and_Shift_Reset.pdf',5)
clock=clock[clock.index('always @(posedge clk)'):clock.index('Worked boundary transitions')]
mux=readpage('HDLBits_Combined_Questions_and_Day2_Review.pdf',7)
mask=re.search(r'assign out = \(\{8[\s\S]+?;',mux).group(0)
fall=readpage('HDLBits_Combined_Questions_and_Day2_Review.pdf',8)
fall=fall[fall.index('always @(posedge clk'):fall.index('// While in a falling state')]
src='`timescale 1ns/1ps\n'+vector+'\n'+ps2+'\n'
src+='module clock_review(input clk,reset,ena,output reg [7:0] second,minutes,hour,output reg pmreg);\n'+clock+'\nendmodule\n'
src+='module mux_review(input sel,input [7:0] a,b,output [7:0] out);\n'+mask+'\nendmodule\n'
src+='module fall_review(input clk,areset,ground,output reg [4:0] count);\n'+fall+'\nendmodule\n'
src+=r'''
module tb;
reg clk=0, reset=1,ena=1;
reg [31:0] vin;wire [31:0] vout;
reg [7:0] pin; wire [23:0] pout;wire done;
reg sel;reg [7:0] a,b;wire [7:0] mout;
reg areset=0,ground=1;wire [4:0] count;
wire [7:0] second,minutes,hour;wire pmreg;
integer i,j,k,h,m,s,n,fh;reg [23:0] packet;
reverse_bytes v(vin,vout);
ps2_parser p(clk,pin,reset,pout,done);
clock_review c(clk,reset,ena,second,minutes,hour,pmreg);
mux_review mx(sel,a,b,mout);
fall_review f(clk,areset,ground,count);
task tick;begin #2;clk=1;#1;clk=0;#1;end endtask
function [7:0] bcd(input integer v);bcd=((v/10)<<4)|(v%10);endfunction
initial begin
 pin=0;vin=0;sel=0;a=0;b=0;
 for(i=0;i<256;i=i+1) for(j=0;j<256;j=j+1) begin
   a=i;b=j;sel=0;#1;if(mout!==a)$fatal(1,"mux sel0");
   sel=1;#1;if(mout!==b)$fatal(1,"mux sel1");
 end
 for(i=0;i<1000;i=i+1)begin
  vin=$random;#1;if(vout!=={vin[7:0],vin[15:8],vin[23:16],vin[31:24]})$fatal(1,"byte reversal");
 end
 tick();reset=0;
 for(i=0;i<100;i=i+1)begin
  packet=$random;packet[19]=1;pin=packet[23:16];tick();if(done)$fatal(1,"PS2 byte1");
  pin=packet[15:8];tick();if(done)$fatal(1,"PS2 byte2");
  pin=packet[7:0];tick();if(!done||pout!==packet)$fatal(1,"PS2 byte3");
 end
 pin=0;tick();if(done)$fatal(1,"PS2 stuck done");tick();if(done)$fatal(1,"PS2 false start");
 reset=1;ena=0;tick();reset=0;
 if({hour,minutes,second,pmreg}!=={8'h12,8'h00,8'h00,1'b0})$fatal(1,"clock reset priority");
 tick();if(second!==0)$fatal(1,"disabled clock");ena=1;
 for(n=1;n<=86400;n=n+1)begin
  tick();s=n%60;m=(n/60)%60;h=(n/3600)%24;fh=h%12;if(fh==0)fh=12;
  if(second!==bcd(s)||minutes!==bcd(m)||hour!==bcd(fh)||pmreg!==(h>=12))$fatal(1,"clock time %0d",n);
 end
 for(i=19;i<=70;i=i+1)begin
  areset=1;#1;areset=0;ground=0;
  for(j=0;j<i;j=j+1)tick();
  if((count>20)!==(i>20))$fatal(1,"fall boundary %0d",i);
  if(count!==((i>21)?21:i))$fatal(1,"fall saturation");
  ground=1;tick();if(count!==0)$fatal(1,"landing reset");
 end
 $display("PASS: extracted PDF code: 131072 mux selections, 1000 byte reversals, 100 back-to-back PS2 packets, full 86400-second clock cycle, and 19-70-cycle falls.");
 $finish;
end
endmodule
'''
path=WORK/'extracted_pdf_examples.sv';path.write_text(src,encoding='utf-8')
results.append(run('extracted_pdf_examples',[path]))
# The parity equation should accept exactly one parity bit for each data byte.
for value in range(256):
    expected=1^(value.bit_count()%2)
    assert ((value.bit_count()+expected)%2)==1
    assert ((value.bit_count()+(expected^1))%2)==0
results.append({'name':'parity','result':'PASS: odd-parity arithmetic for all 256 data bytes and both parity choices; no complete serial receiver rerun claimed.'})
(WORK/'simulation_results.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
for r in results: print(r['name']+': '+r['result'])
