
reg              Tx_CLKi;
wire             LPCE_DATo;
wire             LPCE_CLKo;
reg              WR_CLK;
reg              WR_RSTn;
reg              WR_EN;
wire             WR_FULL;
reg    [127:0]   WR_DATA;
reg              GCLKi;
reg              GRSTi;
wire             LPCE_DATo;
wire             LPCE_CLKo;
reg    [127:0]   FIFO_DATAi;
reg              FIFO_EMPTi;
wire             FIFO_READ;

LPCE_tx inst_LPCE_tx(
    .Tx_CLKi         (),
    .LPCE_DATo       (),
    .LPCE_CLKo       (),
    .WR_CLK          (),
    .WR_RSTn         (),
    .WR_EN           (),
    .WR_FULL         (),
    .WR_DATA         (),
    .GCLKi           (),
    .GRSTi           (),
    .LPCE_DATo       (),
    .LPCE_CLKo       (),
    .FIFO_DATAi      (),
    .FIFO_EMPTi      (),
    .FIFO_READ       ()
);