from myhdl import *
from alu import alu

def alu_convert():
    ds1,ds2,imm,alu_out=[Signal(intbv(0)[8:]) for _ in range(4)]
    unsign,bra,branch=[Signal(bool(0))for _ in range(3)]
    alu_signal=Signal(intbv(0)[5:])
    alu_ins = alu(ds1, ds2, imm,  bra, branch, alu_out, alu_signal)
    return alu_ins
if __name__ == '__main__':
    alu_ins = alu_convert()
    alu_ins.convert(hdl='Verilog', initial_values=True)