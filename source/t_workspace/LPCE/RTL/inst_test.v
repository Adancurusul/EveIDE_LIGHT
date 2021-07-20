
reg                  CSR_tvm;
reg                  CSR_tsr;
reg    [1:0]         InstrPriv;
reg    [31:0]        Instruction;
reg    [`XLEN-1:0]   InstructionPC;
reg                  Valid;
reg                  InsAccessFlt;
reg                  InsPageFlt;
reg                  InsAddrMis;
wire   [4:0]         rs1_index;
wire                 rs1_en;
wire   [4:0]         rs2_index;
wire                 rs2_en;
reg    [`XLEN-1:0]   rs1_data;
reg    [`XLEN-1:0]   rs2_data;
wire   [4:0]         rd_index;
wire                 rd_en;
wire   [11:0]        csr_index;
wire                 csr_en;
reg    [`XLEN-1:0]   CSR_data;
wire                 Checken;
reg                  DepdcFind;
wire                 Info_jmp;
wire                 Info_illins;
wire                 Info_mret;
wire                 Info_sret;
wire                 Info_ecall;
wire                 Info_ebreak;
wire                 Info_system;
wire   [`XLEN-1:0]   BP_address;
wire                 BP_jmp;
wire                 disp_ALU;
wire                 disp_LSU;
wire                 disp_Mcop;
wire   [7:0]         disp_opcode;
wire   [1:0]         disp_opinfo;
wire   [3:0]         disp_size;
wire   [`XLEN-1:0]   disp_ds1;
wire   [`XLEN-1:0]   disp_ds2;

IDcore#(
    .DISP_NULL(4'h0),
    .DISP_ALU (4'h1),
    .DISP_LSU (4'h2),
    .DISP_Mcop(4'h4)
) inst_IDcore(
    .CSR_tvm            (),
    .CSR_tsr            (),
    .InstrPriv          (),
    .Instruction        (),
    .InstructionPC      (),
    .Valid              (),
    .InsAccessFlt       (),
    .InsPageFlt         (),
    .InsAddrMis         (),
    .rs1_index          (),
    .rs1_en             (),
    .rs2_index          (),
    .rs2_en             (),
    .rs1_data           (),
    .rs2_data           (),
    .rd_index           (),
    .rd_en              (),
    .csr_index          (),
    .csr_en             (),
    .CSR_data           (),
    .Checken            (),
    .DepdcFind          (),
    .Info_jmp           (),
    .Info_illins        (),
    .Info_mret          (),
    .Info_sret          (),
    .Info_ecall         (),
    .Info_ebreak        (),
    .Info_system        (),
    .BP_address         (),
    .BP_jmp             (),
    .disp_ALU           (),
    .disp_LSU           (),
    .disp_Mcop          (),
    .disp_opcode        (),
    .disp_opinfo        (),
    .disp_size          (),
    .disp_ds1           (),
    .disp_ds2           ()
);