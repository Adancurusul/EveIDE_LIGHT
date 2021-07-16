from myhdl import *
@block
def cr(clk,rst,int0,int1,int2,int3,mem_read,mem_write,mem_ok,branch,status_sel,ie_sel,
       epc_sel,cpc_sel,temp_sel,tcev0_sel,tcev1_sel,tcev2_sel,tcev3_sel,cr_write,ret,apc,jmp,bra
       ,main_state,pc_next,branch_offset,r6_r7_data,cr_data):
    '''

    :param clk: 1 in clk
    :param rst: 1 in rst
    :param int0: 1 in interrupt
    :param int1: 1 in interrupt
    :param int2: 1 in interrupt
    :param int3: 1 in interrupt
    :param mem_read: 1 in memory read
    :param mem_write: 1 in memory write
    :param mem_ok: 1 in memory ok
    :param branch:  1 in branch
    :param status_sel:  1 in status selector
    :param ie_sel: 1 in ie selector
    :param epc_sel: 1 in epc selector
    :param cpc_sel: 1 in cpc selector
    :param temp_sel: 1 in temp selector
    :param tcev0_sel: 1 in tcev selector
    :param tcev1_sel:1 in tcev selector
    :param tcev2_sel:1 in tcev selector
    :param tcev3_sel:1 in tcev selector
    :param cr_write:1 in cr write
    :param ret: 1 in return
    :param apc: 1 in apc
    :param jmp: 1 in jmp
    :param bra: 1 in branch if
    :param main_state: 1 out main state
    :param pc_next: 16 out program counter next
    :param branch_offset: 16 in branch offset
    :param r6_r7_data: 16 in  data from r6 and r7 (pointer
    :param cr_data: 16 out cr register data
    :return:
    '''
    CPC=Signal(intbv(0)[16:])
    TEMP=Signal(intbv(0)[16:])
    TVEC0=Signal(intbv(0)[16:])
    TVEC1=Signal(intbv(0)[16:])
    TVEC2=Signal(intbv(0)[16:])
    TVEC3=Signal(intbv(0)[16:])
    EPC=Signal(intbv(0)[16:])
    PC=Signal(intbv(0)[16:])
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


    @always_seq(clk, reset= rst)
    def cr_logic():
      #main_state
      if not main_state :
         if mem_read or mem_write:
            main_state.next = intbv(bool(1))
         else:
            main_state.next = intbv(bool(0))
      elif main_state:
         if mem_ok:
            main_state.next = intbv(bool(0))
         else:
            main_state.next = intbv(bool(1))
      #status
      if  int_acc:
         GIE.next=0
      elif ret :
         GIE.next=PGIE
      
      elif status_sel and cr_write :
         GIE.next = r6_r7_data[0]
      
      if int_acc :
         PGIE.next = GIE
      elif status_sel and cr_write:
         PGIE.next = r6_r7_data[1]
      #ie
      if ie_sel and cr_write :
         IE0.next = r6_r7_data[0]
         IE1.next = r6_r7_data[1]
         IE2.next = r6_r7_data[2]
         IE3.next = r6_r7_data[3]
      #epc
      if int_acc:
         EPC.next = PC
      elif epc_sel and cr_write:
         EPC.next = r6_r7_data

      #cpc
      if int_acc:
         CPC.next  = 0
      elif cpc_sel and cr_write:
         CPC.next = r6_r7_data 
      elif int_acc:
         CPC.next = PC

      #pc
      if int_acc:
         PC.next = tvec + 1
      elif ret :
         PC.next = EPC+1
      elif jmp:
         PC.next = r6_r7_data+1
      elif branch:
         PC.next = PC+branch_offset+1
      else :
         if ((not main_state) or not (mem_read or mem_write)) or (main_state and mem_ok):
            PC.next = PC+intbv(0b11111111)[8:]
         else :
            PC.next = PC
      
      #tvec0
      if tcev0_sel and cr_write:
         TVEC0.next = r6_r7_data
      
      #tvec1
      if tcev1_sel and cr_write:
         TVEC1.next = r6_r7_data

      #tvec2
      if tcev2_sel and cr_write:
         TVEC2.next = r6_r7_data

      #tvec3
      if tcev3_sel and cr_write:
         TVEC3.next = r6_r7_data
   
    @always_comb
    def int_logic():
      int0_acc.next = GIE & int0 & IE0
      int1_acc.next = GIE & int1 & IE1
      int2_acc.next = GIE & int2 & IE2
      int3_acc.next = GIE & int3 & IE3
      int_acc.next = not (bra|jmp|ret|mem_read|mem_write) and (int0_acc or int1_acc or int2_acc or int3_acc)

    @always_comb
    def comb_logic() :
       if int0_acc:
          tvec.next = TVEC0
       elif int1_acc :
          tvec.next = TVEC1
       elif int2_acc:
           tvec.next = TVEC2
       else:
           tvec.next = TVEC3

       if ret:





