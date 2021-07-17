`include "LPCEconfig.v"
/*********************************************************************
    LPCE Rx module

    note: 1010101010 is sync head
    
*********************************************************************/
module LPCE_rx(
    input wire          LPCE_DATi,
    input wire          LPCE_CLKi,

    output wire         SYNC,                   //Sync head detected, this pin can connect to LED
//READ interface
    input wire          READ_RSTn,
    input wire          READ_CLK,
    input wire          READ_EN,
	output wire [127:0] READ_DATA,
    output wire         READ_EMPT

);
//----------------FIFO write side---------------------------
    wire            WR_CLK;
    wire [127:0]    WR_DATA;
    wire            WR_EN;
//-----------------Sync read reset to write--------------------
    reg             WR_RSTn0;        
    reg             WR_RSTn;
    always@(posedge LPCE_CLKi)begin
        WR_RSTn0 <= READ_RSTn;
        WR_RSTn  <= WR_RSTn0;
    end
//-------------------------FIFO----------------------------
    async_fifo      FIFO1(
        .wclk           (WR_CLK),
        .wrst_n         (WR_RSTn),
        .winc           (WR_EN),
        .wdata          (WR_DATA),
        .wfull          (),
        .awfull         (),
        .rclk           (READ_CLK),
        .rrst_n         (READ_RSTn),
        .rinc           (READ_EN),
        .rdata          (READ_DATA),
        .rempty         (READ_EMPT),
        .arempty        ()
    );
//-----------------------LPCE rx front---------------------
    LPCE_rx_front   LPCE_rx_front(
    .LPCE_DATi          (LPCE_DATi),
    .LPCE_CLKi          (LPCE_CLKi),

    .SYNC               (SYNC),
    .RSTi               (!WR_RSTn),
//----------------------FIFO interface-----------------------
    .FIFO_CLK           (WR_CLK),
    .FIFO_DATA          (WR_DATA),
    .FIFO_WR            (WR_EN)
    );

endmodule







module LPCE_rx_front(
    input wire          LPCE_DATi,
    input wire          LPCE_CLKi,

    input wire          RSTi,
    output wire         SYNC,
//FIFO interface
    output wire         FIFO_CLK,
    output reg [127:0]  FIFO_DATA,
    output wire         FIFO_WR
);
    reg [154:0] SeqReg;                                     //register for bit sequence

    always@(posedge LPCE_CLKi)begin
        if(RSTi)begin
            SeqReg <= 155'b0;
        end
        else begin
            SeqReg <= {SeqReg[153:0],LPCE_DATi};                //Data shift in from right side 
        end
    end

    assign SYNC = (SeqReg[154:145]==`SYNC_HEAD);      //When sync head is detect, SYNC signal set to 1

//-------------When sync head is detected, data locked to SlaveDATAo----------------
    always@(*)begin
            FIFO_DATA[127:120] <= SeqReg[143:136];
            FIFO_DATA[119:112] <= SeqReg[134:127];
            FIFO_DATA[111:104] <= SeqReg[125:118];
            FIFO_DATA[103:96]  <= SeqReg[116:109];
            FIFO_DATA[95:88]   <= SeqReg[107:100];
            FIFO_DATA[87:80]   <= SeqReg[98:91];
            FIFO_DATA[79:72]   <= SeqReg[89:82];
            FIFO_DATA[71:64]   <= SeqReg[80:73];
            FIFO_DATA[63:56]   <= SeqReg[71:64];
            FIFO_DATA[55:48]   <= SeqReg[62:55];
            FIFO_DATA[47:40]   <= SeqReg[53:46];
            FIFO_DATA[39:32]   <= SeqReg[44:37];
            FIFO_DATA[31:24]   <= SeqReg[35:28];
            FIFO_DATA[23:16]   <= SeqReg[26:19];
            FIFO_DATA[15:8]    <= SeqReg[17:10];
            FIFO_DATA[7:0]     <= SeqReg[8:1];
    end
    assign FIFO_WR = SYNC;
    assign FIFO_CLK = LPCE_CLKi;

endmodule