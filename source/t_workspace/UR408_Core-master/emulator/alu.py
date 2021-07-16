from myhdl import *

@block
def alu(ds1,ds2,imm,bra,branch,alu_out,alu_signal):
    '''

    :param ds1: 8 in  distiation1
    :param ds2: 8 in distination2
    :param imm: 8 in imm
    :param unsign: 1 in
    :param bra: 1 in jump
    :param branch: 1 out allow jump
    :param alu_out: 4 out output of alu
    :param alu_signal: 11 in alu signals
    :return:
    '''
    states=enum('add0','sub0','and0','or0','xor0','sr0','sl0','sra0','slt0','sltu0','eq0','neq0')

    shift_right_signed = Signal(intbv(0)[8:])
    shift_right_signed_temp = Signal(intbv(0)[8:])
    shift_right_unsigned = Signal(intbv(0)[8:])
    shift_left = Signal(intbv(0)[8:])
    shift_num= Signal(intbv(0)[8:])



    @always_comb
    def shift_temp():
        shift_right_signed_temp.next = ds1 >> ds2
        shift_left.next = ds1 << ds2
        #shift_num.next=0b11111111 << (7 + (~ds2+1))
        shift_num.next = 0b00000000
    @always_comb
    def shift_right_logic():
        if alu_signal==states.sr0:
            if ds1[7]:
                shift_right_signed.next=shift_right_signed_temp|shift_num
            else:
                shift_right_signed.next = shift_right_signed_temp
        else :
            shift_right_unsigned.next= shift_right_signed_temp

    @always_comb
    def branch_logic():
        branch.next=bra & ds1[0]

    @always_comb
    def alu_logic():
        #'add0','sub0','and0','or0','xor0','sr0','sl0','sra0','slt0','eq0','neq0'
        if alu_signal==states.add0:
            alu_out.next=ds1+ds2
        elif alu_signal==states.sub0:
            alu_out.next=ds1-ds2
        elif alu_signal==states.and0:
            alu_out.next=ds1 & ds2
        elif alu_signal==states.or0:
            alu_out.next=ds1 & ds2
        elif alu_signal==states.xor0:
            alu_out.next=ds1^ds2
        elif alu_signal==states.sr0:
            alu_out.next=shift_right_signed
        elif alu_signal==states.sl0:
            alu_out.next=shift_left
        elif alu_signal==states.sra0:
            alu_out.next=shift_right_unsigned
        elif alu_signal==states.slt0:
            if(ds1<ds2 and ds1[7]==0 and ds2[7]==0) or (ds1[7:]>ds2[7:] and ds1[7]==1 and ds1[7]==1) or (ds1[7]==1 and ds2[7]==0):
                alu_out.next=1
            else :
                alu_out.next=0
        elif alu_signal==states.sltu0:
            if ds1<ds2:
                alu_out.next=1
            else:
                alu_out.next=0
        elif alu_signal==states.eq0:
            if ds1==ds2:
                alu_out.next=1
            else :
                alu_out.next=0
        elif alu_signal == states.neq0:
            if ds1 == ds2:
                alu_out.next = 0
            else:
                alu_out.next = 1
        else:
            alu_out.next=imm

    return instances()








