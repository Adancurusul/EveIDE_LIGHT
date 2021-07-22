`include "../RTL/PRV564Config.v"
`include "../RTL/PRV564Define.v"
//////////////////////////////////////////////////////////////////////////////////////////////////
//  Date    : 2021                                                                              //
//  Author  : Jack.Pan                                                                          //
//  Desc    : ALU for PRV564 processor                                                          //
//  Version : 0.0(Orininal Verision)                                                            //
//////////////////////////////////////////////////////////////////////////////////////////////////
module ALU(
//-------------------Global Signals------------------------
    input  wire             ALUi_CLK,
    input  wire             ALUi_ARST,
    input  wire             ALUi_Flush,
//------------------Pipline Input Signals------------------
    input  wire             PIP_ALUi_MSC_valid,         //操作有效
    input  wire [7:0]       PIP_ALUi_Opcode,            //ALU操作码
    input  wire [1:0]       PIP_ALUi_OpInfo,            //ALU操作信息
    input  wire [7:0]       PIP_ALUi_INFO_itag,
    input  wire [1:0]       PIP_ALUi_INFO_priv,         //权限
    input  wire [`XLEN-1:0] PIP_ALUi_INFO_PC,           //Instruction Infomation: PC value
    input  wire [`XLEN-1:0] PIP_ALUi_DATA_ds1,
    input  wire [`XLEN-1:0] PIP_ALUi_DATA_ds2,
    output  reg             PIP_ALUi_FC_ready,
//--------------------Pipline Output Signals----------------
    output reg              PIP_ALUo_MSC_valid,
    output reg [`XLEN-1:0]  PIP_ALUo_INFO_itag,
    output reg [`XLEN-1:0]  PIP_ALUo_INFO_pc,
    output reg [1:0]        PIP_ALUo_INFO_priv,
    output reg [`XLEN-1:0]  PIP_ALUo_DATA_data1,        //data1 output, for GPR write back
    output reg [`XLEN-1:0]  PIP_ALUo_DATA_data2,        //data2 output, for CSR write back
    input wire              PIP_ALUi_FC_ready           //write back is ready to go
);
    wire [`XLEN-1:0]    DataOut1, DataOut2;
    wire                Valid;
assign Valid = ALUi_Flush ? 1'b0 : PIP_ALUi_MSC_valid;
//--------------------------ALU compute core-----------------------
ALUcore         ALUcore(
    .Valid              (Valid),
    .Opcode             (PIP_ALUi_Opcode),
    .OpInfo             (PIP_ALUi_OpInfo),
    .DataSource1        (PIP_ALUi_DATA_ds1),
    .DataSource2        (PIP_ALUi_DATA_ds2),
    .DataOut1           (DataOut1),
    .DataOut2           (DataOut2)
);
//-----------------------Output registers----------------------
always@(posedge ALUi_CLK or posedge ALUi_ARST)begin
    if(ALUi_ARST)begin
        PIP_ALUo_MSC_valid  <= 1'b0;
        PIP_ALUo_INFO_itag  <= 8'h00;
        PIP_ALUo_INFO_pc    <= 64'h0;
        PIP_ALUo_INFO_priv  <= `Machine;
        PIP_ALUo_DATA_data1 <= 64'h0;
        PIP_ALUo_DATA_data2 <= 64'h0;
    end
    else if(PIP_ALUo_MSC_valid & !PIP_ALUi_FC_ready)begin
        PIP_ALUo_MSC_valid  <= PIP_ALUo_MSC_valid;
        PIP_ALUo_INFO_itag  <= PIP_ALUo_INFO_itag;
        PIP_ALUo_INFO_pc    <= PIP_ALUo_INFO_pc;
        PIP_ALUo_INFO_priv  <= PIP_ALUo_INFO_priv;
        PIP_ALUo_DATA_data1 <= PIP_ALUo_DATA_data1;
        PIP_ALUo_DATA_data2 <= PIP_ALUo_DATA_data2;
    end
    else begin
        PIP_ALUo_MSC_valid  <= Valid;
        PIP_ALUo_INFO_itag  <= PIP_ALUi_INFO_itag;
        PIP_ALUo_INFO_pc    <= PIP_ALUi_INFO_PC;
        PIP_ALUo_INFO_priv  <= PIP_ALUi_INFO_priv;
        PIP_ALUo_DATA_data1 <= DataOut1;
        PIP_ALUo_DATA_data2 <= DataOut2;
    end
end

endmodule