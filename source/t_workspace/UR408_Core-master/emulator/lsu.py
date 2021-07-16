from myhdl import *
@block
def lsu(r6_r7_data,ds1_data,mem_read,mem_write,mem_ok,lsu_out,addr,wdata,rdata,write,read,rdy):
    '''

    :param r6_r7_data: 16 in
    :param ds1_data:  16 in
    :param mem_read: 1 in
    :param mem_write: 1 in
    :param mem_ok: 1 out
    :param lsu_out: 8 out
    :param addr: 16 out
    :param wdata:  8 in
    :param rdata: 1 out
    :param write: 1 out
    :param read: 1 out
    :param rdy: 1 in
    :return:
    '''
    @always_comb
    def main_logic():
        write.next = mem_write
        read.next = mem_read
        mem_ok.next = rdy
        lsu_out.next = rdata
    @always_comb
    def logic_2():
        if mem_read|mem_write:
            addr.next = r6_r7_data
            wdata.next = ds1_data
        else:
            addr.next = 0
            wdata.next = 0
    return  instances()
