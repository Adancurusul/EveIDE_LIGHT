/*

 *    author : Pan
 *    e-mail : 2320025806@qq.com
 *    date   : 20200518
 *    desc   : R408 ultra high speed 8bit RISC I/O processor
 *    version: 0.0
 *	Ultra high speed call and return
 *	Simple & Fast
 *	IPC=1, execept memory read or write


*/
module r408_top(
input wire clk,
input wire rst,
//I-RAM no wait
//sync RAM logic
output wire [15:0]pc,
input wire [15:0]ins,
//D-bus
output wire [15:0]addr,
output wire [7:0]wdata,
input wire [7:0]rdata,
output wire write,
output wire read,
input wire rdy

);

wire [7:0]imm;
wire [7:0]alu_out;	//ALU输出数据
wire [7:0]rd_data;	//送RD数据
wire [7:0]lsu_out;

wire [15:0]r6_r7_data;	//r6和r7数据
wire [15:0]branch_offset;

wire [7:0]ds1_data;
wire [7:0]ds2_data;


assign rd_data = rd_mux1 ? (rd_mux0 ? imm : lsu_out) : alu_out;


id id(
.ins		(ins),

//控制线
//控制线1，运算控制
.alu_add	(alu_add),
.alu_sub	(alu_sub),
.alu_and	(alu_and),
.alu_or		(alu_or),
.alu_xor	(alu_xor),
.alu_sr		(alu_sr),
.alu_sl		(alu_sl),
.alu_sra	(alu_sra),
.alu_slt	(alu_slt),
.alu_eq		(alu_eq),
.alu_neq	(alu_neq),
.unsign		(unsign),		//无符号运算
//多周期控制
.mem_read	(mem_read),		//内存访问
.mem_write	(mem_write),
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
.rd_mux0	(rd_mux0),	//选择rd是imm还是lsu 1=imm 0=rdata
.rd_mux1	(rd_mux1),	//选择rd是lsu还是alu 1=LSU 0=alu

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


.imm		(imm),	//立即数输出
.branch_offset	(branch_offset),	//偏移地址
//特殊功能控制
//特殊功能控制
.ret		(ret),	//返回
.apc		(apc),	//获取pc值
.jmp		(jmp),		//跳转
.bra		(bra)		//分支


);

//寄存器单元
//寄存器单元包含了整个机器所有的控制部分
ru ru(

.clk		(clk),
.rst		(rst),

.pc_next	(pc),

//中断输入
.int0		(int0),
.int1		(int1),
.int2		(int2),
.int3		(int3),
//多周期控制
.mem_read	(mem_read),		//内存访问
.mem_write	(mem_write),
.mem_ok		(mem_ok),
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




.branch_offset	(branch_offset),	//偏移地址
//特殊功能控制
.ret		(ret),	//返回
.apc		(apc),	//获取pc值
.jmp		(jmp),		//跳转
.bra		(bra),		//分支

//状态输出
.main_state	(main_state),

//GPR数据输出
.ds1_data	(ds1_data),
.ds2_data	(ds2_data),
.r6_r7_data	(r6_r7_data),	//地址
.rd_data	(rd_data),
.branch		(branch)			//分支有效


);

alu alu(
.ds1		(ds1_data),
.ds2		(ds2_data),
.imm		(imm),

//控制线
//控制线1，运算控制
.alu_add	(alu_add),
.alu_sub	(alu_sub),
.alu_and	(alu_and),
.alu_or		(alu_or),
.alu_xor	(alu_xor),
.alu_sr		(alu_sr),
.alu_sl		(alu_sl),
.alu_sra	(alu_sra),
.alu_slt	(alu_slt),
.alu_eq		(alu_eq),
.alu_neq	(alu_neq),
.unsign		(unsign),		//无符号运算

.bra		(bra),			//跳转指令

.alu_out	(alu_out),
.branch		(branch)		//跳转允许

);
lsu lsu(
//CPU侧信号
.r6_r7_data	(r6_r7_data),	//R6 R7作为地址
.ds1_data	(ds1_data),
.mem_read	(mem_read),		//内存访问
.mem_write	(mem_write),
.mem_ok		(mem_ok),
.lsu_out	(lsu_out),
//bus侧信号
.addr		(addr),
.wdata		(wdata),
.rdata		(rdata),
.write		(write),
.read		(read),
.rdy		(rdy)
);

endmodule
