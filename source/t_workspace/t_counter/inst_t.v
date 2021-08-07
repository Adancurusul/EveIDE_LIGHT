wire           Tx_CLKi  ;
wire           LPCE_DATo;
wire           LPCE_CLKo;

wire           WR_CLK   ;
wire           WR_RSTn  ;
wire           WR_EN    ;
wire           WR_FULL  ;
wire [127:0]   WR_DATA  ;


LPCE_tx LPCE_tx_U0
(
.Tx_CLKi                        ( Tx_CLKi                        ),
.LPCE_DATo                      ( LPCE_DATo                      ),
.LPCE_CLKo                      ( LPCE_CLKo                      ),

.WR_CLK                         ( WR_CLK                         ),
.WR_RSTn                        ( WR_RSTn                        ),
.WR_EN                          ( WR_EN                          ),
.WR_FULL                        ( WR_FULL                        ),
.WR_DATA                        ( WR_DATA                        )
);

wire          GCLKi     ;
wire          GRSTi     ;
wire          LPCE_DATo ;
wire          LPCE_CLKo ;
wire [127:0]  FIFO_DATAi;
wire          FIFO_EMPTi;
wire          FIFO_READ ;


LPCE_tx_front LPCE_tx_front_U0
(
.GCLKi                          ( GCLKi                          ),
.GRSTi                          ( GRSTi                          ),
.LPCE_DATo                      ( LPCE_DATo                      ),
.LPCE_CLKo                      ( LPCE_CLKo                      ),
.FIFO_DATAi                     ( FIFO_DATAi                     ),
.FIFO_EMPTi                     ( FIFO_EMPTi                     ),
.FIFO_READ                      ( FIFO_READ                      )
);

