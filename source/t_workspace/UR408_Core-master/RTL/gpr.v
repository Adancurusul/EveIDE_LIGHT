module gpr(
input wire clk,
input wire rst,
//写回控制
//gpr写控制
input wire r0_write,
input wire r1_write,
input wire r2_write,
input wire r3_write,
input wire r4_write,
input wire r5_write,
input wire r6_write,
input wire r7_write,

input wire rd_r0_mux,
input wire rd_r1_mux,

//寄存器索引和立即数
input wire ds1_r0,
input wire ds1_r1,
input wire ds1_r2,
input wire ds1_r3,
input wire ds1_r4,
input wire ds1_r5,
input wire ds1_r6,
input wire ds1_r7,
input wire ds2_r0,
input wire ds2_r1,
input wire ds2_r2,
input wire ds2_r3,
input wire ds2_r4,
input wire ds2_r5,
input wire ds2_r6,
input wire ds2_r7,

input wire [7:0]rd_data,
input wire [15:0]cr_data,
//GPR数据输出
output wire [7:0]ds1_data,
output wire [7:0]ds2_data,
output wire [15:0]r6_r7_data	//R6和R7复用输出

);
reg [7:0]r0;
reg [7:0]r1;
reg [7:0]r2;
reg [7:0]r3;
reg [7:0]r4;
reg [7:0]r5;
reg [7:0]r6;
reg [7:0]r7;

//R 0和R1的赋值逻辑不同
always@(posedge clk)begin
	if(rst)begin
		r0	<=	8'b0;
	end
	else if(r0_write)begin
		r0	<=	rd_r0_mux ? cr_data[7:0] : rd_data;
	end
end
always@(posedge clk)begin
	if(rst)begin
		r1	<=	8'b0;
	end
	else if(r1_write)begin
		r1	<=	rd_r0_mux ? cr_data[15:8] : rd_data;
	end
end
//R2之后的寄存器赋值逻辑相同
always@(posedge clk)begin
	if(rst)begin
		r2 	<=	8'b0;
	end
	else if(r2_write)begin
		r2	<=	rd_data;
	end
end
always@(posedge clk)begin
	if(rst)begin
		r3 	<=	8'b0;
	end
	else if(r3_write)begin
		r3	<=	rd_data;
	end
end
always@(posedge clk)begin
	if(rst)begin
		r4 	<=	8'b0;
	end
	else if(r4_write)begin
		r4	<=	rd_data;
	end
end
always@(posedge clk)begin
	if(rst)begin
		r5 	<=	8'b0;
	end
	else if(r5_write)begin
		r5	<=	rd_data;
	end
end
always@(posedge clk)begin
	if(rst)begin
		r6 	<=	8'b0;
	end
	else if(r6_write)begin
		r6	<=	rd_data;
	end
end
always@(posedge clk)begin
	if(rst)begin
		r7 	<=	8'b0;
	end
	else if(r7_write)begin
		r7	<=	rd_data;
	end
end

assign ds1_data	=	(ds1_r0 ? r0 : 8'b0) |
					(ds1_r1 ? r1 : 8'b0) |
					(ds1_r2 ? r2 : 8'b0) |
					(ds1_r3 ? r3 : 8'b0) |
					(ds1_r4 ? r4 : 8'b0) |
					(ds1_r5 ? r5 : 8'b0) |
					(ds1_r6 ? r6 : 8'b0) |
					(ds1_r7 ? r7 : 8'b0) | 8'b0;

assign ds2_data	=	(ds2_r0 ? r0 : 8'b0) |
					(ds2_r1 ? r1 : 8'b0) |
					(ds2_r2 ? r2 : 8'b0) |
					(ds2_r3 ? r3 : 8'b0) |
					(ds2_r4 ? r4 : 8'b0) |
					(ds2_r5 ? r5 : 8'b0) |
					(ds2_r6 ? r6 : 8'b0) |
					(ds2_r7 ? r7 : 8'b0) | 8'b0;

assign r6_r7_data	=	{r7,r6};


endmodule








