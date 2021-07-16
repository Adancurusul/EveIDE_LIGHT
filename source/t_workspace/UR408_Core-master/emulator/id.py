from myhdl import *

@block
def id(ins,alu_signal,mem_read,mem_write,register_write,rd_r0_mux,rd_r1_mux
          ,ds1_rx,ds2_rx,rd_mux0,rd_mux1,
        cr_write,selector,imm,branch_offset,bra,ret,apc,jmp):
    '''
    ins in 16
    alu_signal out 4
    mem_read out 1
    mem_write out 1
    register_write out 8
    rd_r0_mux out 1
    rd_r1_mux out 1
    selector out 3
    cr_write out 1
    ds1_rx out 3
    ds2_rx out 3
    imm out 8
    branch_offset out 16
    jmp out 1
    ret out 1
    apc out 1
    bra out 1



    '''
    #opcode_r = Signal(intbv(0)[2:])
    #opcode_b = Signal(intbv(1)[2:])
    #opcode_sys = Signal(intbv(2)[2:])
    opcode_ls = Signal(intbv(3)[2:])
    funct4_0 = Signal(intbv(0)[4:])
    funct4_1 = Signal(intbv(1)[4:])
    funct4_2 = Signal(intbv(2)[4:])
    funct4_3 = Signal(intbv(3)[4:])
    funct4_4 = Signal(intbv(4)[4:])
    funct4_5 = Signal(intbv(5)[4:])
    #funct4_6 = Signal(intbv(6)[4:])
    #funct4_7 = Signal(intbv(7)[4:])
    funct4_8 = Signal(intbv(8)[4:])
    funct4_9 = Signal(intbv(9)[4:])
    #funct4_10 = Signal(intbv(10)[4:])
    #funct4_11 = Signal(intbv(11)[4:])
    #funct4_12 = Signal(intbv(12)[4:])
    #funct4_13 = Signal(intbv(13)[4:])
    #funct4_14 = Signal(intbv(14)[4:])
    #funct4_15 = Signal(intbv(15)[4:])
    #states_alu = enum('add0', 'sub0', 'and0', 'or0', 'xor0', 'sr0', 'sl0', 'sra0', 'slt0', 'sltu0', 'eq0', 'neq0')
    states_opcode = enum("r","b","sys","ls")
    states_rd = enum("a","b","c","d","e","f","g","h")
    ins20 = Signal(intbv(0)[3:])
    ins96 = Signal(intbv(0)[3:])
    @always_comb
    def trans_logic():
        ins20.next = ins[2:0]
        ins96.next = ins[9:6]
    @always_comb
    def id_logic():
        if ins20==states_opcode.r:
            #alu_signal
            alu_signal.next = ins[6:2]
            #register_write signal 1
            register_write.next = ins[9:6]
        else:
            alu_signal.next = 0
            # register_write signal 1
            register_write.next = 0



        if ins20==states_opcode.b:
            bra.next = bool(1)
        else:
            bra.next = bool(0)
        if ins20 == states_opcode.sys:
            register_write[0].next = ins[6:2]==funct4_4
            register_write[1].next = ins[6:2] == funct4_4
            rd_r0_mux.next=ins[6:2] == funct4_4
            rd_r1_mux.next=ins[6:2] == funct4_4
            cr_write.next =ins[6:2] == funct4_3
            #special
            jmp.next = (ins[6:2]==funct4_0 or ins[6:2] ==funct4_2)
            apc.next = (ins[6:2]==funct4_0 or ins[6:2]==funct4_1)
            ret.next = (ins[6:2]==funct4_5)
        else:
            register_write[0].next = bool(0)
            register_write[1].next = bool(0)
            rd_r0_mux.next = bool(0)
            rd_r1_mux.next = bool(0)
            cr_write.next = bool(0)
            # special
            jmp.next = bool(0)
            apc.next = bool(0)
            ret.next = bool(0)


        if ins20 == states_opcode.ls:
            #mem
            mem_read.next = (ins[6:2] == funct4_8)
            mem_write.next = (ins[6:2] == funct4_9)
            #register_write signal 2
            #register_write[0].next = ((ins[9:6]==funct4_9)|(ins[6:2]==funct4_0))&(ins[9:6]==0)
            if (ins[9:6]==funct4_9)|(ins[6:2]==funct4_0):
                if ins96==states_rd.a:
                    register_write[0].next = 1
                elif ins96 == states_rd.b:
                    register_write[1].next = 1

                elif ins96 == states_rd.c:
                    register_write[2].next = 1
                elif ins96 == states_rd.d:
                    register_write[3].next = 1
                elif ins96 == states_rd.e:
                    register_write[4].next = 1
                elif ins96 == states_rd.f:
                    register_write[5].next = 1
                elif ins96 == states_rd.g:
                    register_write[6].next = 1
                elif ins96 == states_rd.h:
                    register_write[7].next = 1
                else :
                    register_write.next = 0
            else:
                register_write.next = 0
        else :
            mem_read.next = bool(0)
            mem_write.next = bool(0)

            register_write.next = 0
    @always_comb
    def rd_logic():
        rd_mux0.next = (ins[6:2]==funct4_0)
        rd_mux1.next = (ins[2:0]==opcode_ls)
        #other two
        #rd_r0_mux and rd_r1_mux are in id logic
        #maybe need to change it

    @always_comb
    def ds_logic():
        ds2_rx.next = ins[12:9]
        ds1_rx.next = ins[12:9]

    @always_comb
    def cr_write_logic():
        selector.next = ins[12:9]
    @always_comb
    def imm_branch_logic():
        imm[7].next = 0
        imm[7:0].next = ins[16:9]
        branch_offset[15].next = ins[15]
        branch_offset[14].next = ins[15]
        branch_offset[13].next = ins[15]
        branch_offset[12].next = ins[15]
        branch_offset[11].next = ins[15]
        branch_offset[10].next = ins[15]
        branch_offset[9].next = ins[15]
        branch_offset[8].next = ins[15]
        branch_offset[8:4].next = ins[15:12]
        branch_offset[4:1].next = ins[9:6]
        branch_offset[0].next = 0


    return instances()





