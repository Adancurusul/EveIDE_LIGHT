
reg                  ATUi_CLK;
reg                  ATUi_ARST;
reg                  ATUi_Flush;
reg                  ATUi_ModifyPermit;
reg    [7:0]         ATUi_ModifyPermitID;
reg                  ATUi_TLBrefersh;
wire                 ATUo_TLBrefersh;
reg                  ATUi_CSR_mxr;
reg                  ATUi_CSR_sum;
reg    [`XLEN-1:0]   ATUi_CSR_satp;
reg                  PIP_ATUi_MSC_valid;
reg    [7:0]         PIP_ATUi_Opcode;
reg    [1:0]         PIP_ATUi_OpInfo;
reg    [3:0]         PIP_ATUi_OpSize;
reg    [7:0]         PIP_ATUi_INFO_ITAG;
reg    [1:0]         PIP_ATUi_INFO_priv;
reg                  PIP_ATUi_INFO_unpage;
reg    [`XLEN-1:0]   PIP_ATUi_INFO_PC;
reg    [`XLEN-1:0]   PIP_ATUi_DATA_VA;
reg    [`XLEN-1:0]   PIP_ATUi_DATA_ds1;
reg    [`XLEN-1:0]   PIP_ATUi_DATA_ds2;
reg                  PIP_ATUi_FC_ready;
wire   [7:0]         PIP_ATUo_Opcode;
wire   [1:0]         PIP_ATUo_OpInfo;
wire   [3:0]         PIP_ATUo_OpSize;
wire                 PIP_ATUo_MSC_valid;
wire                 PIP_ATUo_MSC_LoadPageFlt;
wire                 PIP_ATUo_MSC_StorePageFlt;
wire                 PIP_ATUo_MSC_InstPageFlt;
wire   [`XLEN-1:0]   PIP_ATUo_DATA_PA;
wire   [7:0]         PIP_ATUo_INFO_ITAG;
wire   [1:0]         PIP_ATUo_INFO_priv;
wire   [`XLEN-1:0]   PIP_ATUo_INFO_PC;
wire                 PIP_ATUo_DATA_Cacheable;
wire                 PIP_ATUo_DATA_WrThrough;
wire   [`XLEN-1:0]   PIP_ATUo_DATA_ds1;
wire   [`XLEN-1:0]   PIP_ATUo_DATA_ds2;
wire                 PIP_ATUo_FC_ready;
wire                 ATUo_FIB_WREN;
wire                 ATUo_FIB_REQ;
reg                  ATUi_FIB_ACK;
reg                  ATUi_FIB_FULL;
wire   [7:0]         ATUo_FIB_ID;
wire   [7:0]         ATUo_FIB_CMD;
wire   [3:0]         ATUo_FIB_BURST;
wire   [3:0]         ATUo_FIB_SIZE;
wire   [`XLEN-1:0]   ATUo_FIB_ADDR;
wire   [`XLEN-1:0]   ATUo_FIB_DATA;
reg    [7:0]         ATUi_FIB_ID;
reg    [7:0]         ATUi_FIB_RPL;
reg                  ATUi_FIB_V;
reg    [`XLEN-1:0]   ATUi_FIB_DATA;

ATU#(
    .FIB_ID(8'h00)
) inst_ATU(
    .ATUi_CLK                       (),
    .ATUi_ARST                      (),
    .ATUi_Flush                     (),
    .ATUi_ModifyPermit              (),
    .ATUi_ModifyPermitID            (),
    .ATUi_TLBrefersh                (),
    .ATUo_TLBrefersh                (),
    .ATUi_CSR_mxr                   (),
    .ATUi_CSR_sum                   (),
    .ATUi_CSR_satp                  (),
    .PIP_ATUi_MSC_valid             (),
    .PIP_ATUi_Opcode                (),
    .PIP_ATUi_OpInfo                (),
    .PIP_ATUi_OpSize                (),
    .PIP_ATUi_INFO_ITAG             (),
    .PIP_ATUi_INFO_priv             (),
    .PIP_ATUi_INFO_unpage           (),
    .PIP_ATUi_INFO_PC               (),
    .PIP_ATUi_DATA_VA               (),
    .PIP_ATUi_DATA_ds1              (),
    .PIP_ATUi_DATA_ds2              (),
    .PIP_ATUi_FC_ready              (),
    .PIP_ATUo_Opcode                (),
    .PIP_ATUo_OpInfo                (),
    .PIP_ATUo_OpSize                (),
    .PIP_ATUo_MSC_valid             (),
    .PIP_ATUo_MSC_LoadPageFlt       (),
    .PIP_ATUo_MSC_StorePageFlt      (),
    .PIP_ATUo_MSC_InstPageFlt       (),
    .PIP_ATUo_DATA_PA               (),
    .PIP_ATUo_INFO_ITAG             (),
    .PIP_ATUo_INFO_priv             (),
    .PIP_ATUo_INFO_PC               (),
    .PIP_ATUo_DATA_Cacheable        (),
    .PIP_ATUo_DATA_WrThrough        (),
    .PIP_ATUo_DATA_ds1              (),
    .PIP_ATUo_DATA_ds2              (),
    .PIP_ATUo_FC_ready              (),
    .ATUo_FIB_WREN                  (),
    .ATUo_FIB_REQ                   (),
    .ATUi_FIB_ACK                   (),
    .ATUi_FIB_FULL                  (),
    .ATUo_FIB_ID                    (),
    .ATUo_FIB_CMD                   (),
    .ATUo_FIB_BURST                 (),
    .ATUo_FIB_SIZE                  (),
    .ATUo_FIB_ADDR                  (),
    .ATUo_FIB_DATA                  (),
    .ATUi_FIB_ID                    (),
    .ATUi_FIB_RPL                   (),
    .ATUi_FIB_V                     (),
    .ATUi_FIB_DATA                  ()
);