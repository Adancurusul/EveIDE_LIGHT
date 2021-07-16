from myhdl import *
pc_next,branch_offset,r6_r7_data,cr_data = [Signal(intbv(0))[16:] for _ in range (4)]
selector = Signal(intbv(0)[9:])

@block
def test(pc_next,branch_offset,r6_r7_data,cr_data,selector):
    states = enum('status', 'ie', 'epc', 'cpc', 'temp', 'tvec0', 'tvec1', 'tvec2', 'tvec3', encoding='one_hot')


    CPC = Signal(intbv(0)[16:])
    TEMP = Signal(intbv(0)[16:])
    TVEC0 = Signal(intbv(0)[16:])
    TVEC1 = Signal(intbv(0)[16:])
    TVEC2 = Signal(intbv(0)[16:])
    TVEC3 = Signal(intbv(0)[16:])
    EPC = Signal(intbv(0)[16:])
    PC = Signal(intbv(0)[16:])
    GIE = Signal(bool(0))
    PGIE = Signal(bool(0))
    IE0 = Signal(bool(0))
    IE1 = Signal(bool(0))
    IE2 = Signal(bool(0))
    IE3 = Signal(bool(0))
    int_acc = Signal(bool(0))
    tvec = Signal(intbv(0)[16:])
    int0_acc = Signal(bool(0))
    int1_acc = Signal(bool(0))
    int2_acc = Signal(bool(0))
    int3_acc = Signal(bool(0))
    @always_comb
    def comb_logic():
        if int0_acc:
            tvec.next = TVEC0
        elif int1_acc:
            tvec.next = TVEC1
        elif int2_acc:
            tvec.next = TVEC2
        else:
            tvec.next = TVEC3



        if selector == states.status:
            cr_data[16:2].next = intbv(0)[14:]
            cr_data[1].next = PGIE
            cr_data[0].next = GIE
        elif selector == states.ie:
            cr_data[16:4].next = intbv(0)[12:]
            cr_data[3].next = IE3
            cr_data[2].next = IE2
            cr_data[1].next = IE1
            cr_data[0].next = IE0
        elif selector == states.epc:
            cr_data.next = EPC
        elif selector == states.cpc:
            cr_data.next = CPC
        elif selector == states.tvec0:
            cr_data.next = TVEC0
        elif selector == states.tvec1:
            cr_data.next = TVEC1
        elif selector == states.tvec2:
            cr_data.next = TVEC2
        elif selector == states.tvec3:
            cr_data.next = TVEC3

    return instances()


in16=Signal(intbv(0))[2:]
out16=Signal(intbv(0))[2:]
@block
def test2(in16,out16):

    @always_comb
    def test2_logic():
        TVEC0 = Signal(intbv(0)[2:])
        if in16:
            out16 = TVEC0

    return instances()

#test2(in16,out16).convert(hdl='Verilog')


#test(pc_next,branch_offset,r6_r7_data,cr_data,selector).convert(hdl='Verilog')


@block
def single_port_ram(clk, we, addr, din, dout, addr_width=2, data_width=3) :
    ram_single_port = [Signal(intbv(0)[addr_width:0])
                for i in range(data_width)]

    @always(clk.posedge)
    def write_logic():
        """ write data to address 'addr' """
        if we == 1 :
            ram_single_port[addr].next = din

    @always_comb
    def read_logic():
        """ read data from address 'addr' """
        dout.next = ram_single_port[addr]

    return instances()

def main():
    addr_width = 16
    data_width = 16
    clk = Signal(bool(0))
    we = Signal(bool(0))
    addr = Signal(intbv(0)[addr_width:0])
    din = Signal(intbv(0)[data_width:0])
    dout = Signal(intbv(0)[data_width:0])

    single_port_ram_verilog = single_port_ram(clk, we, addr,
                din, dout, addr_width, data_width)

    single_port_ram_verilog.convert(hdl="Verilog", initial_values=True)

if __name__ == '__main__' :
    main()