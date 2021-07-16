from myhdl import *
from lsu import lsu

def lsu_convert():
    r6_r7_data,ds1_data,addr = [Signal(intbv(0)[16:]) for _ in range(3)]
    mem_read,mem_write,mem_ok ,rdata,write,read,rdy = [Signal(bool(0)) for _ in range(7)]
    wdata = Signal(intbv(0)[8:])
    lsu_out = Signal(intbv(0)[8:])
    lsu_ins = lsu (r6_r7_data, ds1_data, mem_read, mem_write, mem_ok, lsu_out, addr, wdata, rdata, write, read, rdy)
    return lsu_ins
if __name__ == '__main__':
    lsu_ins  = lsu_convert()
    lsu_ins.convert(hdl='Verilog')
