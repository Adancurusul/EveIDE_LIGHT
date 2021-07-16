from myhdl import *
@block
def gpr( clk,rst,register_write,rd_r0_mux,rd_r1_mux
          ,ds1_rx,ds2_rx,
          rd_data,cr_data,ds1_data,ds2_data,r6_r7_data):
    '''

    '''
    states_ds1 = enum("r0","r1","r2","r3","r4","r5","r6","r7")
    states_ds2 = enum("r0", "r1", "r2", "r3", "r4", "r5", "r6", "r7")
    states_r_w = enum("r0","r1","r2","r3","r4","r5","r6","r7",encoding='one_hot')
    r0 = Signal(intbv(0)[8:])
    r1 = Signal(intbv(0)[8:])
    r2 = Signal(intbv(0)[8:])
    r3 = Signal(intbv(0)[8:])
    r4 = Signal(intbv(0)[8:])
    r5 = Signal(intbv(0)[8:])
    r6 = Signal(intbv(0)[8:])
    r7 = Signal(intbv(0)[8:])

    @always_seq(clk.posedge,reset = rst)
    def r0_r1_logic():
        if register_write[0]:
            if rd_r0_mux:
                r0.next = cr_data[8:0]
            else :
                r0.next = rd_data
        if register_write[1]:
            if rd_r1_mux:
                r1.next = cr_data[16:8]
            else:
                r1.next = rd_data

        if register_write[2]:
            r2.next = rd_data
        if register_write[3]:
            r3.next = rd_data
        if register_write[4]:
            r4.next = rd_data
        if register_write[5]:
            r5.next = rd_data
        if register_write[6]:
            r6.next = rd_data
        if register_write[7]:
            r7.next = rd_data


    @always_comb
    def ds1_dat_logic():
        if ds1_rx ==states_ds1.r0:
            ds1_data.next = r0
        elif ds1_rx ==states_ds1.r1:
            ds1_data.next = r1

        elif ds1_rx ==states_ds1.r2:
            ds1_data.next = r2
        elif ds1_rx ==states_ds1.r3:
            ds1_data.next = r3
        elif ds1_rx ==states_ds1.r4:
            ds1_data.next = r4
        elif ds1_rx ==states_ds1.r5:
            ds1_data.next = r5
        elif ds1_rx ==states_ds1.r6:
            ds1_data.next = r6
        elif ds1_rx ==states_ds1.r7:
            ds1_data.next = r7
        else :
            ds1_data.next = 0

    @always_comb
    def ds2_data_logic():
        if ds2_rx == states_ds2.r0:
            ds2_data.next = r0
        elif ds2_rx==states_ds2.r1:
            ds2_data.next = r1

        elif ds2_rx==states_ds2.r2:
            ds2_data.next = r2
        elif ds2_rx==states_ds2.r3:
            ds2_data.next = r3
        elif ds2_rx==states_ds2.r4:
            ds2_data.next = r4
        elif ds2_rx==states_ds2.r5:
            ds2_data.next = r5
        elif ds2_rx==states_ds2.r6:
            ds2_data.next = r6
        elif ds2_rx==states_ds2.r7:
            ds2_data.next = r7
        else:
            ds2_data.next = 0

    @always_comb
    def r6_r7_data_logic():
        r6_r7_data[16:8].next = r7
        r6_r7_data[8:0].next = r6



    return instances()



