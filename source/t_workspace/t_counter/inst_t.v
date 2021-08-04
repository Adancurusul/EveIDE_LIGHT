
reg             GCLKi;
reg             GRSTi;
wire            LPCE_DATo;
wire            LPCE_CLKo;
reg    [127:0]  FIFO_DATAi;
reg             FIFO_EMPTi;
wire            FIFO_READ;

LPCE_tx_front inst_LPCE_tx_front(
    .GCLKi           (),
    .GRSTi           (),
    .LPCE_DATo       (),
    .LPCE_CLKo       (),
    .FIFO_DATAi      (),
    .FIFO_EMPTi      (),
    .FIFO_READ       ()
);