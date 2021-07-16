from myhdl import *
from id import id
@block
def id_invert():
    ins,branch_offset = [Signal(intbv(0)[16:]) for _ in range(2)]
    imm,register_write = [Signal(intbv(0)[8:]) for _ in range(2) ]
    alu_signal = Signal(intbv(0)[4:])
    selector,ds1_rx,ds2_rx = [Signal(intbv(0)[3:]) for _ in range(3)]
    rd_r1_mux,rd_r0_mux,cr_write,mem_read,mem_write,jmp,ret,apc,\
    rd_mux0,rd_mux1,bra=[Signal(bool(0)) for _ in range(11)]
    id_ins = id(ins, alu_signal, mem_read, mem_write, register_write, rd_r0_mux, rd_r1_mux
       , ds1_rx, ds2_rx, rd_mux0, rd_mux1,
       cr_write, selector, imm, branch_offset, bra, ret, apc, jmp)
    return id_ins

if __name__ == '__main__':
    ins = id_invert()
    ins.convert(hdl='Verilog',initial_values=True)