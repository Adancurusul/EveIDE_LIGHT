
reg                  ALUi_CLK;
reg                  ALUi_ARST;
reg                  ALUi_Flush;
reg                  PIP_ALUi_MSC_valid;
reg    [7:0]         PIP_ALUi_Opcode;
reg    [1:0]         PIP_ALUi_OpInfo;
reg    [7:0]         PIP_ALUi_INFO_itag;
reg    [1:0]         PIP_ALUi_INFO_priv;
reg    [`XLEN-1:0]   PIP_ALUi_INFO_PC;
reg    [`XLEN-1:0]   PIP_ALUi_DATA_ds1;
reg    [`XLEN-1:0]   PIP_ALUi_DATA_ds2;
wire                 PIP_ALUi_FC_ready;
wire                 PIP_ALUo_MSC_valid;
wire   [`XLEN-1:0]   PIP_ALUo_INFO_itag;
wire   [`XLEN-1:0]   PIP_ALUo_INFO_pc;
wire   [1:0]         PIP_ALUo_INFO_priv;
wire   [`XLEN-1:0]   PIP_ALUo_DATA_data1;
wire   [`XLEN-1:0]   PIP_ALUo_DATA_data2;
reg                  PIP_ALUi_FC_ready;

ALU inst_ALU(
    .ALUi_CLK                 (),
    .ALUi_ARST                (),
    .ALUi_Flush               (),
    .PIP_ALUi_MSC_valid       (),
    .PIP_ALUi_Opcode          (),
    .PIP_ALUi_OpInfo          (),
    .PIP_ALUi_INFO_itag       (),
    .PIP_ALUi_INFO_priv       (),
    .PIP_ALUi_INFO_PC         (),
    .PIP_ALUi_DATA_ds1        (),
    .PIP_ALUi_DATA_ds2        (),
    .PIP_ALUi_FC_ready        (),
    .PIP_ALUo_MSC_valid       (),
    .PIP_ALUo_INFO_itag       (),
    .PIP_ALUo_INFO_pc         (),
    .PIP_ALUo_INFO_priv       (),
    .PIP_ALUo_DATA_data1      (),
    .PIP_ALUo_DATA_data2      (),
    .PIP_ALUi_FC_ready        ()
);