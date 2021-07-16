module lsu(
//CPU侧信号
input wire [15:0]r6_r7_data,	//R6 R7作为地址
input wire [7:0]ds1_data,
input wire mem_read,
input wire mem_write,
output wire mem_ok,
output wire [7:0]lsu_out,
//bus侧信号
output wire [15:0]addr,
output wire [7:0]wdata,
input wire [7:0]rdata,
output wire write,
output wire read,
input wire rdy
);

assign addr	=	(mem_read | mem_write) ? r6_r7_data : 16'b0;
assign wdata=	(mem_read | mem_write) ? ds1_data	: 8'b0;
assign write=	mem_write;
assign read	=	mem_read;


assign mem_ok	=	rdy;
assign lsu_out	=	rdata;

endmodule