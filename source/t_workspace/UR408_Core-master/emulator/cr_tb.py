from myhdl import *
from cr import cr

def cr_convert():
    rst = ResetSignal(1, active=1, isasync=False)
    clk,int0,int1,int2,int3,mem_read,mem_write,mem_ok,branch,cr_write,ret,apc,jmp,bra,main_state = [Signal(bool(0)) for _ in range(15)]
    selector = Signal(intbv(0)[3:])
    #Signal().driven='wire'
    pc_next,branch_offset,r6_r7_data,cr_data = [Signal(intbv(0)[16:]) for _ in range (4)]
    cr_ins =cr( pc_next, branch_offset, r6_r7_data, cr_data,clk, rst, int0, int1, int2, int3, mem_read, mem_write, mem_ok, branch, selector, cr_write, ret, apc, jmp, bra , main_state)   #toVerilog(cr,pc_next, branch_offset, r6_r7_data, cr_data,clk, rst, int0, int1, int2, int3, mem_read, mem_write, mem_ok, branch, selector, cr_write, ret, apc, jmp, bra , main_state)
    return cr_ins
def cr_sim():
    crins = cr_convert()

if __name__ == '__main__':
    cr_ins = cr_convert()
    cr_ins.convert(hdl='Verilog', initial_values=True)