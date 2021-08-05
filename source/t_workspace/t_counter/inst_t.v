//generate by EveIDE_LIGHT V0.0.2-alpha 
 reg           Tx_CLKi;
wire          LPCE_DATo;
wire          LPCE_CLKo;
reg           WR_CLK;
reg           WR_RSTn;
reg           WR_EN;
wire          WR_FULL;
reg  [127:0]  WR_DATA;
LPCE_tx inst_LPCE_tx(
    .Tx_CLKi    (Tx_CLKi   ) ,// input width : [0:0]
    .LPCE_DATo  (LPCE_DATo ) ,// output width : [0:0]
    .LPCE_CLKo  (LPCE_CLKo ) ,// output width : [0:0]
    .WR_CLK     (WR_CLK    ) ,// input width : [0:0]
    .WR_RSTn    (WR_RSTn   ) ,// input width : [0:0]
    .WR_EN      (WR_EN     ) ,// input width : [0:0]
    .WR_FULL    (WR_FULL   ) ,// output width : [0:0]
    .WR_DATA    (WR_DATA   )  // input width : [127:0] 

);

reg           GCLKi;
reg           GRSTi;
wire          LPCE_DATo;
wire          LPCE_CLKo;
reg  [127:0]  FIFO_DATAi;
reg           FIFO_EMPTi;
wire          FIFO_READ;
LPCE_tx_front inst_LPCE_tx_front(
    .GCLKi       (GCLKi      ) ,// input width : [0:0]
    .GRSTi       (GRSTi      ) ,// input width : [0:0]
    .LPCE_DATo   (LPCE_DATo  ) ,// output width : [0:0]
    .LPCE_CLKo   (LPCE_CLKo  ) ,// output width : [0:0]
    .FIFO_DATAi  (FIFO_DATAi ) ,// input width : [127:0] 
    .FIFO_EMPTi  (FIFO_EMPTi ) ,// input width : [0:0]
    .FIFO_READ   (FIFO_READ  )  // output width : [0:0]

);

