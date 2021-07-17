// Copyright (C) 2018  Intel Corporation. All rights reserved.
// Your use of Intel Corporation's design tools, logic functions 
// and other software and tools, and its AMPP partner logic 
// functions, and any output files from any of the foregoing 
// (including device programming or simulation files), and any 
// associated documentation or information are expressly subject 
// to the terms and conditions of the Intel Program License 
// Subscription Agreement, the Intel Quartus Prime License Agreement,
// the Intel FPGA IP License Agreement, or other applicable license
// agreement, including, without limitation, that your use is for
// the sole purpose of programming logic devices manufactured by
// Intel and sold by Intel or its authorized distributors.  Please
// refer to the applicable agreement for further details.

// *****************************************************************************
// This file contains a Verilog test bench template that is freely editable to  
// suit user's needs .Comments are provided in each section to help the user    
// fill out necessary details.                                                  
// *****************************************************************************
// Generated on "05/01/2021 14:20:10"
                                                                                
// Verilog Test Bench template for design : LPCE_PHY
// 
// Simulation tool : ModelSim (Verilog)
// 

`timescale 1 ns/ 1 ps
module LPCE_PHY_tb();

// test vector input registers
	reg 		READ_CLK;
	reg 		READ_EN;
	reg 		READ_RSTn;
	reg 		Tx_CLKi;
	reg 		WR_CLK;
	reg [127:0]	WR_DATA;
	reg 		WR_EN;
	reg 		WR_RSTn;
// wires                                               
	wire 		LPCE_CLK;
	wire 		LPCE_DAT;
	wire [127:0]READ_DATA;
	wire 		READ_EMPT;
	wire 		SYNC;
	wire 		WR_FULL;

// assign statements (if any)                          
LPCE_PHY LPCE_PHY (
// port map - connection between master ports and signals/registers   
	.LPCE_CLKi		(LPCE_CLK),
	.LPCE_CLKo		(LPCE_CLK),
	.LPCE_DATi		(LPCE_DAT),
	.LPCE_DATo		(LPCE_DAT),
	.READ_CLK		(READ_CLK),
	.READ_DATA		(READ_DATA),
	.READ_EMPT		(READ_EMPT),
	.READ_EN		(READ_EN),
	.READ_RSTn		(READ_RSTn),
	.SYNC			(SYNC),
	.Tx_CLKi		(Tx_CLKi),
	.WR_CLK			(WR_CLK),
	.WR_DATA		(WR_DATA),
	.WR_EN			(WR_EN),
	.WR_FULL		(WR_FULL),
	.WR_RSTn		(WR_RSTn)
);

initial
begin            
    $dumpfile ("wave.vcd") ;        //生成的vcd文件名称
    $dumpvars(0, LPCE_PHY_tb);    //tb模块名称
end   

initial                                                
begin                                                  
// code that executes only once                        
// insert code here --> begin                          
	Tx_CLKi 	= 1'b0;
	READ_CLK	= 1'b0;
	WR_CLK		= 1'b0;
	READ_RSTn	= 1'b0;
	READ_EN 	= 1'b1;			//always read enable
	WR_RSTn		= 1'b0;
	WR_DATA		= 128'haaaa_aaaa_5555_5555;
#100 
	WR_RSTn		= 1'b1;
	READ_RSTn	= 1'b1;
	WR_EN 		= 1'b1;



// --> end                                                                
end                                                    
always                                                 
//-----------generate clock signal----------
begin                                                  
    
	#5 	Tx_CLKi = ~Tx_CLKi;			//Tx CLK = 100MHz (T=10ns)
                                            
end     
always begin
	#16	READ_CLK= ~READ_CLK;		//READ CLK=33MHz
		WR_CLK	= ~WR_CLK;			//WR CLK = 33MHz
end             
always@(posedge WR_CLK)begin
	WR_DATA <= WR_DATA + 1;
end                                  
endmodule

