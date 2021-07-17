protDeclare::::
reg              LPCE_CLKi;
reg              LPCE_DATi;
wire             LPCE_CLKo;
wire             LPCE_DATo;
reg              Tx_CLKi;
wire             SYNC;
reg              READ_RSTn;
reg              READ_CLK;
reg              READ_EN;
wire   [127:0]   READ_DATA;
wire             READ_EMPT;
reg              WR_CLK;
reg              WR_RSTn;
reg              WR_EN;
wire             WR_FULL;
reg    [127:0]   WR_DATA;

moduleName:::LPCE_PHYpataInst::: inst_moduleName:::LPCE_PHYprotInst:::(
    .LPCE_CLKi      (),
    .LPCE_DATi      (),
    .LPCE_CLKo      (),
    .LPCE_DATo      (),
    .Tx_CLKi        (),
    .SYNC           (),
    .READ_RSTn      (),
    .READ_CLK       (),
    .READ_EN        (),
    .READ_DATA      (),
    .READ_EMPT      (),
    .WR_CLK         (),
    .WR_RSTn        (),
    .WR_EN          (),
    .WR_FULL        (),
    .WR_DATA        ()
);