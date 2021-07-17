
reg              LPCE_DATi;
reg              LPCE_CLKi;
wire             SYNC;
reg              READ_RSTn;
reg              READ_CLK;
reg              READ_EN;
wire   [127:0]   READ_DATA;
wire             READ_EMPT;
reg              LPCE_DATi;
reg              LPCE_CLKi;
reg              RSTi;
wire             SYNC;
wire             FIFO_CLK;
wire   [127:0]   FIFO_DATA;
wire             FIFO_WR;

LPCE_rx inst_LPCE_rx(
    .LPCE_DATi      (),
    .LPCE_CLKi      (),
    .SYNC           (),
    .READ_RSTn      (),
    .READ_CLK       (),
    .READ_EN        (),
    .READ_DATA      (),
    .READ_EMPT      (),
    .LPCE_DATi      (),
    .LPCE_CLKi      (),
    .RSTi           (),
    .SYNC           (),
    .FIFO_CLK       (),
    .FIFO_DATA      (),
    .FIFO_WR        ()
);