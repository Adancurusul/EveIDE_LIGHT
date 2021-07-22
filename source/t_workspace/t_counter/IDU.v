`include "../RTL/PRV564Config.v"
`include "../RTL/PRV564Define.v"
//////////////////////////////////////////////////////////////////////////////////////////////////
//  Date    : 2021                                                                              //
//  Author  : Jack.Pan                                                                          //
//  Desc    : Instructions Decode Unit For PRV564 processor                                     //
//  Version : 0.0(Orignal)                                                                      //
//////////////////////////////////////////////////////////////////////////////////////////////////
module IDU(
//--------------------Global Signals-----------------------
    input wire              IDUi_CLK,
    input wire              IDUi_ARST,
    input wire              IDUi_Flush,            //Flush IDU (Global FLush)
//------------------CSR read interface----------------------
    input wire              IDUi_CSR_tvm,
    input wire              IDUi_CSR_tsr,
    input wire              IDUi_CSR_mpriv,
    input wire [1:0]        IDUi_CSR_mpp,
    input wire [`XLEN-1:0]  IDUi_CSR_data,          //CSR data
    output wire [11:0]      IDUo_CSR_index,         //CSR index
    output wire             IDUo_CSR_en,            //read csr enable
//-----------------Regfile(General Perpose Register) read interface---------------------
    output wire [4:0]       IDUo_GPR_rs1index,
    output wire             IDUo_GPR_rs1en,
    input wire  [`XLEN-1:0] IDUi_GPR_rs1data,
    output wire [4:0]       IDUo_GPR_rs2index,
    output wire             IDUo_GPR_rs2en,
    input wire  [`XLEN-1:0] IDUi_GPR_rs2data,
//-------------------------DITF Check interface----------------------------
    output wire             IDUo_Checken,           //check enable
    output wire[4:0]        IDUo_CheckRs1Index,     //rs1 index for check
    output wire             IDUo_CheckRs1en,        //rs1 index for check is enable
    output wire[4:0]        IDUo_CheckRs2Index,     //rs2 index for check
    output wire             IDUo_CheckRs2en,        //rs2 index for check is enable
    output wire[11:0]       IDUo_CheckCSRIndex,     //csr index for check
    output wire             IDUo_CheckCSRen,        //csr index for check is enable
    input wire              IDUi_DepdcFind,         //A dependencies is found
//--------------------------DITF Write Interface---------------------------
    output reg              IDUo_DITF_write,        //Write enable (add a new entry)
    output wire[7:0]        IDUo_DITF_itag,
    output wire[4:0]        IDUo_DITF_rs1index,
    output wire             IDUo_DITF_rs1en,
    output wire[4:0]        IDUo_DITF_rs2index,
    output wire             IDUo_DITF_rs2en,
    output wire[4:0]        IDUo_DITF_rdindex,
    output wire             IDUo_DITF_rden,
    output wire[11:0]       IDUo_DITF_csrindex,
    output wire             IDUo_DITF_csren,
    output wire             IDUo_DITF_jmp,
    output wire             IDUo_DITF_InsAccessFlt,
    output wire             IDUo_DITF_InsPageFlt,
    output wire             IDUo_DITF_InsAddrMis,
    output wire             IDUo_DITF_illins,
    output wire             IDUo_DITF_mret,
    output wire             IDUo_DITF_sret,
    output wire             IDUo_DITF_ecall,
    output wire             IDUo_DITF_ebreak,
    output wire             IDUo_DITF_system,
    input wire              IDUi_DITF_empty,            //DITF is empty now
//-----------FLush & ModifyPermit interface---------
    output wire             IDUo_ModifyPermit,          //Instruction Front Modify is permit
    output wire[`XLEN-1:0]  IDUo_BPC,
    output wire             IDUo_BFlush,                //Flush instruction front
//----------------Pipline input--------------------
    input wire              PIP_IDUi_MSC_valid,         //current instruction is valid
    input wire [`XLEN-1:0]  PIP_IDUi_DATA_instr,        //intruction input (64bit and aligned对齐的)
    input wire [`XLEN-1:0]  PIP_IDUi_INFO_pc,           //current pc
    input wire [1:0]        PIP_IDUi_INFO_priv,
    input wire              PIP_IDUi_MSC_InstPageFlt,
    input wire              PIP_IDUi_MSC_InstAddrMis,
    input wire              PIP_IDUi_MSC_InstAccFlt,
    output reg              PIP_IDUo_FC_ready,
//---------------ALU interface----------------------
    output reg              PIP_ALUi_MSC_valid,
    output reg  [`XLEN-1:0] PIP_ALUi_INFO_pc,
    output reg  [1:0]       PIP_ALUi_INFO_priv,
    output reg  [7:0]       PIP_ALUi_INFO_ITAG,
    output reg  [7:0]       PIP_ALUi_Opcode,
    output reg  [3:0]       PIP_ALUi_OpSize,
    output reg  [1:0]       PIP_ALUi_OPInfo,
    output reg  [`XLEN-1:0] PIP_ALUi_DATA_ds1,
    output reg  [`XLEN-1:0] PIP_ALUi_DATA_ds2,          
    input wire              PIP_ALUo_FC_ready,          //ALU is ready to go
//---------------LSU interface-----------------------
    output reg              PIP_LSUi_MSC_valid,
    output reg  [`XLEN-1:0] PIP_LSUi_INFO_pc,
    output reg  [1:0]       PIP_LSUi_INFO_priv,
    output reg  [7:0]       PIP_LSUi_INFO_ITAG,
    output reg              PIP_LSUi_INFO_unpage,       //unpage mode is on
    output reg  [7:0]       PIP_LSUi_Opcode,
    output reg  [3:0]       PIP_LSUi_OpSize,
    output reg  [1:0]       PIP_LSUi_OPInfo,
    output reg  [`XLEN-1:0] PIP_LSUi_DATA_ds1,
    output reg  [`XLEN-1:0] PIP_LSUi_DATA_ds2,          
    input wire              PIP_LSUo_FC_ready,          //LSU is ready to go
//---------------Math Coprocessor interface----------
    output reg              PIP_Mcopi_MSC_valid,
    output reg  [`XLEN-1:0] PIP_Mcopi_INFO_pc,
    output reg  [1:0]       PIP_Mcopi_INFO_priv,
    output reg  [7:0]       PIP_Mcopi_INFO_ITAG,
    output reg  [7:0]       PIP_Mcopi_Opcode,
    output reg  [3:0]       PIP_Mcopi_OpSize,
    output reg  [1:0]       PIP_Mcopi_OPInfo,
    output reg  [`XLEN-1:0] PIP_Mcopi_DATA_ds1,
    output reg  [`XLEN-1:0] PIP_Mcopi_DATA_ds2,          
    input wire              PIP_Mcopo_FC_ready           //Math coprocessor is ready to go


);
//-----------------------------Instruction and global valid--------------------------------
    wire [31:0]     Instruction;                           //Instruction
    wire            Valid;                                 //Global Valid in IDU
assign Instruction  = PIP_IDUi_INFO_pc[2] ? PIP_IDUi_DATA_instr[63:32] : PIP_IDUi_DATA_instr[31:0];
assign Valid        = IDUi_Flush ? 1'b0 : PIP_IDUi_MSC_valid;
//------------------------------ITAG generate enable---------------------------------------
    reg             ITAG_EN;
//----------------------------dispatch target and dispatch opcode--------------------------
    wire            disp_ALU, disp_LSU, disp_Mcop;          //dispatch target
    wire [7:0]      disp_opcode;
    wire [1:0]      disp_opinfo;
    wire [3:0]      disp_opsize;                            //dispatch operation size
    wire [`XLEN-1:0]disp_ds1, disp_ds2;                     //dispatch data source
//-----------------------------Branch address and jump enable------------------------------
    wire [`XLEN-1:0]BP_address;
    wire            BP_jump_pending;                        //一个跳转正在等待，表明当前指令需要进行跳转
    reg             BP_Flag;                                //分支标志位，表面当前BP冲刷信号已经发出，切勿发出第二次
//-------------------------------Instruction Decode Core-----------------------------------
// ID core将当前指令解码到将要派遣的每个管线上
IDcore              inst_IDcore(
    .CSR_tvm            (IDUi_CSR_tsr),
    .CSR_tsr            (IDUi_CSR_tsr),
    .InstrPriv          (PIP_IDUi_INFO_priv),
    .Instruction        (Instruction),
    .InstructionPC      (PIP_IDUi_INFO_pc),
    .Valid              (Valid),
    .InsAccessFlt       (PIP_IDUi_MSC_InstAccFlt),
    .InsPageFlt         (PIP_IDUi_MSC_InstPageFlt),
    .InsAddrMis         (PIP_IDUi_MSC_InstAddrMis),
    .rs1_index          (IDUo_CheckRs1Index),
    .rs1_en             (IDUo_CheckRs1en),
    .rs2_index          (IDUo_CheckRs2Index),
    .rs2_en             (IDUo_CheckRs2en),
    .rs1_data           (IDUi_GPR_rs1data),
    .rs2_data           (IDUi_GPR_rs2data),
    .rd_index           (IDUo_DITF_rdindex),
    .rd_en              (IDUo_DITF_rden),
    .csr_index          (IDUo_CheckCSRIndex),
    .csr_en             (IDUo_CheckCSRen),
    .CSR_data           (IDUi_CSR_data),
    .Checken            (IDUo_Checken),
    .DepdcFind          (IDUi_DepdcFind),
    .Info_jmp           (IDUo_DITF_jmp),
    .Info_illins        (IDUo_DITF_illins),
    .Info_mret          (IDUo_DITF_mret),
    .Info_sret          (IDUo_DITF_sret),
    .Info_ecall         (IDUo_DITF_ecall),
    .Info_ebreak        (IDUo_DITF_ebreak),
    .Info_system        (IDUo_DITF_system),
    .BP_address         (BP_address),
    .BP_jmp             (BP_jump_pending),
    .disp_ALU           (disp_ALU),
    .disp_LSU           (disp_LSU),
    .disp_Mcop          (disp_Mcop),
    .disp_opcode        (disp_opcode),
    .disp_opinfo        (disp_opinfo),
    .disp_size          (disp_opsize),
    .disp_ds1           (disp_ds1),
    .disp_ds2           (disp_ds2)
);
//-------------------------------Read CSR and GPR----------------------------
assign IDUo_GPR_rs1index    = IDUo_CheckRs1Index;
assign IDUo_GPR_rs1en       = IDUo_CheckRs1en;
assign IDUo_GPR_rs2index    = IDUo_CheckRs2Index;
assign IDUo_GPR_rs2en       = IDUo_CheckRs2en;
assign IDUo_CSR_index       = IDUo_CheckCSRIndex;
assign IDUo_CSR_en          = IDUo_CheckCSRen;
//-------------------------------TAG generate core---------------------------
TAGgen      ITAG_generate(
    .CLKi               (IDUi_CLK),             //clock input
    .ARSTi              (IDUi_ARST),            //Async reset input
    .ENi                (ITAG_EN),              //随机数产生使能，为1时在下一个cycle生成新的随机数，为0时保持
    .DATAo              (IDUo_DITF_itag)        //随机数输出
);
always@(*) begin
    if(PIP_IDUi_MSC_valid & PIP_IDUo_FC_ready)begin
        ITAG_EN <= 1'b1;
    end
    else begin
        ITAG_EN <= 1'b0;
    end
end
//----------------------Modufy permit and Instruction front flush-------------
assign IDUo_ModifyPermit = IDUi_DITF_empty;             //如果DITF为空，则流水线后面已经没有指令了，前级可以进行更改
assign IDUo_BPC          = BP_address;
assign IDUo_BFlush       = BP_jump_pending & !BP_Flag;  //如果当前跳转正在等待，且Flag没有置1，则可以跳转
always@(posedge IDUi_CLK or posedge IDUi_ARST)begin
    if(IDUi_ARST)begin
        BP_Flag <= 1'b0;
    end
    else begin
        case(BP_Flag)
            1'b0 : if(BP_jump_pending & !PIP_IDUo_FC_ready)begin
                        BP_Flag <= 1'b1;
                    end
            1'b1 :  if(PIP_IDUo_FC_ready)begin
                        BP_Flag <= 1'b0;
                    end
        endcase
    end
end
//-------------------------------dispatch to ALU port-------------------------
always@(posedge IDUi_CLK or posedge IDUi_ARST)begin
    if(IDUi_ARST)begin
        PIP_ALUi_MSC_valid  <= 1'b0;
        PIP_ALUi_INFO_pc    <= 63'b0;
        PIP_ALUi_INFO_priv  <= `Machine;
        PIP_ALUi_INFO_ITAG  <= 8'b0;
        PIP_ALUi_Opcode     <= `ALU_NOP;
        PIP_ALUi_OpSize     <= 4'h0;
        PIP_ALUi_OPInfo     <= `Sign64;
        PIP_ALUi_DATA_ds1   <= 64'h0;
        PIP_ALUi_DATA_ds2   <= 64'h0;
    end
    else if(PIP_ALUi_MSC_valid & !PIP_ALUo_FC_ready)begin  //如果派遣的管线中有一条指令但是指令没有准备好，则输出保持
        PIP_ALUi_MSC_valid  <= PIP_ALUi_MSC_valid;
        PIP_ALUi_INFO_pc    <= PIP_ALUi_INFO_pc;
        PIP_ALUi_INFO_priv  <= PIP_ALUi_INFO_priv;
        PIP_ALUi_INFO_ITAG  <= PIP_ALUi_INFO_ITAG;
        PIP_ALUi_Opcode     <= PIP_ALUi_Opcode;
        PIP_ALUi_OpSize     <= PIP_ALUi_OpSize;
        PIP_ALUi_OPInfo     <= PIP_ALUi_OPInfo;
        PIP_ALUi_DATA_ds1   <= PIP_ALUi_DATA_ds1;
        PIP_ALUi_DATA_ds2   <= PIP_ALUi_DATA_ds2;
    end
    else begin
        PIP_ALUi_MSC_valid  <= disp_ALU;
        PIP_ALUi_INFO_pc    <= PIP_IDUi_INFO_pc;
        PIP_ALUi_INFO_priv  <= PIP_IDUi_INFO_priv;
        PIP_ALUi_INFO_ITAG  <= IDUo_DITF_itag;
        PIP_ALUi_Opcode     <= disp_opcode;
        PIP_ALUi_OpSize     <= disp_opsize;
        PIP_ALUi_OPInfo     <= disp_opinfo;
        PIP_ALUi_DATA_ds1   <= disp_ds1;
        PIP_ALUi_DATA_ds2   <= disp_ds2;
    end
end
//-----------------------------dispatch to LSU port------------------------------
always@(posedge IDUi_CLK or posedge IDUi_ARST)begin
    if(IDUi_ARST)begin
        PIP_LSUi_MSC_valid  <= 1'b0;
        PIP_LSUi_INFO_pc    <= 63'b0;
        PIP_LSUi_INFO_priv  <= `Machine;
        PIP_LSUi_INFO_ITAG  <= 8'b0;
        PIP_LSUi_INFO_unpage<= 1'b0;
        PIP_LSUi_Opcode     <= `LSU_NOP;
        PIP_LSUi_OpSize     <= 4'h0;
        PIP_LSUi_OPInfo     <= `Sign64;
        PIP_LSUi_DATA_ds1   <= 64'h0;
        PIP_LSUi_DATA_ds2   <= 64'h0;
    end
    else if(PIP_LSUi_MSC_valid & !PIP_LSUo_FC_ready)begin  //如果派遣的管线中有一条指令但是指令没有准备好，则输出保持
        PIP_LSUi_MSC_valid  <= PIP_LSUi_MSC_valid;
        PIP_LSUi_INFO_pc    <= PIP_LSUi_INFO_pc;
        PIP_LSUi_INFO_priv  <= PIP_LSUi_INFO_priv;
        PIP_LSUi_INFO_ITAG  <= PIP_LSUi_INFO_ITAG;
        PIP_LSUi_INFO_unpage<= PIP_LSUi_INFO_unpage;
        PIP_LSUi_Opcode     <= PIP_LSUi_Opcode;
        PIP_LSUi_OpSize     <= PIP_LSUi_OpSize;
        PIP_LSUi_OPInfo     <= PIP_LSUi_OPInfo;
        PIP_LSUi_DATA_ds1   <= PIP_LSUi_DATA_ds1;
        PIP_LSUi_DATA_ds2   <= PIP_LSUi_DATA_ds2;
    end
    else begin
        PIP_LSUi_MSC_valid  <= disp_LSU;
        PIP_LSUi_INFO_pc    <= PIP_IDUi_INFO_pc;
        PIP_LSUi_INFO_priv  <= PIP_IDUi_INFO_priv;
        PIP_LSUi_INFO_ITAG  <= IDUo_DITF_itag;
        PIP_LSUi_INFO_unpage<= ((PIP_IDUi_INFO_priv == `Machine) & IDUi_CSR_mpriv & (IDUi_CSR_mpp==`Machine)) ? 1'b1 : 1'b0;
        PIP_LSUi_Opcode     <= disp_opcode;
        PIP_LSUi_OpSize     <= disp_opsize;
        PIP_LSUi_OPInfo     <= disp_opinfo;
        PIP_LSUi_DATA_ds1   <= disp_ds1;
        PIP_LSUi_DATA_ds2   <= disp_ds2;
    end
end
//----------------------------Math Coprocessor Port------------------------------
always@(posedge IDUi_CLK or posedge IDUi_ARST)begin
    if(IDUi_ARST)begin
        PIP_Mcopi_MSC_valid  <= 1'b0;
        PIP_Mcopi_INFO_pc    <= 63'b0;
        PIP_Mcopi_INFO_priv  <= `Machine;
        PIP_Mcopi_INFO_ITAG  <= 8'b0;
        PIP_Mcopi_Opcode     <= `Mcop_NOP;
        PIP_Mcopi_OpSize     <= 4'h0;
        PIP_Mcopi_OPInfo     <= `Sign64;
        PIP_Mcopi_DATA_ds1   <= 64'h0;
        PIP_Mcopi_DATA_ds2   <= 64'h0;
    end
    else if(PIP_Mcopi_MSC_valid & !PIP_Mcopo_FC_ready)begin  //如果派遣的管线中有一条指令但是指令没有准备好，则输出保持
        PIP_Mcopi_MSC_valid  <= PIP_Mcopi_MSC_valid;
        PIP_Mcopi_INFO_pc    <= PIP_Mcopi_INFO_pc;
        PIP_Mcopi_INFO_priv  <= PIP_Mcopi_INFO_priv;
        PIP_Mcopi_INFO_ITAG  <= PIP_Mcopi_INFO_ITAG;
        PIP_Mcopi_Opcode     <= PIP_Mcopi_Opcode;
        PIP_Mcopi_OpSize     <= PIP_Mcopi_OpSize;
        PIP_Mcopi_OPInfo     <= PIP_Mcopi_OPInfo;
        PIP_Mcopi_DATA_ds1   <= PIP_Mcopi_DATA_ds1;
        PIP_Mcopi_DATA_ds2   <= PIP_Mcopi_DATA_ds2;
    end
    else begin
        PIP_Mcopi_MSC_valid  <= disp_Mcop;
        PIP_Mcopi_INFO_pc    <= PIP_IDUi_INFO_pc;
        PIP_Mcopi_INFO_priv  <= PIP_IDUi_INFO_priv;
        PIP_Mcopi_INFO_ITAG  <= IDUo_DITF_itag;
        PIP_Mcopi_Opcode     <= disp_opcode;
        PIP_Mcopi_OpSize     <= disp_opsize;
        PIP_Mcopi_OPInfo     <= disp_opinfo;
        PIP_Mcopi_DATA_ds1   <= disp_ds1;
        PIP_Mcopi_DATA_ds2   <= disp_ds2;
    end
end
//-----------------------------DITF write & ready--------------------------------
assign IDUo_DITF_InsAddrMis     = PIP_IDUi_MSC_InstAddrMis;
assign IDUo_DITF_InsAccessFlt   = PIP_IDUi_MSC_InstAccFlt;
assign IDUo_DITF_InsPageFlt     = PIP_IDUi_MSC_InstPageFlt;
assign IDUo_DITF_rs1index       = IDUo_CheckRs1Index;
assign IDUo_DITF_rs1en          = IDUo_CheckRs1en;
assign IDUo_DITF_rs2index       = IDUo_CheckRs2Index;
assign IDUo_DITF_rs2en          = IDUo_CheckRs2en;
assign IDUo_DITF_csrindex       = IDUo_CheckCSRIndex;
assign IDUo_DITF_csren          = IDUo_CheckCSRen;
always@(*)begin
    if(PIP_IDUi_MSC_valid)begin
        if(disp_ALU)begin
            PIP_IDUo_FC_ready <= (PIP_ALUi_MSC_valid^PIP_ALUo_FC_ready) ? 1'b0 : 1'b1;      //if valid output = ready, 即valid，ready=0，0和1，1，表示派遣成功，否则不成功 
            IDUo_DITF_write   <= (PIP_ALUi_MSC_valid^PIP_ALUo_FC_ready) ? 1'b0 : 1'b1;      //if valid 和 ready 均为1或者均为0，表示后级有指令且准备好或无指令，可以派遣
        end
        else if(disp_LSU)begin
            PIP_IDUo_FC_ready <= (PIP_LSUi_MSC_valid^PIP_LSUo_FC_ready) ? 1'b0 : 1'b1;
            IDUo_DITF_write   <= (PIP_LSUi_MSC_valid^PIP_LSUo_FC_ready) ? 1'b0 : 1'b1;      
        end
        else if(disp_LSU)begin
            PIP_IDUo_FC_ready <= (PIP_Mcopi_MSC_valid^PIP_Mcopo_FC_ready) ? 1'b0 : 1'b1;
            IDUo_DITF_write   <= (PIP_Mcopi_MSC_valid^PIP_Mcopo_FC_ready) ? 1'b0 : 1'b1;      
        end
        else begin
            PIP_IDUo_FC_ready <= IDUi_Flush ? 1'b1 : 1'b0;  //if no dispatch, the instruction is waiting
            IDUo_DITF_write   <= 1'b0;
        end
    end
    else begin
        PIP_IDUo_FC_ready <= 1'b0;
        IDUo_DITF_write   <= 1'b0;
    end
end

endmodule
