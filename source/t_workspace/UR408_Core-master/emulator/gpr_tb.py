from myhdl import *
from gpr import gpr

def gpr_convert():
    rst = ResetSignal(1, active=1, isasync=False)
    clk,   rd_r0_mux, rd_r1_mux=   [Signal(bool(0)) for _ in range(3)]
    rd_data,ds1_data,ds2_data= [Signal(intbv(0)[8:]) for _ in range(3)]
    cr_data,r6_r7_data = [Signal(intbv(0)[16:]) for _ in range(2)]
    register_write = Signal(intbv(0)[8:])
    ds1_rx, ds2_rx = [Signal(intbv(0)[3:]) for i in range(2)]
    gpr_ins = gpr(clk,rst,register_write,rd_r0_mux,rd_r1_mux
          ,ds1_rx,ds2_rx,
          rd_data,cr_data,ds1_data,ds2_data,r6_r7_data)
    return gpr_ins
if __name__ == '__main__':
    gpr_ins = gpr_convert()
    gpr_ins.convert(hdl = 'Verilog')