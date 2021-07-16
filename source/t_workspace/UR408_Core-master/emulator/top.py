from myhdl import *
from alu import alu
from cr import cr
from gpr import gpr
from id import  id
from lsu import lsu

@block
def top(clk,rst,write,read,rdy,pc,ins,addr,wdata,rdata,int0,int1,int2,int3):
    '''
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
    '''
    imm = Signal(intbv(0)[8:])
    alu_out = Signal(intbv(0)[8:])
    rd_data = Signal(intbv(0)[8:])
    lsu_out = Signal(intbv(0)[8:])

    r6_r7_data = Signal(intbv(0)[16:])
    branch_offset = Signal(intbv(0)[16:])

    ds1_data = Signal(intbv(0)[8:])
    ds2_data = Signal(intbv(0)[8:])

    rd_mux1 = Signal(bool(0))
    rd_mux0 = Signal(bool(0))

    register_write = Signal(intbv(0)[8:])
    alu_signal = Signal(intbv(0)[4:])
    selector= Signal(intbv(0)[3:])
    ds1_rx=Signal(intbv(0)[3:])
    ds2_rx = Signal(intbv(0)[3:])

    rd_r1_mux = Signal(bool(0))
    rd_r0_mux = Signal(bool(0))
    cr_write = Signal(bool(0))
    mem_read = Signal(bool(0))
    mem_write = Signal(bool(0))
    jmp =Signal(bool(0))
    ret = Signal(bool(0))
    apc = Signal(bool(0))
    bra = Signal(bool(0))

    pc_next = Signal(intbv(0)[16:])
    cr_data = Signal(intbv(0)[16:])

    mem_ok = Signal(bool(0))
    branch = Signal(bool(0))
    main_state = Signal(bool(0))

    @always_comb
    def rd_data_logic():
        if rd_mux1:
            if rd_mux0:
                rd_data.next = imm
            else:
                rd_data.next = lsu_out
        else:
            rd_data.next = alu_out

    id_instance = id(ins, alu_signal, mem_read, mem_write, register_write, rd_r0_mux, rd_r1_mux , ds1_rx, ds2_rx, rd_mux0, rd_mux1, cr_write, selector, imm, branch_offset, bra, ret, apc, jmp)

    cr_instance =cr( pc, branch_offset, r6_r7_data, cr_data,clk, rst, int0, int1, int2, int3, mem_read, mem_write, mem_ok, branch, selector, cr_write, ret, apc, jmp, bra , main_state)   #toVerilog(cr,pc_next, branch_offset, r6_r7_data, cr_data,clk, rst, int0, int1, int2, int3, mem_read, mem_write, mem_ok, branch, selector, cr_write, ret, apc, jmp, bra , main_state)

    alu_instance = alu(ds1_data, ds2_data, imm,  bra, branch, alu_out, alu_signal)

    lsu_instance = lsu (r6_r7_data, ds1_data, mem_read, mem_write, mem_ok, lsu_out, addr, wdata, rdata, write, read, rdy)

    gpr_instance = gpr(clk,rst,register_write,rd_r0_mux,rd_r1_mux,ds1_rx,ds2_rx,rd_data,cr_data,ds1_data,ds2_data,r6_r7_data)

    return instances()