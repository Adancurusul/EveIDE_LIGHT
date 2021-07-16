from myhdl import *
from top import top

def top_invert():
    clk = Signal(bool(0))
    rst = ResetSignal(1, active=1, isasync=False)
    write = Signal(bool(0))
    read = Signal(bool(0))
    rdy = Signal(bool(0))
    pc = Signal(intbv(0)[16:])
    ins = Signal(intbv(0)[16:])
    addr = Signal(intbv(0)[16:])
    wdata = Signal(intbv(0)[8:])
    rdata = Signal(intbv(0)[8:])
    int0 = Signal(bool(0))
    int1 = Signal(bool(0))
    int2 = Signal(bool(0))
    int3 = Signal(bool(0))
    top_ins = top(clk,rst,write,read,rdy,pc,ins,addr,wdata,rdata,int0,int1,int2,int3)
    return top_ins

if __name__ == '__main__':
    top_ins = top_invert()
    top_ins.convert(hdl='Verilog', initial_values=True)