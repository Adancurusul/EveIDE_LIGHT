/*****************************************************************
    Physical interface of Low Pin Connection Express(LPCE)
*****************************************************************/
module LPCE_PHY(
    //----LPCE Rx Interface-----
    input wire          LPCE_CLKi,
    input wire          LPCE_DATi,
    //----LPCE Tx Interface-----
    output wire         LPCE_CLKo,
    output wire         LPCE_DATo,
    //Reference clock
    input wire         Tx_CLKi,                 //Hi speed Tx refCLK

    output wire         SYNC,                   //Sync head detected, this pin can connect to LED
//READ interface
    input wire          READ_RSTn,              //Reset
    input wire          READ_CLK,               //Read clock
    input wire          READ_EN,                //Read enable
	output wire [127:0] READ_DATA,              //
    output wire         READ_EMPT,              //current FIFO is empty
//write interface
    input wire          WR_CLK,                 //write clock
    input wire          WR_RSTn,                //write reset
    input wire          WR_EN,                  //write enable
    output wire         WR_FULL,                //write FIFO full
    input wire [127:0]  WR_DATA                 //write data

);

//-----Tx module-----
    LPCE_tx                 TxU(
        .Tx_CLKi                (Tx_CLKi),
        .LPCE_DATo              (LPCE_DATo),           //Serial Data output
        .LPCE_CLKo              (LPCE_CLKo),           //Serial Data output
    //---------Tx interface--------------
        .WR_CLK                 (WR_CLK),
        .WR_RSTn                (WR_RSTn),
        .WR_EN                  (WR_EN),
        .WR_FULL                (WR_FULL),
        .WR_DATA                (WR_DATA)
    );
//-----Rx module------
    LPCE_rx                 RxU(
        .LPCE_DATi              (LPCE_DATi),
        .LPCE_CLKi              (LPCE_CLKi),
        .SYNC                   (SYNC),                 //Sync head detected, this pin can connect to LED
//READ interface
        .READ_RSTn              (READ_RSTn),
        .READ_CLK               (READ_CLK),
        .READ_EN                (READ_EN),
	    .READ_DATA              (READ_DATA),
        .READ_EMPT              (READ_EMPT)
    );

endmodule