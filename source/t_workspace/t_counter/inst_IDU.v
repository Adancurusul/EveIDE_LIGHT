
reg                  IDUi_CLK;
reg                  IDUi_ARST;
reg                  IDUi_Flush;
reg                  IDUi_CSR_tvm;
reg                  IDUi_CSR_tsr;
reg                  IDUi_CSR_mpriv;
reg    [1:0]         IDUi_CSR_mpp;
reg    [`XLEN-1:0]   IDUi_CSR_data;
wire   [11:0]        IDUo_CSR_index;
wire                 IDUo_CSR_en;
wire   [4:0]         IDUo_GPR_rs1index;
wire                 IDUo_GPR_rs1en;
reg    [`XLEN-1:0]   IDUi_GPR_rs1data;
wire   [4:0]         IDUo_GPR_rs2index;
wire                 IDUo_GPR_rs2en;
reg    [`XLEN-1:0]   IDUi_GPR_rs2data;
wire                 IDUo_Checken;
wire                 IDUo_CheckRs1en;
wire                 IDUo_CheckRs2en;
wire                 IDUo_CheckCSRen;
reg                  IDUi_DepdcFind;
wire                 IDUo_DITF_write;
wire                 IDUo_DITF_rs1en;
wire                 IDUo_DITF_rs2en;
wire                 IDUo_DITF_rden;
wire                 IDUo_DITF_csren;
wire                 IDUo_DITF_jmp;
wire                 IDUo_DITF_InsAccessFlt;
wire                 IDUo_DITF_InsPageFlt;
wire                 IDUo_DITF_InsAddrMis;
wire                 IDUo_DITF_illins;
wire                 IDUo_DITF_mret;
wire                 IDUo_DITF_sret;
wire                 IDUo_DITF_ecall;
wire                 IDUo_DITF_ebreak;
wire                 IDUo_DITF_system;
reg                  IDUi_DITF_empty;
wire                 IDUo_ModifyPermit;
wire                 IDUo_BFlush;
reg                  PIP_IDUi_MSC_valid;
reg    [`XLEN-1:0]   PIP_IDUi_DATA_instr;
reg    [`XLEN-1:0]   PIP_IDUi_INFO_pc;
reg    [1:0]         PIP_IDUi_INFO_priv;
reg                  PIP_IDUi_MSC_InstPageFlt;
reg                  PIP_IDUi_MSC_InstAddrMis;
reg                  PIP_IDUi_MSC_InstAccFlt;
wire                 PIP_IDUo_FC_ready;
wire                 PIP_ALUi_MSC_valid;
wire   [`XLEN-1:0]   PIP_ALUi_INFO_pc;
wire   [1:0]         PIP_ALUi_INFO_priv;
wire   [7:0]         PIP_ALUi_INFO_ITAG;
wire   [7:0]         PIP_ALUi_Opcode;
wire   [3:0]         PIP_ALUi_OpSize;
wire   [1:0]         PIP_ALUi_OPInfo;
wire   [`XLEN-1:0]   PIP_ALUi_DATA_ds1;
wire   [`XLEN-1:0]   PIP_ALUi_DATA_ds2;
reg                  PIP_ALUo_FC_ready;
wire                 PIP_LSUi_MSC_valid;
wire   [`XLEN-1:0]   PIP_LSUi_INFO_pc;
wire   [1:0]         PIP_LSUi_INFO_priv;
wire   [7:0]         PIP_LSUi_INFO_ITAG;
wire                 PIP_LSUi_INFO_unpage;
wire   [7:0]         PIP_LSUi_Opcode;
wire   [3:0]         PIP_LSUi_OpSize;
wire   [1:0]         PIP_LSUi_OPInfo;
wire   [`XLEN-1:0]   PIP_LSUi_DATA_ds1;
wire   [`XLEN-1:0]   PIP_LSUi_DATA_ds2;
reg                  PIP_LSUo_FC_ready;
wire                 PIP_Mcopi_MSC_valid;
wire   [`XLEN-1:0]   PIP_Mcopi_INFO_pc;
wire   [1:0]         PIP_Mcopi_INFO_priv;
wire   [7:0]         PIP_Mcopi_INFO_ITAG;
wire   [7:0]         PIP_Mcopi_Opcode;
wire   [3:0]         PIP_Mcopi_OpSize;
wire   [1:0]         PIP_Mcopi_OPInfo;
wire   [`XLEN-1:0]   PIP_Mcopi_DATA_ds1;
wire   [`XLEN-1:0]   PIP_Mcopi_DATA_ds2;
reg                  PIP_Mcopo_FC_ready;

