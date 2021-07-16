module ru(

input wire clk,
input wire rst,

output wire [15:0]pc_next,

input wire int0,
input wire int1,
input wire int2,
input wire int3,
//多周期控制
input wire mem_read,		//内存访问
input wire mem_write,
input wire mem_ok,
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
input wire rd_mux0,	//选择rd是imm还是lsu 1=imm 0=rdata
input wire rd_mux1,	//选择rd是lsu还是alu 1=LSU 0=alu
input wire rd_r0_mux,
input wire rd_r1_mux,
//cr写控制
input wire statu_sel,
input wire ie_sel,
input wire epc_sel,
input wire cpc_sel,
input wire temp_sel,
input wire tcev0_sel,
input wire tcev1_sel,
input wire tcev2_sel,
input wire tcev3_sel,

input wire cr_write,
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

input wire [15:0]branch_offset,	//偏移地址
//特殊功能控制
input wire ret,	//返回
input wire apc,	//获取pc值
input wire jmp,		//跳转
input wire bra,		//分支

//状态输出
output wire main_state,

//GPR数据输出
output wire [7:0]ds1_data,
output wire [7:0]ds2_data,
output wire [15:0]r6_r7_data,	//地址
input wire [7:0]rd_data,
input wire branch			//分支有效


);

wire [15:0]cr_data;




cr cr(
.clk		(clk),
.rst		(rst),

.pc_next	(pc_next),
//中断输入
.int0		(int0),
.int1		(int1),
.int2		(int2),
.int3		(int3),

//多周期控制
.mem_read	(mem_read),		//内存访问
.mem_write	(mem_write),
.mem_ok		(mem_ok),

.branch		(branch),

.main_state	(main_state),

//cr写控制
.statu_sel	(statu_sel),
.ie_sel		(ie_sel),
.epc_sel	(epc_sel),
.cpc_sel	(cpc_sel),
.temp_sel	(temp_sel),
.tcev0_sel	(tcev0_sel),
.tcev1_sel	(tcev1_sel),
.tcev2_sel	(tcev2_sel),
.tcev3_sel	(tcev3_sel),

.cr_write	(cr_write),

.branch_offset	(branch_offset),	//偏移地址
//特殊功能控制
.ret		(ret),	//返回
.apc		(apc),	//获取pc值
.jmp		(jmp),		//跳转
.bra		(bra),		//分支

.r6_r7_data	(r6_r7_data),
.cr_data	(cr_data)

);

gpr gpr(
.clk		(clk),
.rst		(rst),
//写回控制
//gpr写控制
.r0_write	(r0_write),
.r1_write	(r1_write),
.r2_write	(r2_write),
.r3_write	(r3_write),
.r4_write	(r4_write),
.r5_write	(r5_write),
.r6_write	(r6_write),
.r7_write	(r7_write),

.rd_r0_mux	(rd_r0_mux),
.rd_r1_mux	(rd_r1_mux),

//寄存器索引和立即数
.ds1_r0		(ds1_r0),
.ds1_r1		(ds1_r1),
.ds1_r2		(ds1_r2),
.ds1_r3		(ds1_r3),
.ds1_r4		(ds1_r4),
.ds1_r5		(ds1_r5),
.ds1_r6		(ds1_r6),
.ds1_r7		(ds1_r7),
.ds2_r0		(ds2_r0),
.ds2_r1		(ds2_r1),
.ds2_r2		(ds2_r2),
.ds2_r3		(ds2_r3),
.ds2_r4		(ds2_r4),
.ds2_r5		(ds2_r5),
.ds2_r6		(ds2_r6),
.ds2_r7		(ds2_r7),

.rd_data	(rd_data),
.cr_data	(cr_data),
//GPR数据输出
.ds1_data	(ds1_data),
.ds2_data	(ds2_data),
.r6_r7_data	(r6_r7_data)	//R6和R7复用输出

);



endmodule









