`include "../RTL/PRV564Config.v"

`include "../RTL/PRV564Define.v"

//////////////////////////////////////////////////////////////////////////////////////////////////

//  Date    : 2021                                                                              //

//  Author  : Jack.Pan                                                                          //

//  Desc    : Instructions Decode core For PRV564 processor, which is a part of IDU             //

//  Version : 0.0(Orignal)                                                                      //

//////////////////////////////////////////////////////////////////////////////////////////////////

module IDcore(

//-----------------------CSR input------------------------------

    input wire              CSR_tvm,                    //Trap virtual memory

    input wire              CSR_tsr,                    //Trap supervisior return

    //input wire              CSR_tw,

//----------------------Instruction input(32bit fix-length)-----

    input wire [1:0]        InstrPriv,                  //Current instruction's privlage

    input wire  [31:0]      Instruction,                //Instruction input

    input wire [`XLEN-1:0]  InstructionPC,              //Instruction PC

    input wire              Valid,                      //Current instruction is valid

    input wire              InsAccessFlt,

    input wire              InsPageFlt,

    input wire              InsAddrMis,

//----------------------Read regfile (also used in dependence check)-----------

    output wire [4:0]       rs1_index,

    output reg              rs1_en,

    output wire [4:0]       rs2_index,

    output reg              rs2_en,

    input wire  [`XLEN-1:0] rs1_data,

    input wire  [`XLEN-1:0] rs2_data,

    output wire [4:0]       rd_index,

    output reg              rd_en,

//---------------------Read CSRs---------------------------------

    output wire [11:0]      csr_index,

    output reg              csr_en,

	 input  wire [`XLEN-1:0] CSR_data,

//---------------Data dependence check---------------------------

    output reg              Checken,

    input wire              DepdcFind,

//------------------Instruction information----------------------

    output reg              Info_jmp,

    output reg              Info_illins,

    output reg              Info_mret,

    output reg              Info_sret,

    output reg              Info_ecall,

    output reg              Info_ebreak,

    output reg              Info_system,

//---------------------BP Port----------------------------------

    output reg [`XLEN-1:0]  BP_address,                 //BP address

    output reg              BP_jmp,                     //need jump

//------------------Dispatch Port--------------------------------

    output wire             disp_ALU,                   //dispatch to ALU

    output wire             disp_LSU,                   //dispatch to load and store unit

    output wire             disp_Mcop,                  //dispatch to math-coprocessor

    output reg [7:0]        disp_opcode,

    output reg [1:0]        disp_opinfo,                //operation information

    output reg [3:0]        disp_size,                  //operation size

    output reg [`XLEN-1:0]  disp_ds1,                   //operation data source 1

    output reg [`XLEN-1:0]  disp_ds2                    //operation data source 2



);

parameter DISP_NULL = 4'h0;

parameter DISP_ALU  = 4'h1;

parameter DISP_LSU  = 4'h2;

parameter DISP_Mcop = 4'h4;

    reg  [3:0] disp_dest;             //dispatch destination

//-------------Instruction Opcode and funct segment decode--------------------

    wire [6:0] opcode;                 //Instr opcode

    wire [2:0] funct3;

    wire [4:0] funct5;

    wire [5:0] funct6;

    wire [6:0] funct7;

    wire [11:0]funct12;

assign opcode = (Instruction[6:0]);

assign funct3 = (Instruction[14:12]);

assign funct5 = (Instruction[31:27]);

assign funct6 = (Instruction[31:26]);

assign funct7 = (Instruction[31:25]);

assign funct12= (Instruction[31:20]);

//--------------immediate data decode----------------



    wire [63:0]imm20;		            //LUI，AUIPC指令使用的20位立即数（进行符号位拓展）

    wire [63:0]imm20_jal;	            //jal指令使用的20位立即数，左移一位，高位进行符号拓展

    wire [63:0]imm12_i;		            //I-type，L-type指令使用的12位立即数（进行符号位拓展）

    wire [63:0]imm12_b;		            //b-type指令使用的12位立即数（进行符号位拓展）

    wire [63:0]imm12_s;		            //S-type指令使用的12位立即数（进行符号位拓展）

    wire [63:0]imm5_csr;	            //csr指令使用的5位立即数，高位补0

    wire [63:0]shamt;                   //64bit 移位指令用的6bit立即数



assign imm20 	= {{32{Instruction[31]}},Instruction[31:12],12'b0};				//LUI，AUIPC指令使用的20位立即数（进行符号位拓展）

assign imm20_jal= {{44{Instruction[31]}},Instruction[19:12],Instruction[20],Instruction[30:21],1'b0};				//jal指令使用的20位立即数，左移一位，高位进行符号拓展

assign imm12_i	= {{52{Instruction[31]}},Instruction[31:20]};						//I-type，L-type指令使用的12位立即数（进行符号位拓展）

assign imm12_b	= {{52{Instruction[31]}},Instruction[7],Instruction[30:25],Instruction[11:8],1'b0};	//b-type指令使用的12位立即数（进行符号位拓展）

assign imm12_s	= {{52{Instruction[31]}},Instruction[31:25],Instruction[11:7]};		//S-type指令使用的12位立即数（进行符号位拓展）

assign imm5_csr = {59'b0,Instruction[11:7]};

assign shamt    = (Instruction[25:20]);	

//-----------------csr and regfile index decode-----------------

assign rs1_index = Instruction[19:15];

assign rs2_index = Instruction[24:20];

assign rd_index  = Instruction[11:7];

assign csr_index = Instruction[31:20];





//-----------------------------Instruction Decode------------------------------



    reg [127:0] instr_decode;          //Instruction one hot code

//////////////////////////////////////////////////////////////////////////////

//                                  decode                                  //

//                                                                          //

//                  Find all things about instructions here                 //

//                                                                          //

//////////////////////////////////////////////////////////////////////////////

always@(*)begin

    if(Valid)begin

        if(InsAddrMis | InsPageFlt | InsAccessFlt)begin //if instruction exception happen, the instruction is dispatch to ALU

            rs1_en      <= 1'b0;

            rs2_en      <= 1'b0;

            rd_en       <= 1'b0;

            csr_en      <= 1'b0;

            Checken     <= 1'b0;

            Info_jmp    <= 1'b0;

            Info_ebreak <= 1'b0;

            Info_ecall  <= 1'b0;

            Info_illins <= 1'b0;

            Info_mret   <= 1'b0;

            Info_sret   <= 1'b0;

            Info_system <= 1'b0;

            disp_opcode <= `ALU_NOP;

            disp_opinfo <= `Sign64;

            disp_size   <= 4'h8;

            disp_ds1    <= 64'hx;

            disp_ds2    <= 64'hx;

            disp_dest   <= DISP_ALU;            //a instruction flt happen, dispatch to ALU

        end

        else begin

            case(opcode)

                `lui_encode     : 

                begin 

                    instr_decode    <= `ins_lui;

                    rs1_en      <= 1'b0;

                    rs2_en      <= 1'b0;

                    rd_en       <= 1'b1;

                    csr_en      <= 1'b0;

                    Checken     <= 1'b0;

                    Info_jmp    <= 1'b0;

                    Info_ebreak <= 1'b0;

                    Info_ecall  <= 1'b0;

                    Info_illins <= 1'b0;

                    Info_mret   <= 1'b0;

                    Info_sret   <= 1'b0;

                    Info_system <= 1'b0;

                    disp_opcode <= `ALU_NOP;

                    disp_opinfo <= `Sign64;

                    disp_size   <= 4'h8;

                    disp_ds1    <= imm20;

                    disp_ds2    <= 64'hx;

                    disp_dest   <= DISP_ALU;

                end

                `auipc_encode   : 

                begin 

                    instr_decode    <= `ins_auipc;

                    rs1_en      <= 1'b0;

                    rs2_en      <= 1'b0;

                    rd_en       <= 1'b0;

                    csr_en      <= 1'b0;

                    Checken     <= 1'b0;

                    Info_jmp    <= 1'b0;

                    Info_ebreak <= 1'b0;

                    Info_ecall  <= 1'b0;

                    Info_illins <= 1'b0;

                    Info_mret   <= 1'b0;

                    Info_sret   <= 1'b0;

                    Info_system <= 1'b0;

                    disp_opcode <= `ALU_ADD;

                    disp_opinfo <= `Sign64;

                    disp_size   <= 4'h8;

                    disp_ds1    <= imm20;

                    disp_ds2    <= InstructionPC;

                    disp_dest   <= DISP_ALU;

                end

                `jal_encode     :                           //jump and link

                begin 

                    instr_decode    <= `ins_jal;

                    rs1_en      <= 1'b0;

                    rs2_en      <= 1'b0;

                    rd_en       <= 1'b1;

                    csr_en      <= 1'b0;

                    Checken     <= 1'b0;

                    Info_jmp    <= 1'b1;

                    Info_ebreak <= 1'b0;

                    Info_ecall  <= 1'b0;

                    Info_illins <= 1'b0;

                    Info_mret   <= 1'b0;

                    Info_sret   <= 1'b0;

                    Info_system <= 1'b0;

                    disp_opcode <= `ALU_ADD;

                    disp_opinfo <= `Sign64;

                    disp_size   <= 4'h8;

                    disp_ds1    <= 64'h4;

                    disp_ds2    <= InstructionPC;

                    disp_dest   <= DISP_ALU;

                end

                `jalr_encode    :                           //jump and link (reg)

                begin

                    instr_decode    <= `ins_jalr;

                    rs1_en      <= 1'b0;

                    rs2_en      <= 1'b0;

                    rd_en       <= 1'b1;

                    csr_en      <= 1'b0;

                    Checken     <= 1'b0;

                    Info_jmp    <= 1'b1;

                    Info_ebreak <= 1'b0;

                    Info_ecall  <= 1'b0;

                    Info_illins <= 1'b0;

                    Info_mret   <= 1'b0;

                    Info_sret   <= 1'b0;

                    Info_system <= 1'b0;

                    disp_opcode <= `ALU_ADD;

                    disp_opinfo <= `Sign64;

                    disp_size   <= 4'h8;

                    disp_ds1    <= 64'h4;

                    disp_ds2    <= InstructionPC;

                    disp_dest   <= DISP_ALU;

                end

                `branch_encode  :

                begin

                case(funct3)

                    3'b000 :                //beq

                    begin

                        instr_decode    <= `ins_beq;

                        rs1_en      <= 1'b1;

                        rs2_en      <= 1'b1;

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b1;

                        Info_jmp    <= 1'b1;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_NOP;

                        disp_opinfo <= `Sign64;

                        disp_size   <= 4'h8;

                        disp_ds1    <= 64'hx;

                        disp_ds2    <= 64'hx;

                        disp_dest   <= DepdcFind ? DISP_NULL : DISP_ALU; // if data dependence find, stop dispatch

                    end

                    3'b001 :                    //bne

                    begin

                        instr_decode    <= `ins_bne;

                        rs1_en      <= 1'b1;

                        rs2_en      <= 1'b1;

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b1;

                        Info_jmp    <= 1'b1;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_NOP;

                        disp_opinfo <= `Sign64;

                        disp_size   <= 4'h8;

                        disp_ds1    <= 64'hx;

                        disp_ds2    <= 64'hx;

                        disp_dest   <= DepdcFind ? DISP_NULL : DISP_ALU; // if data dependence find, stop dispatch

                    end

                    3'b100 :                    //blt

                    begin

                        instr_decode    <= `ins_blt;

                        rs1_en      <= 1'b1;

                        rs2_en      <= 1'b1;

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b1;

                        Info_jmp    <= 1'b1;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_NOP;

                        disp_opinfo <= `Sign64;

                        disp_size   <= 4'h8;

                        disp_ds1    <= 64'hx;

                        disp_ds2    <= 64'hx;

                        disp_dest   <= DepdcFind ? DISP_NULL : DISP_ALU; // if data dependence find, stop dispatch

                    end

                    3'b101 :                      //bge

                    begin

                        instr_decode    <= `ins_bge;

                        rs1_en      <= 1'b1;

                        rs2_en      <= 1'b1;

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b1;

                        Info_jmp    <= 1'b1;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_NOP;

                        disp_opinfo <= `Sign64;

                        disp_size   <= 4'h8;

                        disp_ds1    <= 64'hx;

                        disp_ds2    <= 64'hx;

                        disp_dest   <= DepdcFind ? DISP_NULL : DISP_ALU; // if data dependence find, stop dispatch

                    end

                    3'b110 :                        //bltu

                    begin

                        instr_decode    <= `ins_bltu;

                        rs1_en      <= 1'b1;

                        rs2_en      <= 1'b1;

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b1;

                        Info_jmp    <= 1'b1;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_NOP;

                        disp_opinfo <= `Sign64;

                        disp_size   <= 4'h8;

                        disp_ds1    <= 64'hx;

                        disp_ds2    <= 64'hx;

                        disp_dest   <= DepdcFind ? DISP_NULL : DISP_ALU; // if data dependence find, stop dispatch

                    end

                    3'b111 :                            //bgeu

                    begin

                        instr_decode    <= `ins_bgeu;

                        rs1_en      <= 1'b1;        //

                        rs2_en      <= 1'b1;

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b1;

                        Info_jmp    <= 1'b1;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_NOP;

                        disp_opinfo <= `Sign64;

                        disp_size   <= 4'h8;

                        disp_ds1    <= 64'hx;

                        disp_ds2    <= 64'hx;

                        disp_dest   <= DepdcFind ? DISP_NULL : DISP_ALU; // if data dependence find, stop dispatch

                    end

                    default:        //指令无法解码，产生异常指令

                    begin

                        instr_decode    <= `ins_nop;

                        rs1_en      <= 1'b0;

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b0;

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b1;            //this is a illigal instruction

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_NOP;

                        disp_opinfo <= `Sign64;

                        disp_size   <= 4'h8;

                        disp_ds1    <= 64'hx;

                        disp_ds2    <= 64'hx;

                        disp_dest   <= DISP_ALU;

                    end

                endcase

                end

                `load_encode    :                           //load

                begin

                case(funct3)

                    3'b000 :                        //lb

                    begin

                        instr_decode    <= `ins_lb;

                        rs1_en      <= 1'b1;        //rs1 data is used

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b1;        // write back to rd enable

                        csr_en      <= 1'b0;

                        Checken     <= 1'b1;        //need dependence check

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `LSU_READ;

                        disp_opinfo <= `Sign64;     //Sign extension is needed

                        disp_size   <= 4'h1;        //Operation Size = 1 Byte

                        disp_ds1    <= rs1_data + imm12_i;

                        disp_ds2    <= 64'hx;

                        disp_dest   <= DepdcFind ? DISP_NULL : DISP_LSU; // if data dependence find, stop dispatch

                    end

                    3'b001 :                        //lh

                    begin

                        instr_decode    <= `ins_lh;

                        rs1_en      <= 1'b1;

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b1;        // write back to rd enable

                        csr_en      <= 1'b0;

                        Checken     <= 1'b1;

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `LSU_READ;

                        disp_opinfo <= `Sign64;     //Sign extension is needed

                        disp_size   <= 4'h2;        //Operation Size = 2 Byte

                        disp_ds1    <= rs1_data + imm12_i;

                        disp_ds2    <= 64'hx;

                        disp_dest   <= DepdcFind ? DISP_NULL : DISP_LSU; // if data dependence find, stop dispatch

                    end

                    3'b010 :                        //lw

                    begin

                        instr_decode    <= `ins_lw;

                        rs1_en      <= 1'b1;

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b1;        // write back to rd enable

                        csr_en      <= 1'b0;

                        Checken     <= 1'b1;

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `LSU_READ;

                        disp_opinfo <= `Sign64;     //Sign extension is needed

                        disp_size   <= 4'h4;        //Operation Size = 4 Byte

                        disp_ds1    <= rs1_data + imm12_i;

                        disp_ds2    <= 64'hx;

                        disp_dest   <= DepdcFind ? DISP_NULL : DISP_LSU; // if data dependence find, stop dispatch

                    end

                    3'b011 :                        //ld

                    begin

                        instr_decode    <= `ins_ld;

                        rs1_en      <= 1'b1;

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b1;        // write back to rd enable

                        csr_en      <= 1'b0;

                        Checken     <= 1'b1;

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `LSU_READ;

                        disp_opinfo <= `Sign64;     //Sign extension is needed (it doesn't matter)

                        disp_size   <= 4'h8;        //Operation Size = 8 Byte

                        disp_ds1    <= rs1_data + imm12_i;

                        disp_ds2    <= 64'hx;

                        disp_dest   <= DepdcFind ? DISP_NULL : DISP_LSU; // if data dependence find, stop dispatch

                    end

                    3'b100 :                        //lbu

                    begin

                        instr_decode    <= `ins_lbu;

                        rs1_en      <= 1'b1;

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b1;        // write back to rd enable

                        csr_en      <= 1'b0;

                        Checken     <= 1'b1;

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `LSU_READ;

                        disp_opinfo <= `Unsign64;   //No sign extension

                        disp_size   <= 4'h1;        //Operation Size = 1 Byte

                        disp_ds1    <= rs1_data + imm12_i;

                        disp_ds2    <= 64'hx;

                        disp_dest   <= DepdcFind ? DISP_NULL : DISP_LSU; // if data dependence find, stop dispatch

                    end

                    3'b101 :                        //lhu

                    begin

                        instr_decode    <= `ins_lhu;

                        rs1_en      <= 1'b1;

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b1;        // write back to rd enable

                        csr_en      <= 1'b0;

                        Checken     <= 1'b1;

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `LSU_READ;

                        disp_opinfo <= `Unsign64;   //No sign extension

                        disp_size   <= 4'h2;        //Operation Size = 2 Byte

                        disp_ds1    <= rs1_data + imm12_i;

                        disp_ds2    <= 64'hx;

                        disp_dest   <= DepdcFind ? DISP_NULL : DISP_LSU; // if data dependence find, stop dispatch

                    end

                    3'b110 :                        //lwu

                    begin

                        instr_decode    <= `ins_lwu;

                        rs1_en      <= 1'b1;

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b1;        // write back to rd enable

                        csr_en      <= 1'b0;

                        Checken     <= 1'b1;

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `LSU_READ;

                        disp_opinfo <= `Unsign64;   //No sign extension

                        disp_size   <= 4'h4;        //Operation Size = 4 Byte

                        disp_ds1    <= rs1_data + imm12_i;

                        disp_ds2    <= 64'hx;

                        disp_dest   <= DepdcFind ? DISP_NULL : DISP_LSU; // if data dependence find, stop dispatch

                    end

                    default:

                    begin

                        instr_decode    <= `ins_nop;

                        rs1_en      <= 1'b0;

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b0;

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b1;            //this is a illigal instruction

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_NOP;

                        disp_opinfo <= `Sign64;

                        disp_size   <= 4'h8;

                        disp_ds1    <= 64'hx;

                        disp_ds2    <= 64'hx;

                        disp_dest   <= DISP_ALU;

                    end

                endcase

                end

                `store_encode   :                           //store

                begin

                case(funct3)

                    3'b000:

                    begin

                        instr_decode <= `ins_sb;

                        rs1_en      <= 1'b1;                //rs1 data is used

                        rs2_en      <= 1'b1;                //rs2 data is used

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b1;                //check enable

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `LSU_WRITE;          //command: write to memory

                        disp_opinfo <= `Sign64;             //It doesn't matter

                        disp_size   <= 4'h1;                //size = 1 byte

                        disp_ds1    <= rs1_data + imm12_s;  //Address = rs1 + imm12

                        disp_ds2    <= rs2_data;            //Data = rs2

                        disp_dest   <= DepdcFind ? DISP_NULL : DISP_LSU;

                    end

                    3'b001:

                    begin

                        instr_decode    <= `ins_sh;

                        rs1_en      <= 1'b1;                //rs1 data is used

                        rs2_en      <= 1'b1;                //rs2 data is used

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b1;                //check enable

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `LSU_WRITE;          //command: write to memory

                        disp_opinfo <= `Sign64;             //It doesn't matter

                        disp_size   <= 4'h2;                //size = 2 byte

                        disp_ds1    <= rs1_data + imm12_s;  //Address = rs1 + imm12

                        disp_ds2    <= rs2_data;            //Data = rs2

                        disp_dest   <= DepdcFind ? DISP_NULL : DISP_LSU;

                    end

                    3'b010:

                    begin

                        instr_decode    <= `ins_sw;

                        rs1_en      <= 1'b1;                //rs1 data is used

                        rs2_en      <= 1'b1;                //rs2 data is used

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b1;                //check enable

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `LSU_WRITE;          //command: write to memory

                        disp_opinfo <= `Sign64;             //It doesn't matter

                        disp_size   <= 4'h4;                //size = 4 byte

                        disp_ds1    <= rs1_data + imm12_s;  //Address = rs1 + imm12

                        disp_ds2    <= rs2_data;            //Data = rs2

                        disp_dest   <= DepdcFind ? DISP_NULL : DISP_LSU;

                    end

                    3'b011:

                    begin

                        instr_decode    <= `ins_sd;

                        rs1_en      <= 1'b1;                //rs1 data is used

                        rs2_en      <= 1'b1;                //rs2 data is used

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b1;                //check enable

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `LSU_WRITE;          //command: write to memory

                        disp_opinfo <= `Sign64;             //It doesn't matter

                        disp_size   <= 4'h8;                //size = 8 byte

                        disp_ds1    <= rs1_data + imm12_s;  //Address = rs1 + imm12

                        disp_ds2    <= rs2_data;            //Data = rs2

                        disp_dest   <= DepdcFind ? DISP_NULL : DISP_LSU;

                    end

                    default:

                    begin

                        instr_decode    <= `ins_nop;

                        rs1_en      <= 1'b0;

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b0;

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b1;            //this is a illigal instruction

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_NOP;

                        disp_opinfo <= `Sign64;

                        disp_size   <= 4'h8;

                        disp_ds1    <= 64'hx;

                        disp_ds2    <= 64'hx;

                        disp_dest   <= DISP_ALU;

                    end

                endcase

                end

                `imm_encode     :                           //64bit imm-reg operation

                case(funct3)

                    3'b000:

                    begin

                        instr_decode    <= `ins_addi;

                        rs1_en      <= 1'b1;                //rs1 data is used

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b1;                //write back is enable

                        csr_en      <= 1'b0;

                        Checken     <= 1'b1;                //check enable

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_ADD;            //command: ds1 + ds2

                        disp_opinfo <= `Sign64;             //It doesn't matter

                        disp_size   <= 4'h8;                //size = 8 byte

                        disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                        disp_ds2    <= imm12_i;             //Op data source 2 = imm12_i

                        disp_dest   <= DepdcFind ? DISP_NULL : DISP_ALU;

                    end

                    3'b001:                                 //shift left instructions

                    begin

                        if(funct6==6'b000000)begin              //slli

                            instr_decode    <= `ins_slli;

                            rs1_en      <= 1'b1;                //rs1 data is used

                            rs2_en      <= 1'b0;

                            rd_en       <= 1'b1;                //write back is enable

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;                //check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_SL;            //command: compare ds1 and ds2

                            disp_opinfo <= `Sign64;             //Sign number is used

                            disp_size   <= 4'h8;                //size = 8 byte

                            disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                            disp_ds2    <= shamt;               //Op data source 2 = shamt

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_ALU;

                        end

                        else begin

                            instr_decode    <= `ins_nop;

                            rs1_en      <= 1'b0;

                            rs2_en      <= 1'b0;

                            rd_en       <= 1'b0;

                            csr_en      <= 1'b0;

                            Checken     <= 1'b0;

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b1;            //this is a illigal instruction

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_NOP;

                            disp_opinfo <= `Sign64;

                            disp_size   <= 4'h8;

                            disp_ds1    <= 64'hx;

                            disp_ds2    <= 64'hx;

                            disp_dest   <= DISP_ALU;

                        end

                    end

                    3'b010:

                    begin

                        instr_decode    <= `ins_slti;

                        rs1_en      <= 1'b1;                //rs1 data is used

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b1;                //write back is enable

                        csr_en      <= 1'b0;

                        Checken     <= 1'b1;                //check enable

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_SLT;            //command: compare ds1 and ds2

                        disp_opinfo <= `Sign64;             //Sign number is used

                        disp_size   <= 4'h8;                //size = 8 byte

                        disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                        disp_ds2    <= imm12_i;             //Op data source 2 = imm12_i

                        disp_dest   <= DepdcFind ? DISP_NULL : DISP_ALU;

                    end

                    3'b011:

                    begin

                        instr_decode <= `ins_sltiu;

                        rs1_en      <= 1'b1;                //rs1 data is used

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b1;                //write back is enable

                        csr_en      <= 1'b0;

                        Checken     <= 1'b1;                //check enable

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_SLT;            //command: compare ds1 and ds2

                        disp_opinfo <= `Unsign64;           //Unsign number is used

                        disp_size   <= 4'h8;                //size = 8 byte

                        disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                        disp_ds2    <= imm12_i;             //Op data source 2 = imm12_i

                        disp_dest   <= DepdcFind ? DISP_NULL : DISP_ALU;

                    end

                    3'b100:

                    begin

                        instr_decode    <= `ins_xori;

                        rs1_en      <= 1'b1;                //rs1 data is used

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b1;                //write back is enable

                        csr_en      <= 1'b0;

                        Checken     <= 1'b1;                //check enable

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_XOR;            //command: XOR operation

                        disp_opinfo <= `Sign64;             //It doesn't matter

                        disp_size   <= 4'h8;                //size = 8 byte

                        disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                        disp_ds2    <= imm12_i;             //Op data source 2 = imm12_i

                        disp_dest   <= DepdcFind ? DISP_NULL : DISP_ALU;

                    end

                    3'b101:                                 //shift right instructions

                    begin

                        if(funct6==6'b000000)begin              //srli

                            instr_decode    <= `ins_srli;

                            rs1_en      <= 1'b1;                //rs1 data is used

                            rs2_en      <= 1'b0;

                            rd_en       <= 1'b1;                //write back is enable

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;                //check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_SR;            //command: compare ds1 and ds2

                            disp_opinfo <= `Sign64;             //Sign number is used

                            disp_size   <= 4'h8;                //size = 8 byte

                            disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                            disp_ds2    <= shamt;               //Op data source 2 = shamt

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_ALU;

                        end

                        else if(funct6==6'b010000)begin              //srli

                            instr_decode    <= `ins_srai;

                            rs1_en      <= 1'b1;                //rs1 data is used

                            rs2_en      <= 1'b0;

                            rd_en       <= 1'b1;                //write back is enable

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;                //check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_SR;            //command: compare ds1 and ds2

                            disp_opinfo <= `Unsign64;             //Sign number is used

                            disp_size   <= 4'h8;                //size = 8 byte

                            disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                            disp_ds2    <= shamt;               //Op data source 2 = shamt

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_ALU;

                        end

                        else begin

                            instr_decode    <= `ins_nop;

                            rs1_en      <= 1'b0;

                            rs2_en      <= 1'b0;

                            rd_en       <= 1'b0;

                            csr_en      <= 1'b0;

                            Checken     <= 1'b0;

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b1;            //this is a illigal instruction

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_NOP;

                            disp_opinfo <= `Sign64;

                            disp_size   <= 4'h8;

                            disp_ds1    <= 64'hx;

                            disp_ds2    <= 64'hx;

                            disp_dest   <= DISP_ALU;

                        end

                    end

                    3'b110:

                    begin

                        instr_decode    <= `ins_ori;

                        rs1_en      <= 1'b1;                //rs1 data is used

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b1;                //write back is enable

                        csr_en      <= 1'b0;

                        Checken     <= 1'b1;                //check enable

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_OR;             //command: OR operation

                        disp_opinfo <= `Sign64;             //It doesn't matter

                        disp_size   <= 4'h8;                //size = 8 byte

                        disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                        disp_ds2    <= imm12_i;             //Op data source 2 = imm12_i

                        disp_dest   <= DepdcFind ? DISP_NULL : DISP_ALU;

                    end

                    3'b111:

                    begin

                        instr_decode    <= `ins_andi;

                        rs1_en      <= 1'b1;                //rs1 data is used

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b1;                //write back is enable

                        csr_en      <= 1'b0;

                        Checken     <= 1'b1;                //check enable

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_AND;            //command: OR operation

                        disp_opinfo <= `Sign64;             //It doesn't matter

                        disp_size   <= 4'h8;                //size = 8 byte

                        disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                        disp_ds2    <= imm12_i;             //Op data source 2 = imm12_i

                        disp_dest   <= DepdcFind ? DISP_NULL : DISP_ALU;

                    end

                    default:

                    begin

                        instr_decode    <= `ins_nop;

                        rs1_en      <= 1'b0;

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b0;

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b1;            //this is a illigal instruction

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_NOP;

                        disp_opinfo <= `Sign64;

                        disp_size   <= 4'h8;

                        disp_ds1    <= 64'hx;

                        disp_ds2    <= 64'hx;

                        disp_dest   <= DISP_ALU;

                    end

                endcase

                `imm32_encode   :                           //32bit imm-reg operation

                case(funct3)

                    3'b000 : 

                    begin

                        instr_decode    <= `ins_addiw;

                        rs1_en      <= 1'b1;                //rs1 data is used

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b1;                //write back is enable

                        csr_en      <= 1'b0;

                        Checken     <= 1'b1;                //check enable

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_ADD;            //command: ds1 + ds2

                        disp_opinfo <= `Sign32;             //32bit operation

                        disp_size   <= 4'h4;                //size = 4 byte

                        disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                        disp_ds2    <= imm12_i;             //Op data source 2 = imm12_i

                        disp_dest   <= DepdcFind ? DISP_NULL : DISP_ALU;

                    end

                    3'b001 : 

                    if(funct7==7'b0)begin

                        instr_decode    <= `ins_slliw;

                        rs1_en      <= 1'b1;                //rs1 data is used

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b1;                //write to regfile is enable

                        csr_en      <= 1'b0;

                        Checken     <= 1'b1;                //check enable

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_SL;             //command: ds1 shift left

                        disp_opinfo <= `Sign32;             //32bit operation

                        disp_size   <= 4'h4;                //size = 4 byte

                        disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                        disp_ds2    <= rs2_index;           //Op data source 2 = shamt (rs2 index) 

                        disp_dest   <= DepdcFind ? DISP_NULL : DISP_ALU; 

                    end

                    else begin

                        instr_decode    <= `ins_nop;

                        rs1_en      <= 1'b0;

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b0;

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b1;            //this is a illigal instruction

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_NOP;

                        disp_opinfo <= `Sign64;

                        disp_size   <= 4'h8;

                        disp_ds1    <= 64'hx;

                        disp_ds2    <= 64'hx;

                        disp_dest   <= DISP_ALU;

                    end

                    3'b101 :

                    if(funct7==7'b0)begin

                        instr_decode    <= `ins_srliw;

                        rs1_en      <= 1'b1;                //rs1 data is used

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b1;                //write to regfile is enable

                        csr_en      <= 1'b0;

                        Checken     <= 1'b1;                //check enable

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_SR;             //command: ds1 shift right

                        disp_opinfo <= `Sign32;             //32bit operation

                        disp_size   <= 4'h4;                //size = 4 byte

                        disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                        disp_ds2    <= rs2_index;           //Op data source 2 = shamt (rs2 index) 

                        disp_dest   <= DepdcFind ? DISP_NULL : DISP_ALU; 

                    end

                    else if(funct7==7'd32)begin

                        instr_decode    <= `ins_sraiw;

                        rs1_en      <= 1'b1;                //rs1 data is used

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b1;                //write to regfile is enable

                        csr_en      <= 1'b0;

                        Checken     <= 1'b1;                //check enable

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_SR;             //command: ds1 shift right

                        disp_opinfo <= `Unsign32;           //Unsign 32bit operation

                        disp_size   <= 4'h4;                //size = 4 byte

                        disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                        disp_ds2    <= rs2_index;           //Op data source 2 = shamt (rs2 index) 

                        disp_dest   <= DepdcFind ? DISP_NULL : DISP_ALU; 

                    end

                    else begin

                        instr_decode    <= `ins_nop;

                        rs1_en      <= 1'b0;

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b0;

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b1;            //this is a illigal instruction

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_NOP;

                        disp_opinfo <= `Sign64;

                        disp_size   <= 4'h8;

                        disp_ds1    <= 64'hx;

                        disp_ds2    <= 64'hx;

                        disp_dest   <= DISP_ALU;

                    end

                    default:

                    begin

                        instr_decode    <= `ins_nop;

                        rs1_en      <= 1'b0;

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b0;

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b1;            //this is a illigal instruction

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_NOP;

                        disp_opinfo <= `Sign64;

                        disp_size   <= 4'h8;

                        disp_ds1    <= 64'hx;

                        disp_ds2    <= 64'hx;

                        disp_dest   <= DISP_ALU;

                    end

                endcase

                `reg_encode     :                           //64bit reg-reg operation

                case(funct3)

                    3'b000 :

                    begin

                        if(funct7==7'd0)begin

                            instr_decode    <= `ins_add;

                            rs1_en      <= 1'b1;                //rs1 data is used

                            rs2_en      <= 1'b1;                //rs2 data is used

                            rd_en       <= 1'b1;                //write to regfile is enable

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;                //check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_ADD;            //command: ds1 ADD ds2

                            disp_opinfo <= `Sign64;             //64bit operation

                            disp_size   <= 4'h8;                //size = 8 byte

                            disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                            disp_ds2    <= rs2_data;            //Op data source 2 = rs2

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_ALU; 

                        end

                        else if(funct7==7'd1)begin                   // MUL

                            instr_decode    <= `ins_mul;

                            rs1_en      <= 1'b1;                //rs1 data is used

                            rs2_en      <= 1'b1;                //rs2 data is used

                            rd_en       <= 1'b1;                //write to regfile is enable

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;                //check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `Mcop_MUL;           //command: ds1 * ds2

                            disp_opinfo <= `Sign64;             //64bit operation

                            disp_size   <= 4'h8;                //size = 8 byte

                            disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                            disp_ds2    <= rs2_data;            //Op data source 2 = rs2

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_Mcop; 

                        end

                        else if(funct7==7'd32)begin

                            instr_decode    <= `ins_sub;

                            rs1_en      <= 1'b1;                //rs1 data is used

                            rs2_en      <= 1'b1;                //rs2 data is used

                            rd_en       <= 1'b1;                //write to regfile is enable

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;                //check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_SUB;            //command: ds1 SUB ds2

                            disp_opinfo <= `Sign64;             //64bit operation

                            disp_size   <= 4'h8;                //size = 8 byte

                            disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                            disp_ds2    <= rs2_data;            //Op data source 2 = rs2

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_ALU; 

                        end

                        else begin

                            instr_decode    <= `ins_nop;

                            rs1_en      <= 1'b0;

                            rs2_en      <= 1'b0;

                            rd_en       <= 1'b0;

                            csr_en      <= 1'b0;

                            Checken     <= 1'b0;

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b1;            //this is a illigal instruction

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_NOP;

                            disp_opinfo <= `Sign64;

                            disp_size   <= 4'h8;

                            disp_ds1    <= 64'hx;

                            disp_ds2    <= 64'hx;

                            disp_dest   <= DISP_ALU;

                        end

                    end

                    3'b001 :

                    begin

                        if(funct7==7'd0)begin

                            instr_decode    <= `ins_sll;

                            rs1_en      <= 1'b1;                //rs1 data is used

                            rs2_en      <= 1'b1;                //rs2 data is used

                            rd_en       <= 1'b1;                //write to regfile is enable

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;                //check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_SL;             //command: ds1 shift left by ds2

                            disp_opinfo <= `Sign64;             //64bit operation

                            disp_size   <= 4'h8;                //size = 8 byte

                            disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                            disp_ds2    <= rs2_data;            //Op data source 2 = rs2

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_ALU; 

                        end

                        else if(funct7==7'd1)begin

                            instr_decode    <= `ins_mulh;

                            rs1_en      <= 1'b1;                //rs1 data is used

                            rs2_en      <= 1'b1;                //rs2 data is used

                            rd_en       <= 1'b1;                //write to regfile is enable

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;                //check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `Mcop_MULH;          

                            disp_opinfo <= `Sign64;             //64bit operation

                            disp_size   <= 4'h8;                //size = 8 byte

                            disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                            disp_ds2    <= rs2_data;            //Op data source 2 = rs2

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_Mcop; 

                        end

                        else begin

                            instr_decode    <= `ins_nop;

                            rs1_en      <= 1'b0;

                            rs2_en      <= 1'b0;

                            rd_en       <= 1'b0;

                            csr_en      <= 1'b0;

                            Checken     <= 1'b0;

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b1;            //this is a illigal instruction

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_NOP;

                            disp_opinfo <= `Sign64;

                            disp_size   <= 4'h8;

                            disp_ds1    <= 64'hx;

                            disp_ds2    <= 64'hx;

                            disp_dest   <= DISP_ALU;

                        end

                    end

                    3'b010 :

                    begin

                        if(funct7==7'd0)begin

                            instr_decode    <= `ins_slt;

                            rs1_en      <= 1'b1;                //rs1 data is used

                            rs2_en      <= 1'b1;                //rs2 data is used

                            rd_en       <= 1'b1;                //write back to regfile is enable

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;                //check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_SLT;            //command: if ds1 is small that ds2

                            disp_opinfo <= `Sign64;             //64bit operation

                            disp_size   <= 4'h8;                //size = 8 byte

                            disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                            disp_ds2    <= rs2_data;            //Op data source 2 = rs2

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_ALU; 

                        end

                        else if(funct7==7'd1)begin

                            instr_decode    <= `ins_mulhsu;

                            rs1_en      <= 1'b1;                //rs1 data is used

                            rs2_en      <= 1'b1;                //rs2 data is used

                            rd_en       <= 1'b1;                //write to regfile is enable

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;                //check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `Mcop_NULHS;         //command: 

                            disp_opinfo <= `Unsign64;             //64bit operation

                            disp_size   <= 4'h8;                //size = 8 byte

                            disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                            disp_ds2    <= rs2_data;            //Op data source 2 = rs2

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_Mcop; 

                        end

                        else begin

                            instr_decode    <= `ins_nop;

                            rs1_en      <= 1'b0;

                            rs2_en      <= 1'b0;

                            rd_en       <= 1'b0;

                            csr_en      <= 1'b0;

                            Checken     <= 1'b0;

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b1;            //this is a illigal instruction

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_NOP;

                            disp_opinfo <= `Sign64;

                            disp_size   <= 4'h8;

                            disp_ds1    <= 64'hx;

                            disp_ds2    <= 64'hx;

                            disp_dest   <= DISP_ALU;

                        end

                    end

                    3'b011 :

                    begin

                        if(funct7==7'd0)begin

                            instr_decode    <= `ins_sltu;

                            rs1_en      <= 1'b1;                //rs1 data is used

                            rs2_en      <= 1'b1;                //rs2 data is used

                            rd_en       <= 1'b1;                //write back to regfile is enable

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;                //check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_SLT;            //command: if ds1 is small that ds2

                            disp_opinfo <= `Unsign64;           //Unsign 64bit operation

                            disp_size   <= 4'h8;                //size = 8 byte

                            disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                            disp_ds2    <= rs2_data;            //Op data source 2 = rs2

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_ALU; 

                        end

                        else if(funct7==7'd1)begin

                            instr_decode    <= `ins_mulhu;

                            rs1_en      <= 1'b1;                //rs1 data is used

                            rs2_en      <= 1'b1;                //rs2 data is used

                            rd_en       <= 1'b1;                //write to regfile is enable

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;                //check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `Mcop_MULH;          //command: 

                            disp_opinfo <= `Unsign64;             //64bit operation

                            disp_size   <= 4'h8;                //size = 8 byte

                            disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                            disp_ds2    <= rs2_data;            //Op data source 2 = rs2

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_Mcop; 

                        end

                        else begin

                            instr_decode    <= `ins_nop;

                            rs1_en      <= 1'b0;

                            rs2_en      <= 1'b0;

                            rd_en       <= 1'b0;

                            csr_en      <= 1'b0;

                            Checken     <= 1'b0;

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b1;            //this is a illigal instruction

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_NOP;

                            disp_opinfo <= `Sign64;

                            disp_size   <= 4'h8;

                            disp_ds1    <= 64'hx;

                            disp_ds2    <= 64'hx;

                            disp_dest   <= DISP_ALU;

                        end

                    end

                    3'b100 :

                    begin

                        if(funct7==7'd0)begin

                            instr_decode    <= `ins_xor;

                            rs1_en      <= 1'b1;                //rs1 data is used

                            rs2_en      <= 1'b1;                //rs2 data is used

                            rd_en       <= 1'b1;                //write to regfile is enable

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;                //check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_XOR;            //command: ds1 XOR ds2

                            disp_opinfo <= `Sign64;             //64bit operation

                            disp_size   <= 4'h8;                //size = 8 byte

                            disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                            disp_ds2    <= rs2_data;            //Op data source 2 = rs2

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_ALU; 

                        end

                        else if(funct7==7'd1)begin

                            instr_decode    <= `ins_div;

                            rs1_en      <= 1'b1;                //rs1 data is used

                            rs2_en      <= 1'b1;                //rs2 data is used

                            rd_en       <= 1'b1;                //write to regfile is enable

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;                //check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `Mcop_DIV;           //command: 

                            disp_opinfo <= `Sign64;             //64bit operation

                            disp_size   <= 4'h8;                //size = 8 byte

                            disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                            disp_ds2    <= rs2_data;            //Op data source 2 = rs2

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_Mcop; 

                        end

                        else begin

                            instr_decode    <= `ins_nop;

                            rs1_en      <= 1'b0;

                            rs2_en      <= 1'b0;

                            rd_en       <= 1'b0;

                            csr_en      <= 1'b0;

                            Checken     <= 1'b0;

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b1;            //this is a illigal instruction

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_NOP;

                            disp_opinfo <= `Sign64;

                            disp_size   <= 4'h8;

                            disp_ds1    <= 64'hx;

                            disp_ds2    <= 64'hx;

                            disp_dest   <= DISP_ALU;

                        end

                    end

                    3'b101 :

                    begin

                        if(funct7==7'd0)begin

                            instr_decode    <= `ins_srl;

                            rs1_en      <= 1'b1;                //rs1 data is used

                            rs2_en      <= 1'b1;                //rs2 data is used

                            rd_en       <= 1'b1;                //write to regfile is enable

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;                //check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_SR;             //command: ds1 Shift Right by ds2

                            disp_opinfo <= `Sign64;             //64bit w Sign extension operation

                            disp_size   <= 4'h8;                //size = 8 byte

                            disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                            disp_ds2    <= rs2_data;            //Op data source 2 = rs2

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_ALU; 

                        end

                        else if(funct7==7'd1)begin

                            instr_decode    <= `ins_divu;

                            rs1_en      <= 1'b1;                //rs1 data is used

                            rs2_en      <= 1'b1;                //rs2 data is used

                            rd_en       <= 1'b1;                //write to regfile is enable

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;                //check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `Mcop_DIV;           //command: 

                            disp_opinfo <= `Unsign64;           //64bit operation

                            disp_size   <= 4'h8;                //size = 8 byte

                            disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                            disp_ds2    <= rs2_data;            //Op data source 2 = rs2

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_Mcop; 

                        end

                        else if(funct7==7'd32)begin

                            instr_decode    <= `ins_sra;

                            rs1_en      <= 1'b1;                //rs1 data is used

                            rs2_en      <= 1'b1;                //rs2 data is used

                            rd_en       <= 1'b1;                //write to regfile is enable

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;                //check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_SR;             //command: ds1 Shift Right by ds2

                            disp_opinfo <= `Unsign64;           //64bit w Sign extension operation

                            disp_size   <= 4'h8;                //size = 8 byte

                            disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                            disp_ds2    <= rs2_data;            //Op data source 2 = rs2

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_ALU; 

                        end

                        else begin

                            instr_decode    <= `ins_nop;

                            rs1_en      <= 1'b0;

                            rs2_en      <= 1'b0;

                            rd_en       <= 1'b0;

                            csr_en      <= 1'b0;

                            Checken     <= 1'b0;

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b1;            //this is a illigal instruction

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_NOP;

                            disp_opinfo <= `Sign64;

                            disp_size   <= 4'h8;

                            disp_ds1    <= 64'hx;

                            disp_ds2    <= 64'hx;

                            disp_dest   <= DISP_ALU;

                        end

                    end

                    3'b110 :

                    begin

                        if(funct7==7'd0)begin

                            instr_decode    <= `ins_or;

                            rs1_en      <= 1'b1;                //rs1 data is used

                            rs2_en      <= 1'b1;                //rs2 data is used

                            rd_en       <= 1'b1;                //write to regfile is enable

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;                //check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_OR;             //command: ds1 OR ds2

                            disp_opinfo <= `Sign64;             //64bit operation

                            disp_size   <= 4'h8;                //size = 8 byte

                            disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                            disp_ds2    <= rs2_data;            //Op data source 2 = rs2

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_ALU;

                        end

                        else if(funct7==7'd1)begin

                            instr_decode    <= `ins_rem;

                            rs1_en      <= 1'b1;                //rs1 data is used

                            rs2_en      <= 1'b1;                //rs2 data is used

                            rd_en       <= 1'b1;                //write to regfile is enable

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;                //check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `Mcop_REM;         //command: 

                            disp_opinfo <= `Sign64;             //64bit operation

                            disp_size   <= 4'h8;                //size = 8 byte

                            disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                            disp_ds2    <= rs2_data;            //Op data source 2 = rs2

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_Mcop; 

                        end

                        else begin

                            instr_decode    <= `ins_nop;

                            rs1_en      <= 1'b0;

                            rs2_en      <= 1'b0;

                            rd_en       <= 1'b0;

                            csr_en      <= 1'b0;

                            Checken     <= 1'b0;

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b1;            //this is a illigal instruction

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_NOP;

                            disp_opinfo <= `Sign64;

                            disp_size   <= 4'h8;

                            disp_ds1    <= 64'hx;

                            disp_ds2    <= 64'hx;

                            disp_dest   <= DISP_ALU;

                        end

                    end

                    3'b111 :

                    begin

                        if(funct7==7'd0)begin

                            instr_decode    <= `ins_and;

                            rs1_en      <= 1'b1;                //rs1 data is used

                            rs2_en      <= 1'b1;                //rs2 data is used

                            rd_en       <= 1'b1;                //write to regfile is enable

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;                //check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_AND;            //command: ds1 OR ds2

                            disp_opinfo <= `Sign64;             //64bit operation

                            disp_size   <= 4'h8;                //size = 8 byte

                            disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                            disp_ds2    <= rs2_data;            //Op data source 2 = rs2

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_ALU;

                        end

                        else if(funct7==7'd1)begin

                            instr_decode    <= `ins_remu;

                            rs1_en      <= 1'b1;                //rs1 data is used

                            rs2_en      <= 1'b1;                //rs2 data is used

                            rd_en       <= 1'b1;                //write to regfile is enable

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;                //check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `Mcop_REM;         //command: 

                            disp_opinfo <= `Sign64;             //64bit operation

                            disp_size   <= 4'h8;                //size = 8 byte

                            disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                            disp_ds2    <= rs2_data;            //Op data source 2 = rs2

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_Mcop; 

                        end

                        else begin

                            instr_decode    <= `ins_nop;

                            rs1_en      <= 1'b0;

                            rs2_en      <= 1'b0;

                            rd_en       <= 1'b0;

                            csr_en      <= 1'b0;

                            Checken     <= 1'b0;

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b1;            //this is a illigal instruction

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_NOP;

                            disp_opinfo <= `Sign64;

                            disp_size   <= 4'h8;

                            disp_ds1    <= 64'hx;

                            disp_ds2    <= 64'hx;

                            disp_dest   <= DISP_ALU;

                        end

                    end

                    default : 

                    begin

                        instr_decode    <= `ins_nop;

                        rs1_en      <= 1'b0;

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b0;

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b1;            //this is a illigal instruction

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_NOP;

                        disp_opinfo <= `Sign64;

                        disp_size   <= 4'h8;

                        disp_ds1    <= 64'hx;

                        disp_ds2    <= 64'hx;

                        disp_dest   <= DISP_ALU;

                    end

                endcase

                `reg32_encode   :                           //32bit reg-reg operation

                case(funct3)

                    3'b000 :

                    begin

                        if(funct7==7'd0)begin

                            instr_decode    <= `ins_addw;

                            rs1_en      <= 1'b1;                //rs1 data is used

                            rs2_en      <= 1'b1;                //rs2 data is used

                            rd_en       <= 1'b1;                //write to regfile is enable

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;                //check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_ADD;            //command: ds1 ADD ds2

                            disp_opinfo <= `Sign32;             //32bit operation

                            disp_size   <= 4'h4;                //size = 4 byte

                            disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                            disp_ds2    <= rs2_data;            //Op data source 2 = rs2

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_ALU; 

                        end

                        else if(funct7==7'd1)begin

                            instr_decode    <= `ins_mulw;

                            rs1_en      <= 1'b1;                //rs1 data is used

                            rs2_en      <= 1'b1;                //rs2 data is used

                            rd_en       <= 1'b1;                //write to regfile is enable

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;                //check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `Mcop_MUL;           //command: 

                            disp_opinfo <= `Sign32;             //64bit operation

                            disp_size   <= 4'h4;                //size = 8 byte

                            disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                            disp_ds2    <= rs2_data;            //Op data source 2 = rs2

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_Mcop; 

                        end

                        else if(funct7==7'd32)begin

                            instr_decode    <= `ins_subw;

                            rs1_en      <= 1'b1;                //rs1 data is used

                            rs2_en      <= 1'b1;                //rs2 data is used

                            rd_en       <= 1'b1;                //write to regfile is enable

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;                //check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_SUB;            //command: ds1 SUB ds2

                            disp_opinfo <= `Sign32;             //32bit operation

                            disp_size   <= 4'h4;                //size = 4 byte

                            disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                            disp_ds2    <= rs2_data;            //Op data source 2 = rs2

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_ALU; 

                        end

                        else begin

                            instr_decode    <= `ins_nop;

                            rs1_en      <= 1'b0;

                            rs2_en      <= 1'b0;

                            rd_en       <= 1'b0;

                            csr_en      <= 1'b0;

                            Checken     <= 1'b0;

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b1;            //this is a illigal instruction

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_NOP;

                            disp_opinfo <= `Sign64;

                            disp_size   <= 4'h8;

                            disp_ds1    <= 64'hx;

                            disp_ds2    <= 64'hx;

                            disp_dest   <= DISP_ALU;

                        end

                    end

                    3'b001 :

                    begin

                        if(funct7==7'd0)begin

                            instr_decode    <= `ins_sllw;

                            rs1_en      <= 1'b1;                //rs1 data is used

                            rs2_en      <= 1'b1;                //rs2 data is used

                            rd_en       <= 1'b1;                //write to regfile is enable

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;                //check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_SL;             //command: ds1 shift left by ds2

                            disp_opinfo <= `Sign32;             //32bit operation

                            disp_size   <= 4'h4;                //size = 8 byte

                            disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                            disp_ds2    <= rs2_data;            //Op data source 2 = rs2

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_ALU; 

                        end

                        else begin

                            instr_decode    <= `ins_nop;

                            rs1_en      <= 1'b0;

                            rs2_en      <= 1'b0;

                            rd_en       <= 1'b0;

                            csr_en      <= 1'b0;

                            Checken     <= 1'b0;

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b1;            //this is a illigal instruction

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_NOP;

                            disp_opinfo <= `Sign64;

                            disp_size   <= 4'h8;

                            disp_ds1    <= 64'hx;

                            disp_ds2    <= 64'hx;

                            disp_dest   <= DISP_ALU;

                        end

                    end

                    3'b100 :

                    begin

                        if(funct7==7'd1)begin

                            instr_decode    <= `ins_divw;

                            rs1_en      <= 1'b1;                //rs1 data is used

                            rs2_en      <= 1'b1;                //rs2 data is used

                            rd_en       <= 1'b1;                //write to regfile is enable

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;                //check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `Mcop_DIV;           //command: 

                            disp_opinfo <= `Sign32;             //64bit operation

                            disp_size   <= 4'h8;                //size = 8 byte

                            disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                            disp_ds2    <= rs2_data;            //Op data source 2 = rs2

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_Mcop; 

                        end

                        else begin

                            instr_decode    <= `ins_nop;

                            rs1_en      <= 1'b0;

                            rs2_en      <= 1'b0;

                            rd_en       <= 1'b0;

                            csr_en      <= 1'b0;

                            Checken     <= 1'b0;

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b1;            //this is a illigal instruction

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_NOP;

                            disp_opinfo <= `Sign64;

                            disp_size   <= 4'h8;

                            disp_ds1    <= 64'hx;

                            disp_ds2    <= 64'hx;

                            disp_dest   <= DISP_ALU;

                        end

                    end

                    3'b101 :

                    begin

                        if(funct7==7'd0)begin

                            instr_decode    <= `ins_srlw;

                            rs1_en      <= 1'b1;                //rs1 data is used

                            rs2_en      <= 1'b1;                //rs2 data is used

                            rd_en       <= 1'b1;                //write to regfile is enable

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;                //check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_SR;             //command: ds1 Shift Right by ds2

                            disp_opinfo <= `Sign32;             //32bit w Sign extension operation

                            disp_size   <= 4'h4;                //size = 8 byte

                            disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                            disp_ds2    <= rs2_data;            //Op data source 2 = rs2

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_ALU; 

                        end

                        else if(funct7==7'd1)begin

                            instr_decode    <= `ins_divuw;

                            rs1_en      <= 1'b1;                //rs1 data is used

                            rs2_en      <= 1'b1;                //rs2 data is used

                            rd_en       <= 1'b1;                //write to regfile is enable

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;                //check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `Mcop_DIV;           //command: 

                            disp_opinfo <= `Unsign32;           //64bit operation

                            disp_size   <= 4'h4;                //size = 8 byte

                            disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                            disp_ds2    <= rs2_data;            //Op data source 2 = rs2

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_Mcop; 

                        end

                        else begin

                            instr_decode    <= `ins_nop;

                            rs1_en      <= 1'b0;

                            rs2_en      <= 1'b0;

                            rd_en       <= 1'b0;

                            csr_en      <= 1'b0;

                            Checken     <= 1'b0;

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b1;            //this is a illigal instruction

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_NOP;

                            disp_opinfo <= `Sign64;

                            disp_size   <= 4'h8;

                            disp_ds1    <= 64'hx;

                            disp_ds2    <= 64'hx;

                            disp_dest   <= DISP_ALU;

                        end

                    end

                    3'b110 :

                    begin

                        if(funct7==7'd1)begin

                            instr_decode    <= `ins_remw;

                            rs1_en      <= 1'b1;                //rs1 data is used

                            rs2_en      <= 1'b1;                //rs2 data is used

                            rd_en       <= 1'b1;                //write to regfile is enable

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;                //check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `Mcop_REM;           //command: 

                            disp_opinfo <= `Sign32;             //64bit operation

                            disp_size   <= 4'h8;                //size = 8 byte

                            disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                            disp_ds2    <= rs2_data;            //Op data source 2 = rs2

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_Mcop; 

                        end

                        else begin

                            instr_decode    <= `ins_nop;

                            rs1_en      <= 1'b0;

                            rs2_en      <= 1'b0;

                            rd_en       <= 1'b0;

                            csr_en      <= 1'b0;

                            Checken     <= 1'b0;

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b1;            //this is a illigal instruction

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_NOP;

                            disp_opinfo <= `Sign64;

                            disp_size   <= 4'h8;

                            disp_ds1    <= 64'hx;

                            disp_ds2    <= 64'hx;

                            disp_dest   <= DISP_ALU;

                        end

                    end

                    3'b111 :

                    begin

                        if(funct7==7'd1)begin

                            instr_decode    <= `ins_remuw;

                            rs1_en      <= 1'b1;                //rs1 data is used

                            rs2_en      <= 1'b1;                //rs2 data is used

                            rd_en       <= 1'b1;                //write to regfile is enable

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;                //check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `Mcop_REM;           //command: 

                            disp_opinfo <= `Unsign32;             //64bit operation

                            disp_size   <= 4'h8;                //size = 8 byte

                            disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                            disp_ds2    <= rs2_data;            //Op data source 2 = rs2

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_Mcop; 

                        end

                        else begin

                            instr_decode    <= `ins_nop;

                            rs1_en      <= 1'b0;

                            rs2_en      <= 1'b0;

                            rd_en       <= 1'b0;

                            csr_en      <= 1'b0;

                            Checken     <= 1'b0;

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b1;            //this is a illigal instruction

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_NOP;

                            disp_opinfo <= `Sign64;

                            disp_size   <= 4'h8;

                            disp_ds1    <= 64'hx;

                            disp_ds2    <= 64'hx;

                            disp_dest   <= DISP_ALU;

                        end

                    end

                    default:

                    begin

                        instr_decode    <= `ins_nop;

                        rs1_en      <= 1'b0;

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b0;

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b1;            //this is a illigal instruction

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_NOP;

                        disp_opinfo <= `Sign64;

                        disp_size   <= 4'h8;

                        disp_ds1    <= 64'hx;

                        disp_ds2    <= 64'hx;

                        disp_dest   <= DISP_ALU;

                    end

                endcase

                `mem_encode     : 

                case(funct3)

                    3'b000 : 

                    begin

                        instr_decode    <= `ins_fence;

                        rs1_en      <= 1'b0;

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b0;

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b1;                //This is a system instruction

                        disp_opcode <= `LSU_CacheRef;       //command: Cache Refersh

                        disp_opinfo <= `Sign64;             //opinfo=2'b00, is local refersh

                        disp_size   <= 4'h8;                //

                        disp_ds1    <= rs1_data;            //Op data source 1 = rs1

                        disp_ds2    <= rs2_data;            //Op data source 2 = rs2

                        disp_dest   <= DISP_LSU; 

                    end

                    3'b001 :

                    begin

                        instr_decode    <= `ins_fence_i;

                        rs1_en      <= 1'b0;

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b0;

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b1;                //This is a system instruction

                        disp_opcode <= `LSU_CacheRef;       //command: Cache Refersh

                        disp_opinfo <= `Unsign32;           //opinfo=2'b11, is another refersh

                        disp_size   <= 4'h8;                //

                        disp_ds1    <= 64'hx;               //Op data source 1 = rs1

                        disp_ds2    <= 64'hx;               //Op data source 2 = rs2

                        disp_dest   <= DISP_LSU; 

                    end

                    default :

                    begin

                        instr_decode    <= `ins_nop;

                        rs1_en      <= 1'b0;

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b0;

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b1;            //this is a illigal instruction

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_NOP;

                        disp_opinfo <= `Sign64;

                        disp_size   <= 4'h8;

                        disp_ds1    <= 64'hx;

                        disp_ds2    <= 64'hx;

                        disp_dest   <= DISP_ALU;

                    end

                endcase

                `system_encode  :                           //system control instructions

                case(funct3)

                    3'b000 : 

                    if(funct12==12'd0)begin                 //ecall

                        instr_decode    <= `ins_ecall;

                        rs1_en      <= 1'b0;

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b0;

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b1;                //ecall instruction

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b1;                //This is a system instruction

                        disp_opcode <= `ALU_NOP;            //command: NO

                        disp_opinfo <= `Sign64;             //default

                        disp_size   <= 4'h8;                //

                        disp_ds1    <= 64'hx;               //

                        disp_ds2    <= 64'hx;               //

                        disp_dest   <= DISP_ALU; 

                    end

                    else if(funct12==12'd1)begin            //ebreak

                        instr_decode    <= `ins_ebreak;

                        rs1_en      <= 1'b0;

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b0;

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b1;                //ebreak instruction

                        Info_ecall  <= 1'b0;                

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b1;                //This is a system instruction

                        disp_opcode <= `ALU_NOP;            //command: NO

                        disp_opinfo <= `Sign64;             //default

                        disp_size   <= 4'h8;                //

                        disp_ds1    <= 64'hx;               //

                        disp_ds2    <= 64'hx;               //

                        disp_dest   <= DISP_ALU; 

                    end

                    else if(funct12==12'b000100000010)begin //sret

                        if(CSR_tsr)begin                        //TSR=1, execute a SRET will cause a illigal instr error

                            instr_decode    <= `ins_nop;

                            rs1_en      <= 1'b0;

                            rs2_en      <= 1'b0;

                            rd_en       <= 1'b0;

                            csr_en      <= 1'b0;

                            Checken     <= 1'b0;

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b1;            //this is a illigal instruction

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_NOP;

                            disp_opinfo <= `Sign64;

                            disp_size   <= 4'h8;

                            disp_ds1    <= 64'hx;

                            disp_ds2    <= 64'hx;

                            disp_dest   <= DISP_ALU;

                        end

                        else begin

                            instr_decode    <= `ins_sret;       //sret

                            rs1_en      <= 1'b0;

                            rs2_en      <= 1'b0;

                            rd_en       <= 1'b0;

                            csr_en      <= 1'b0;

                            Checken     <= 1'b0;

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;                

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b1;                //sret instruction

                            Info_system <= 1'b1;                //This is a system instruction

                            disp_opcode <= `ALU_NOP;            //command: NO

                            disp_opinfo <= `Sign64;             //default

                            disp_size   <= 4'h8;                //

                            disp_ds1    <= 64'hx;               //

                            disp_ds2    <= 64'hx;               //

                            disp_dest   <= DISP_ALU;

                        end 

                    end

                    else if(funct12==12'b001100000010)begin //mret

                        instr_decode    <= `ins_mret;

                        rs1_en      <= 1'b0;

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b0;

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;                

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b1;                //mret instruction

                        Info_sret   <= 1'b0;                

                        Info_system <= 1'b1;                //This is a system instruction

                        disp_opcode <= `ALU_NOP;            //command: NO

                        disp_opinfo <= `Sign64;             //default

                        disp_size   <= 4'h8;                //

                        disp_ds1    <= 64'hx;               //

                        disp_ds2    <= 64'hx;               //

                        disp_dest   <= DISP_ALU; 

                    end

                    else if(funct12==12'b000100000101)begin //wfi

                        instr_decode    <= `ins_wfi;

                        rs1_en      <= 1'b0;

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b0;

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;                

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;                

                        Info_system <= 1'b0;                //This is NOT a system instruction

                        disp_opcode <= `ALU_NOP;            //command: NO

                        disp_opinfo <= `Sign64;             //default

                        disp_size   <= 4'h8;                //

                        disp_ds1    <= 64'hx;               //

                        disp_ds2    <= 64'hx;               //

                        disp_dest   <= DISP_ALU; 

                    end

                    else if(funct7==7'b0001001)begin        //sfence.vma

                        if(CSR_tvm)begin

                            instr_decode    <= `ins_nop;

                            rs1_en      <= 1'b0;

                            rs2_en      <= 1'b0;

                            rd_en       <= 1'b0;

                            csr_en      <= 1'b0;

                            Checken     <= 1'b0;

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b1;            //this is a illigal instruction

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_NOP;

                            disp_opinfo <= `Sign64;

                            disp_size   <= 4'h8;

                            disp_ds1    <= 64'hx;

                            disp_ds2    <= 64'hx;

                            disp_dest   <= DISP_ALU;

                        end

                        else begin

                            instr_decode    <= `ins_sfencevma;

                            rs1_en      <= 1'b0;

                            rs2_en      <= 1'b0;

                            rd_en       <= 1'b0;

                            csr_en      <= 1'b0;

                            Checken     <= 1'b0;

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;   

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;                

                            Info_system <= 1'b1;                //This is a system instruction

                            disp_opcode <= `LSU_TLBRef;         //command: refersh TLB

                            disp_opinfo <= `Sign64;             //default

                            disp_size   <= 4'h8;                //

                            disp_ds1    <= 64'hx;               //

                            disp_ds2    <= 64'hx;               //

                            disp_dest   <= DISP_LSU;

                        end 

                    end

                    else begin

                        instr_decode    <= `ins_nop;

                        rs1_en      <= 1'b0;

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b0;

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b1;            //this is a illigal instruction

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_NOP;

                        disp_opinfo <= `Sign64;

                        disp_size   <= 4'h8;

                        disp_ds1    <= 64'hx;

                        disp_ds2    <= 64'hx;

                        disp_dest   <= DISP_ALU;

                    end

                    3'b001 :

                    if(InstrPriv >= csr_index[9:8])     //if current privlage higner than CSR's privlage, access permit

                    begin

                        instr_decode    <= `ins_csrrw;

                        rs1_en      <= 1'b1;            //rs 1 enable

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b1;            //write back to csr

                        csr_en      <= 1'b1;            //csr read&write enable

                        Checken     <= 1'b1;            //check enable    

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b1;            //this is a system instruction

                        disp_opcode <= `ALU_CSRW;       //command : CSRW

                        disp_opinfo <= `Sign64;

                        disp_size   <= 4'h8;

                        disp_ds1    <= rs1_data;        //data source1 = rs1

                        disp_ds2    <= CSR_data;        //data source2 = csr read

                        disp_dest   <= DISP_ALU;        //dispatch to ALU

                    end

                    else begin

                        instr_decode    <= `ins_nop;

                        rs1_en      <= 1'b0;

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b0;

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b1;            //this is a illigal instruction

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_NOP;

                        disp_opinfo <= `Sign64;

                        disp_size   <= 4'h8;

                        disp_ds1    <= 64'hx;

                        disp_ds2    <= 64'hx;

                        disp_dest   <= DISP_ALU;

                    end

                    3'b010 :

                    if(InstrPriv >= csr_index[9:8])

                    begin

                        instr_decode    <= `ins_csrrs;

                        rs1_en      <= 1'b1;            //rs 1 enable

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b1;            //write back to csr

                        csr_en      <= 1'b1;            //csr read&write enable

                        Checken     <= 1'b1;            //check enable    

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b1;            //this is a system instruction

                        disp_opcode <= `ALU_CSRS;       //command : CSRS

                        disp_opinfo <= `Sign64;

                        disp_size   <= 4'h8;

                        disp_ds1    <= rs1_data;        //data source1 = rs1

                        disp_ds2    <= CSR_data;        //data source2 = csr read

                        disp_dest   <= DISP_ALU;        //dispatch to ALU

                    end

                    else begin

                        instr_decode    <= `ins_nop;

                        rs1_en      <= 1'b0;

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b0;

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b1;            //this is a illigal instruction

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_NOP;

                        disp_opinfo <= `Sign64;

                        disp_size   <= 4'h8;

                        disp_ds1    <= 64'hx;

                        disp_ds2    <= 64'hx;

                        disp_dest   <= DISP_ALU;

                    end

                    3'b011 :

                    if(InstrPriv >= csr_index[9:8])

                    begin

                        instr_decode    <= `ins_csrrc;

                        rs1_en      <= 1'b1;            //rs 1 enable

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b1;            //write back to csr

                        csr_en      <= 1'b1;            //csr read&write enable

                        Checken     <= 1'b1;            //check enable    

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b1;            //this is a system instruction

                        disp_opcode <= `ALU_CSRC;       //command : CSRC

                        disp_opinfo <= `Sign64;

                        disp_size   <= 4'h8;

                        disp_ds1    <= rs1_data;        //data source1 = rs1

                        disp_ds2    <= CSR_data;        //data source2 = csr read

                        disp_dest   <= DISP_ALU;        //dispatch to ALU

                    end

                    else begin

                        instr_decode    <= `ins_nop;

                        rs1_en      <= 1'b0;

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b0;

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b1;            //this is a illigal instruction

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_NOP;

                        disp_opinfo <= `Sign64;

                        disp_size   <= 4'h8;

                        disp_ds1    <= 64'hx;

                        disp_ds2    <= 64'hx;

                        disp_dest   <= DISP_ALU;

                    end

                    3'b101 :

                    if(InstrPriv >= csr_index[9:8])

                    begin

                        instr_decode    <= `ins_csrrwi;

                        rs1_en      <= 1'b0;            

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b1;            //write back to csr

                        csr_en      <= 1'b1;            //csr read&write enable

                        Checken     <= 1'b1;            //check enable    

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b1;            //this is a system instruction

                        disp_opcode <= `ALU_CSRW;       //command : CSRC

                        disp_opinfo <= `Sign64;

                        disp_size   <= 4'h8;

                        disp_ds1    <= imm5_csr;        //data source1 = immediate data

                        disp_ds2    <= CSR_data;        //data source2 = csr read

                        disp_dest   <= DISP_ALU;        //dispatch to ALU

                    end

                    else begin

                        instr_decode    <= `ins_nop;

                        rs1_en      <= 1'b0;

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b0;

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b1;            //this is a illigal instruction

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_NOP;

                        disp_opinfo <= `Sign64;

                        disp_size   <= 4'h8;

                        disp_ds1    <= 64'hx;

                        disp_ds2    <= 64'hx;

                        disp_dest   <= DISP_ALU;

                    end

                    3'b110 :

                    if(InstrPriv >= csr_index[9:8])

                    begin

                        instr_decode    <= `ins_csrrsi;

                        rs1_en      <= 1'b0;            

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b1;            //write back to csr

                        csr_en      <= 1'b1;            //csr read&write enable

                        Checken     <= 1'b1;            //check enable    

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b1;            //this is a system instruction

                        disp_opcode <= `ALU_CSRS;       //command : CSRC

                        disp_opinfo <= `Sign64;

                        disp_size   <= 4'h8;

                        disp_ds1    <= imm5_csr;        //data source1 = immediate data

                        disp_ds2    <= CSR_data;        //data source2 = csr read

                        disp_dest   <= DISP_ALU;        //dispatch to ALU

                    end

                    else begin

                        instr_decode    <= `ins_nop;

                        rs1_en      <= 1'b0;

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b0;

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b1;            //this is a illigal instruction

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_NOP;

                        disp_opinfo <= `Sign64;

                        disp_size   <= 4'h8;

                        disp_ds1    <= 64'hx;

                        disp_ds2    <= 64'hx;

                        disp_dest   <= DISP_ALU;

                    end

                    3'b111 :

                    if(InstrPriv >= csr_index[9:8])

                    begin

                        instr_decode    <= `ins_csrrci;

                        rs1_en      <= 1'b0;            

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b1;            //write back to csr

                        csr_en      <= 1'b1;            //csr read&write enable

                        Checken     <= 1'b1;            //check enable    

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b0;

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b1;            //this is a system instruction

                        disp_opcode <= `ALU_CSRC;       //command : CSRC

                        disp_opinfo <= `Sign64;

                        disp_size   <= 4'h8;

                        disp_ds1    <= imm5_csr;        //data source1 = immediate data

                        disp_ds2    <= CSR_data;        //data source2 = csr read

                        disp_dest   <= DISP_ALU;        //dispatch to ALU

                    end

                    else begin

                        instr_decode    <= `ins_nop;

                        rs1_en      <= 1'b0;

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b0;

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b1;            //this is a illigal instruction

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_NOP;

                        disp_opinfo <= `Sign64;

                        disp_size   <= 4'h8;

                        disp_ds1    <= 64'hx;

                        disp_ds2    <= 64'hx;

                        disp_dest   <= DISP_ALU;

                    end

                    default :

                    begin

                        instr_decode    <= `ins_nop;

                        rs1_en      <= 1'b0;

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b0;

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b1;            //this is a illigal instruction

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_NOP;

                        disp_opinfo <= `Sign64;

                        disp_size   <= 4'h8;

                        disp_ds1    <= 64'hx;

                        disp_ds2    <= 64'hx;

                        disp_dest   <= DISP_ALU;

                    end

                endcase

                `amo_encode     :

                if(funct3==3'b011)begin                     //64bit A-extension

                    case(funct5)

                        5'd2 : 

                        begin

                            instr_decode    <= `ins_lrd;

                            rs1_en      <= 1'b1;            //rs1 is used

                            rs2_en      <= 1'b0;

                            rd_en       <= 1'b1;            //write back to regfile

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;            //Check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `LSU_READ_Lock;

                            disp_opinfo <= `Sign64;

                            disp_size   <= 4'h8;            //64bit operation size

                            disp_ds1    <= rs1_data;

                            disp_ds2    <= rs2_data;

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_LSU;

                        end

                        5'd3 :

                        begin

                            instr_decode    <= `ins_scd;

                            rs1_en      <= 1'b1;            //rs1 is used

                            rs2_en      <= 1'b1;

                            rd_en       <= 1'b1;            //write back to regfile

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;            //Check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `LSU_WRITE_Unloc;

                            disp_opinfo <= `Sign64;

                            disp_size   <= 4'h8;            //64bit operation size

                            disp_ds1    <= rs1_data;

                            disp_ds2    <= rs2_data;

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_LSU;

                        end

                        5'd1 :

                        begin

                            instr_decode    <= `ins_amoswapd;

                            rs1_en      <= 1'b1;            //rs1 is used

                            rs2_en      <= 1'b1;

                            rd_en       <= 1'b1;            //write back to regfile

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;            //Check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `LSU_AMOSWAP;

                            disp_opinfo <= `Sign64;

                            disp_size   <= 4'h8;            //64bit operation size

                            disp_ds1    <= rs1_data;

                            disp_ds2    <= rs1_data;

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_LSU;

                        end

                        5'd0 :

                        begin

                            instr_decode    <= `ins_amoaddd;

                            rs1_en      <= 1'b1;            //rs1 is used

                            rs2_en      <= 1'b1;

                            rd_en       <= 1'b1;            //write back to regfile

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;            //Check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `LSU_AMOADD;

                            disp_opinfo <= `Sign64;

                            disp_size   <= 4'h8;            //64bit operation size

                            disp_ds1    <= rs1_data;

                            disp_ds2    <= rs1_data;

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_LSU;

                        end

                        5'd4 :

                        begin

                            instr_decode    <= `ins_amoxord;

                            rs1_en      <= 1'b1;            //rs1 is used

                            rs2_en      <= 1'b1;

                            rd_en       <= 1'b1;            //write back to regfile

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;            //Check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `LSU_AMOXOR;

                            disp_opinfo <= `Sign64;

                            disp_size   <= 4'h8;            //64bit operation size

                            disp_ds1    <= rs1_data;

                            disp_ds2    <= rs1_data;

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_LSU;

                        end

                        5'd12 :

                        begin

                            instr_decode    <= `ins_amoandd;

                            rs1_en      <= 1'b1;            //rs1 is used

                            rs2_en      <= 1'b1;

                            rd_en       <= 1'b1;            //write back to regfile

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;            //Check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `LSU_AMOAND;

                            disp_opinfo <= `Sign64;

                            disp_size   <= 4'h8;            //64bit operation size

                            disp_ds1    <= rs1_data;

                            disp_ds2    <= rs1_data;

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_LSU;

                        end

                        5'd8 :

                        begin

                            instr_decode    <= `ins_amoord;

                            rs1_en      <= 1'b1;            //rs1 is used

                            rs2_en      <= 1'b1;

                            rd_en       <= 1'b1;            //write back to regfile

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;            //Check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `LSU_AMOOR;

                            disp_opinfo <= `Sign64;

                            disp_size   <= 4'h8;            //64bit operation size

                            disp_ds1    <= rs1_data;

                            disp_ds2    <= rs1_data;

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_LSU;

                        end

                        5'd16 :

                        begin

                            instr_decode    <= `ins_amomind;

                            rs1_en      <= 1'b1;            //rs1 is used

                            rs2_en      <= 1'b1;

                            rd_en       <= 1'b1;            //write back to regfile

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;            //Check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `LSU_AMOMIN;

                            disp_opinfo <= `Sign64;

                            disp_size   <= 4'h8;            //64bit operation size

                            disp_ds1    <= rs1_data;

                            disp_ds2    <= rs1_data;

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_LSU;

                        end

                        5'd20 :

                        begin

                            instr_decode    <= `ins_amomaxd;

                            rs1_en      <= 1'b1;            //rs1 is used

                            rs2_en      <= 1'b1;

                            rd_en       <= 1'b1;            //write back to regfile

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;            //Check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `LSU_AMOMAX;

                            disp_opinfo <= `Sign64;

                            disp_size   <= 4'h8;            //64bit operation size

                            disp_ds1    <= rs1_data;

                            disp_ds2    <= rs1_data;

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_LSU;

                        end

                        5'd24 :

                        begin

                            instr_decode    <= `ins_amominud;

                            rs1_en      <= 1'b1;            //rs1 is used

                            rs2_en      <= 1'b1;

                            rd_en       <= 1'b1;            //write back to regfile

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;            //Check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `LSU_AMOMIN;

                            disp_opinfo <= `Unsign64;

                            disp_size   <= 4'h8;            //64bit operation size

                            disp_ds1    <= rs1_data;

                            disp_ds2    <= rs1_data;

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_LSU;

                        end

                        5'd28 :

                        begin

                            instr_decode    <= `ins_amomaxud;

                            rs1_en      <= 1'b1;            //rs1 is used

                            rs2_en      <= 1'b1;

                            rd_en       <= 1'b1;            //write back to regfile

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;            //Check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `LSU_AMOMAX;

                            disp_opinfo <= `Unsign64;

                            disp_size   <= 4'h8;            //64bit operation size

                            disp_ds1    <= rs1_data;

                            disp_ds2    <= rs1_data;

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_LSU;

                        end

                        default:

                        begin

                            instr_decode    <= `ins_nop;

                            rs1_en      <= 1'b0;

                            rs2_en      <= 1'b0;

                            rd_en       <= 1'b0;

                            csr_en      <= 1'b0;

                            Checken     <= 1'b0;

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b1;            //this is a illigal instruction

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_NOP;

                            disp_opinfo <= `Sign64;

                            disp_size   <= 4'h8;

                            disp_ds1    <= 64'hx;

                            disp_ds2    <= 64'hx;

                            disp_dest   <= DISP_ALU;

                        end

                    endcase

                end

                else if(funct3==3'b010)begin                //32bit A-extension

                    case(funct5)

                        5'd2 : 

                        begin

                            instr_decode    <= `ins_lrw;

                            rs1_en      <= 1'b1;            //rs1 is used

                            rs2_en      <= 1'b0;

                            rd_en       <= 1'b1;            //write back to regfile

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;            //Check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `LSU_READ_Lock;

                            disp_opinfo <= `Sign32;

                            disp_size   <= 4'h4;            //64bit operation size

                            disp_ds1    <= rs1_data;

                            disp_ds2    <= rs2_data;

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_LSU;

                        end

                        5'd3 :

                        begin

                            instr_decode    <= `ins_scw;

                            rs1_en      <= 1'b1;            //rs1 is used

                            rs2_en      <= 1'b1;

                            rd_en       <= 1'b1;            //write back to regfile

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;            //Check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `LSU_WRITE_Unloc;

                            disp_opinfo <= `Sign32;

                            disp_size   <= 4'h4;            //64bit operation size

                            disp_ds1    <= rs1_data;

                            disp_ds2    <= rs2_data;

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_LSU;

                        end

                        5'd1 :

                        begin

                            instr_decode    <= `ins_amoswapw;

                            rs1_en      <= 1'b1;            //rs1 is used

                            rs2_en      <= 1'b1;

                            rd_en       <= 1'b1;            //write back to regfile

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;            //Check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `LSU_AMOSWAP;

                            disp_opinfo <= `Sign32;

                            disp_size   <= 4'h4;            //64bit operation size

                            disp_ds1    <= rs1_data;

                            disp_ds2    <= rs1_data;

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_LSU;

                        end

                        5'd0 :

                        begin

                            instr_decode    <= `ins_amoaddw;

                            rs1_en      <= 1'b1;            //rs1 is used

                            rs2_en      <= 1'b1;

                            rd_en       <= 1'b1;            //write back to regfile

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;            //Check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `LSU_AMOADD;

                            disp_opinfo <= `Sign32;

                            disp_size   <= 4'h4;            //64bit operation size

                            disp_ds1    <= rs1_data;

                            disp_ds2    <= rs1_data;

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_LSU;

                        end

                        5'd4 :

                        begin

                            instr_decode    <= `ins_amoxorw;

                            rs1_en      <= 1'b1;            //rs1 is used

                            rs2_en      <= 1'b1;

                            rd_en       <= 1'b1;            //write back to regfile

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;            //Check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `LSU_AMOXOR;

                            disp_opinfo <= `Sign32;

                            disp_size   <= 4'h4;            //64bit operation size

                            disp_ds1    <= rs1_data;

                            disp_ds2    <= rs1_data;

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_LSU;

                        end

                        5'd12 :

                        begin

                            instr_decode    <= `ins_amoandw;

                            rs1_en      <= 1'b1;            //rs1 is used

                            rs2_en      <= 1'b1;

                            rd_en       <= 1'b1;            //write back to regfile

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;            //Check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `LSU_AMOAND;

                            disp_opinfo <= `Sign32;

                            disp_size   <= 4'h4;            //64bit operation size

                            disp_ds1    <= rs1_data;

                            disp_ds2    <= rs1_data;

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_LSU;

                        end

                        5'd8 :

                        begin

                            instr_decode    <= `ins_amoorw;

                            rs1_en      <= 1'b1;            //rs1 is used

                            rs2_en      <= 1'b1;

                            rd_en       <= 1'b1;            //write back to regfile

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;            //Check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `LSU_AMOOR;

                            disp_opinfo <= `Sign32;

                            disp_size   <= 4'h4;            //64bit operation size

                            disp_ds1    <= rs1_data;

                            disp_ds2    <= rs1_data;

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_LSU;

                        end

                        5'd16 :

                        begin

                            instr_decode    <= `ins_amominw;

                            rs1_en      <= 1'b1;            //rs1 is used

                            rs2_en      <= 1'b1;

                            rd_en       <= 1'b1;            //write back to regfile

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;            //Check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `LSU_AMOMIN;

                            disp_opinfo <= `Sign32;

                            disp_size   <= 4'h4;            //64bit operation size

                            disp_ds1    <= rs1_data;

                            disp_ds2    <= rs1_data;

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_LSU;

                        end

                        5'd20 :

                        begin

                            instr_decode    <= `ins_amomaxw;

                            rs1_en      <= 1'b1;            //rs1 is used

                            rs2_en      <= 1'b1;

                            rd_en       <= 1'b1;            //write back to regfile

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;            //Check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `LSU_AMOMAX;

                            disp_opinfo <= `Sign32;

                            disp_size   <= 4'h4;            //64bit operation size

                            disp_ds1    <= rs1_data;

                            disp_ds2    <= rs1_data;

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_LSU;

                        end

                        5'd24 :

                        begin

                            instr_decode    <= `ins_amominud;

                            rs1_en      <= 1'b1;            //rs1 is used

                            rs2_en      <= 1'b1;

                            rd_en       <= 1'b1;            //write back to regfile

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;            //Check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `LSU_AMOMIN;

                            disp_opinfo <= `Unsign32;

                            disp_size   <= 4'h4;            //64bit operation size

                            disp_ds1    <= rs1_data;

                            disp_ds2    <= rs1_data;

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_LSU;

                        end

                        5'd28 :

                        begin

                            instr_decode    <= `ins_amomaxud;

                            rs1_en      <= 1'b1;            //rs1 is used

                            rs2_en      <= 1'b1;

                            rd_en       <= 1'b1;            //write back to regfile

                            csr_en      <= 1'b0;

                            Checken     <= 1'b1;            //Check enable

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b0;

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `LSU_AMOMAX;

                            disp_opinfo <= `Unsign32;

                            disp_size   <= 4'h4;            //64bit operation size

                            disp_ds1    <= rs1_data;

                            disp_ds2    <= rs1_data;

                            disp_dest   <= DepdcFind ? DISP_NULL : DISP_LSU;

                        end

                        default:

                        begin

                            instr_decode    <= `ins_nop;

                            rs1_en      <= 1'b0;

                            rs2_en      <= 1'b0;

                            rd_en       <= 1'b0;

                            csr_en      <= 1'b0;

                            Checken     <= 1'b0;

                            Info_jmp    <= 1'b0;

                            Info_ebreak <= 1'b0;

                            Info_ecall  <= 1'b0;

                            Info_illins <= 1'b1;            //this is a illigal instruction

                            Info_mret   <= 1'b0;

                            Info_sret   <= 1'b0;

                            Info_system <= 1'b0;

                            disp_opcode <= `ALU_NOP;

                            disp_opinfo <= `Sign64;

                            disp_size   <= 4'h8;

                            disp_ds1    <= 64'hx;

                            disp_ds2    <= 64'hx;

                            disp_dest   <= DISP_ALU;

                        end

                    endcase

                end

                else begin

                    instr_decode    <= `ins_nop;

                    rs1_en      <= 1'b0;

                    rs2_en      <= 1'b0;

                    rd_en       <= 1'b0;

                    csr_en      <= 1'b0;

                    Checken     <= 1'b0;

                    Info_jmp    <= 1'b0;

                    Info_ebreak <= 1'b0;

                    Info_ecall  <= 1'b0;

                    Info_illins <= 1'b1;            //this is a illigal instruction

                    Info_mret   <= 1'b0;

                    Info_sret   <= 1'b0;

                    Info_system <= 1'b0;

                    disp_opcode <= `ALU_NOP;

                    disp_opinfo <= `Sign64;

                    disp_size   <= 4'h8;

                    disp_ds1    <= 64'hx;

                    disp_ds2    <= 64'hx;

                    disp_dest   <= DISP_ALU;

                end

                default:

					 begin

						instr_decode    <= `ins_nop;

                        rs1_en      <= 1'b0;

                        rs2_en      <= 1'b0;

                        rd_en       <= 1'b0;

                        csr_en      <= 1'b0;

                        Checken     <= 1'b0;

                        Info_jmp    <= 1'b0;

                        Info_ebreak <= 1'b0;

                        Info_ecall  <= 1'b0;

                        Info_illins <= 1'b1;            //this is a illigal instruction

                        Info_mret   <= 1'b0;

                        Info_sret   <= 1'b0;

                        Info_system <= 1'b0;

                        disp_opcode <= `ALU_NOP;

                        disp_opinfo <= `Sign64;

                        disp_size   <= 4'h8;

                        disp_ds1    <= 64'hx;

                        disp_ds2    <= 64'hx;

                        disp_dest   <= DISP_ALU;

					end

            endcase

        end

    end

    else begin                                  //Valid=0, no decode is enable

        rs1_en      <= 1'b0;

        rs2_en      <= 1'b0;

        rd_en       <= 1'b0;

        csr_en      <= 1'b0;

        Checken     <= 1'b0;

        Info_jmp    <= 1'b0;

        Info_ebreak <= 1'b0;

        Info_ecall  <= 1'b0;

        Info_illins <= 1'b0;

        Info_mret   <= 1'b0;

        Info_sret   <= 1'b0;

        Info_system <= 1'b0;

        disp_opcode <= `ALU_NOP;

        disp_opinfo <= `Sign64;

        disp_size   <= 4'h8;

        disp_ds1    <= 64'hx;

        disp_ds2    <= 64'hx;

        disp_dest   <= DISP_NULL;

    end

end

//------------------------------------Branch and jump address generate-----------------------------------

always@(*)begin

    if(Valid)begin

        case(opcode)

            `jal_encode     :                   //jal instruction

            begin

                BP_address  <= imm20_jal + InstructionPC;

                BP_jmp      <= 1'b1;

            end

            `jalr_encode    :                   //jalr

            begin

                BP_address  <= imm12_i + InstructionPC;

                BP_jmp      <= 1'b1;

            end

            `branch_encode  :                   //branch instruction

            case(funct3)

                3'b000 :                    //beq

                begin

                    BP_address  <= imm12_b + InstructionPC;

                    BP_jmp      <= (rs1_data == rs2_data);      //if rs1==rs2, jump

                end

                3'b001 :                    //bne

                begin

                    BP_address  <= imm12_b + InstructionPC;

                    BP_jmp      <= (rs1_data != rs2_data);      //if rs1!=rs2, jump   

                end

                3'b100 :                    //blt

                if(rs1_data[63] & !rs2_data[63])begin           //rs1 is positive, rs2 is negtive

                    BP_address  <= imm12_b + InstructionPC;

                    BP_jmp      <= 1'b0;

                end

                else if(!rs1_data[63] & rs2_data[63])begin           //if rs1 is negtive, rs2 is positive

                    BP_address  <=  imm12_b + InstructionPC;

                    BP_jmp      <=  1'b1;

                end

                else begin

                    BP_address  <=  imm12_b + InstructionPC;

                    BP_jmp      <=  (rs1_data < rs2_data);

                end

                3'b101 :                      //bge

                if(rs1_data[63] & !rs2_data[63])begin           //rs1 is positive, rs2 is negtive

                    BP_address  <= imm12_b + InstructionPC;

                    BP_jmp      <= 1'b1;

                end

                else if(!rs1_data[63] & rs2_data[63])begin           //if rs1 is negtive, rs2 is positive

                    BP_address  <=  imm12_b + InstructionPC;

                    BP_jmp      <=  1'b0;

                end

                else begin

                    BP_address  <=  imm12_b + InstructionPC;

                    BP_jmp      <=  (rs1_data > rs2_data);

                end

                3'b110 :                        //bltu

                begin

                    BP_address  <= imm12_b + InstructionPC;

                    BP_jmp      <= (rs1_data < rs2_data);      //if rs1<rs2, jump   

                end

                3'b111 :                        //bgeu

                begin

                    BP_address  <= imm12_b + InstructionPC;

                    BP_jmp      <= (rs1_data > rs2_data);      //if rs1>rs2, jump   

                end

                default:                                        //Not a branch instruction

                begin

                    BP_address  <= imm12_b + InstructionPC;

                    BP_jmp      <= 1'b0;  

                end



            endcase

            default         :

            begin

                BP_address  <= imm12_b + InstructionPC;

                BP_jmp      <= 1'b0; 

            end

        endcase

    end

    else begin

        BP_address  <= imm12_b + InstructionPC;

        BP_jmp      <= 1'b0;  

    end

end

//----------------------------------------Dispatch Distinction-------------------------------------------



assign disp_ALU = (disp_dest==DISP_ALU);        //dispatch to ALU

assign disp_LSU = (disp_dest==DISP_LSU);        //dispatch to LSU

assign disp_Mcop= (disp_dest==DISP_Mcop);       //dispatch to Math coprocessor



endmodule





