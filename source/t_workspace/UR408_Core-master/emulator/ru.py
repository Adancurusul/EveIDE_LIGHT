from myhdl import *
 @block
 def ru(clk,rst,int0,int1,int2,int3,mem_read,mem_write,mem_ok,r0_write,r1_write,r2_write,r3_write,r4_write,r5_write,r6_write,r7_write,
        rd_mux0,rd_mux1,rd_r0_mux,rd_r1_mux,selector,cr_write,ds1_r0,ds1_r1,ds1_r2,ds1_r3,ds1_r4,ds1_r5,ds1_r6,ds1_r7,
        ds2_r0,ds2_r1,ds2_r2,ds2_r3,ds2_r4,ds2_r5,ds2_r6,ds2_r7,branch_offset,ret,apc,jmp,bra,branch,rd_data,pc_next,ds1_data,ds2_data,r6_r7_data):
     '''

     :param clk: 1 in
     :param rst:  1 in
     :param int0: 1 in
     :param int1:
     :param int2:
     :param int3:
     :param mem_read: 1 in
     :param mem_write: 1 in
     :param mem_ok: 1 in
     :param r0_write: 1 in
     :param r1_write:
     :param r2_write:
     :param r3_write:
     :param r4_write:
     :param r5_write:
     :param r6_write:
     :param r7_write:
     :param rd_mux0:
     :param rd_mux1:
     :param rd_r0_mux:
     :param rd_r1_mux:
     :param selector: 9 in
     :param cr_write: 1 in
     :param ds1_r0: 1 in
     :param ds1_r1:
     :param ds1_r2:
     :param ds1_r3:
     :param ds1_r4:
     :param ds1_r5:
     :param ds1_r6:
     :param ds1_r7:
     :param ds2_r0:
     :param ds2_r1:
     :param ds2_r2:
     :param ds2_r3:
     :param ds2_r4:
     :param ds2_r5:
     :param ds2_r6:
     :param ds2_r7:
     :param branch_offset: 16 in
     :param ret: 1 in
     :param apc: 1 in
     :param jmp: 1 in
     :param bra: 1 in
     :param branch: 1 in
     :param rd_data: 8 in
     :param pc_next: 16 out
     :param ds1_data: 8 out
     :param ds2_data: 8 out
     :param r6_r7_data: 16 out
     :return:
     '''
