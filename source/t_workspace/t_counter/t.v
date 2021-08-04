`include "LPCEconfig.v"
/************************************************************************************
    Low Pin Connection Express (LPCE) transmitter
Detail  :|<-------------------------Sync Head----------------------->|
LPC_DATo:<  1     0     1     0     1     0     1     0     1     0  ><b153><b152><b125><b124> // <b000>
LPC_CLKo:___/--\__/--\__/--\__/--\__/--\__/--\__/--\__/--\__/--\__/--\__/--\__/--\__/--\__/--\_//___/--\
    Every 8bit convert to 9bit

    control timing
GCLK        :\__/--\__/--\__/-//__/--\__/--\__/--\__/--\__/--\__/--\__/--\__/--\__/--\__/--\__/--\
FIFO_DATAi :---<DATA0>-------//--------<DATA1>

    NOTE: Frame frim frame at least inseart 2 zeros.
************************************************************************************/
module LPCE_tx(
    input  wire        Tx_CLKi,             //Tx reference clock (equal to Bode rate)
    output wire         LPCE_DATo,           //Serial Data output
    output wire         LPCE_CLKo,           //Serial Data output
    //---------Tx interface--------------
    input wire          WR_CLK,
    input wire          WR_RSTn,
    input wire          WR_EN,
    output wire         WR_FULL,
    input wire [127:0]  WR_DATA
);
    wire [127:0] FIFO_DATA;
    wire         FIFO_EMPT;
    wire         FIFO_READ;

    reg          Tx_RST;
    reg          Tx_RST0;
    //-------Sync Tx front's reset to Tx clock------
    always@(posedge Tx_CLKi)begin
        Tx_RST0 <= ~WR_RSTn;
        Tx_RST  <= Tx_RST0;
    end

    LPCE_tx_front       LPCE_tx_front(
    .GCLKi                  (Tx_CLKi),              //Tx clock
    .GRSTi                  (Tx_RST),              //Global reset input
    .LPCE_DATo              (LPCE_DATo),           //Serial Data output
    .LPCE_CLKo              (LPCE_CLKo),           //Serial Data output
    .FIFO_DATAi             (FIFO_DATA),           //
    .FIFO_EMPTi             (FIFO_EMPT),
    .FIFO_READ              (FIFO_READ)

    );
//----------------FIFO (in )---------------
    async_fifo      FIFO1(
        .wclk           (WR_CLK),
        .wrst_n         (WR_RSTn),
        .winc           (WR_EN),
        .wdata          (WR_DATA),
        .wfull          (WR_FULL),
        .awfull         (),
        //Read port is sync to Tx front
        .rclk           (Tx_CLKi),
        .rrst_n         (!Tx_RST),
        .rinc           (FIFO_READ),
        .rdata          (FIFO_DATA),
        .rempty         (FIFO_EMPT),
        .arempty        ()
    );

endmodule


/*f asdfa   asdf*//*1qqqa   asdf
 asdf*/
 
module LPCE_tx_front(
    input  wire         GCLKi,              //Global clock input
    input  wire         GRSTi,              //Global reset input
    output wire         LPCE_DATo,           //Serial Data output
    output wire         LPCE_CLKo,           //Serial Data output
    input  wire [127:0] FIFO_DATAi,        //
    input  wire         FIFO_EMPTi,
    output wire         FIFO_READ

);
    reg                         StateReg;               //state contral
    reg [7 : 0]   Counter;                //bit counter
    reg [154:0]                 SeqReg;                 //Sequence data register

    always@(posedge GCLKi)begin:StateMachine
        if(GRSTi)begin
            StateReg <= 1'b0;
        end
        else begin
            case(StateReg)
                1'b0    :   StateReg <= (!FIFO_EMPTi) ? 1'b1 : StateReg;       //if FIFO is NOT empty, Tx enable
                1'b1    :   if(Counter == 8'b00)begin
                                StateReg <= 1'b0;
                            end
				endcase
        end
    end
//---------Send bit sequence generate----------
    always@(posedge GCLKi)begin:SeqRegister
        if(GRSTi)begin
            SeqReg <= 155'b0;
        end
        else if(!FIFO_EMPTi & !StateReg)begin                //is FIFO is NOT empty and state is in standby, bit seq reg is load
            SeqReg[154:145]     <= `SYNC_HEAD;
            SeqReg[144:135]     <=  {FIFO_DATAi[127],FIFO_DATAi[127:120],FIFO_DATAi[120]};
            SeqReg[134:126]     <=  {FIFO_DATAi[119:112],FIFO_DATAi[112]};
            SeqReg[125:117]     <=  {FIFO_DATAi[111:104],FIFO_DATAi[104]};
            SeqReg[116:108]     <=  {FIFO_DATAi[103:96],FIFO_DATAi[96]};
            SeqReg[107:99]      <=  {FIFO_DATAi[95:88],FIFO_DATAi[88]};
            SeqReg[98:90]       <=  {FIFO_DATAi[87:80],FIFO_DATAi[80]};
            SeqReg[89:81]       <=  {FIFO_DATAi[79:72],FIFO_DATAi[72]};
            SeqReg[80:72]       <=  {FIFO_DATAi[71:64],FIFO_DATAi[64]};
            SeqReg[71:63]       <=  {FIFO_DATAi[63:56],FIFO_DATAi[56]};
            SeqReg[62:54]       <=  {FIFO_DATAi[55:48],FIFO_DATAi[48]};
            SeqReg[53:45]       <=  {FIFO_DATAi[47:40],FIFO_DATAi[40]};
            SeqReg[44:36]       <=  {FIFO_DATAi[39:32],FIFO_DATAi[32]};
            SeqReg[35:27]       <=  {FIFO_DATAi[31:24],FIFO_DATAi[24]};
            SeqReg[26:18]       <=  {FIFO_DATAi[23:16],FIFO_DATAi[16]};
            SeqReg[17:9]        <=  {FIFO_DATAi[15:8],FIFO_DATAi[8]};
            SeqReg[8:0]         <=  {FIFO_DATAi[7:0],FIFO_DATAi[0]};
        end
        else begin
            SeqReg <= (SeqReg << 1);        //MSB first
        end
    end
//-----------Send bit counter-------------
    always@(posedge GCLKi)begin
        if(FIFO_READ)begin
            Counter <= (`FRAME_LENGTH);   //When send is enable, counter load the frame length total send 156 bits(include 0 in the end)
        end
        else begin
            Counter <= Counter - 8'h1;
        end
    end
//----------Done output-------------------
    assign FIFO_READ = !StateReg & !FIFO_EMPTi;
//-----------LPCE Interface----------------
    assign LPCE_DATo = SeqReg[154];          //MSB shift out first
    assign LPCE_CLKo = ~GCLKi;               //GCLK is use as refclock

endmodule