IDU inst_IDU(
    .IDUi_CLK                      (),
    .IDUi_ARST                     (),
    .IDUi_Flush                    (),
    .IDUi_CSR_tvm                  (),
    .IDUi_CSR_tsr                  (),
    .IDUi_CSR_mpriv                (),
    .IDUi_CSR_mpp                  (),
    .IDUi_CSR_data                 (),
    .IDUo_CSR_index                (),
    .IDUo_CSR_en                   (),
    .IDUo_GPR_rs1index             (),
    .IDUo_GPR_rs1en                (),
    .IDUi_GPR_rs1data              (),
    .IDUo_GPR_rs2index             (),
    .IDUo_GPR_rs2en                (),
    .IDUi_GPR_rs2data              (),
    .IDUo_Checken                  (),
    .IDUo_CheckRs1en               (),
    .IDUo_CheckRs2en               (),
    .IDUo_CheckCSRen               (),
    .IDUi_DepdcFind                (),
    .IDUo_DITF_write               (),
    .IDUo_DITF_rs1en               (),
    .IDUo_DITF_rs2en               (),
    .IDUo_DITF_rden                (),
    .IDUo_DITF_csren               (),
    .IDUo_DITF_jmp                 (),
    .IDUo_DITF_InsAccessFlt        (),
    .IDUo_DITF_InsPageFlt          (),
    .IDUo_DITF_InsAddrMis          (),
    .IDUo_DITF_illins              (),
    .IDUo_DITF_mret                (),
    .IDUo_DITF_sret                (),
    .IDUo_DITF_ecall               (),
    .IDUo_DITF_ebreak              (),
    .IDUo_DITF_system              (),
    .IDUi_DITF_empty               (),
    .IDUo_ModifyPermit             (),
    .IDUo_BFlush                   (),
    .PIP_IDUi_MSC_valid            (),
    .PIP_IDUi_DATA_instr           (),
    .PIP_IDUi_INFO_pc              (),
    .PIP_IDUi_INFO_priv            (),
    .PIP_IDUi_MSC_InstPageFlt      (),
    .PIP_IDUi_MSC_InstAddrMis      (),
    .PIP_IDUi_MSC_InstAccFlt       (),
    .PIP_IDUo_FC_ready             (),
    .PIP_ALUi_MSC_valid            (),
    .PIP_ALUi_INFO_pc              (),
    .PIP_ALUi_INFO_priv            (),
    .PIP_ALUi_INFO_ITAG            (),
    .PIP_ALUi_Opcode               (),
    .PIP_ALUi_OpSize               (),
    .PIP_ALUi_OPInfo               (),
    .PIP_ALUi_DATA_ds1             (),
    .PIP_ALUi_DATA_ds2             (),
    .PIP_ALUo_FC_ready             (),
    .PIP_LSUi_MSC_valid            (),
    .PIP_LSUi_INFO_pc              (),
    .PIP_LSUi_INFO_priv            (),
    .PIP_LSUi_INFO_ITAG            (),
    .PIP_LSUi_INFO_unpage          (),
    .PIP_LSUi_Opcode               (),
    .PIP_LSUi_OpSize               (),
    .PIP_LSUi_OPInfo               (),
    .PIP_LSUi_DATA_ds1             (),
    .PIP_LSUi_DATA_ds2             (),
    .PIP_LSUo_FC_ready             (),
    .PIP_Mcopi_MSC_valid           (),
    .PIP_Mcopi_INFO_pc             (),
    .PIP_Mcopi_INFO_priv           (),
    .PIP_Mcopi_INFO_ITAG           (),
    .PIP_Mcopi_Opcode              (),
    .PIP_Mcopi_OpSize              (),
    .PIP_Mcopi_OPInfo              (),
    .PIP_Mcopi_DATA_ds1            (),
    .PIP_Mcopi_DATA_ds2            (),
    .PIP_Mcopo_FC_ready            ()
);