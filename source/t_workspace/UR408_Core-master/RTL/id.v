module id(
input wire [15:0]ins,

//控制线
//控制线1，运算控制
output wire alu_add,
output wire alu_sub,
output wire alu_and,
output wire alu_or,
output wire alu_xor,
output wire alu_sr,
output wire alu_sl,
output wire alu_sra,
output wire alu_slt,
output wire alu_eq,
output wire alu_neq,
output wire unsign,		//无符号运算
//多周期控制
output wire mem_read,		//内存访问
output wire mem_write,
//写回控制
//gpr写控制
output wire r0_write,
output wire r1_write,
output wire r2_write,
output wire r3_write,
output wire r4_write,
output wire r5_write,
output wire r6_write,
output wire r7_write,
output wire rd_mux0,	//选择rd是imm还是lsu 1=imm 0=rdata
output wire rd_mux1,	//选择rd是lsu还是alu 1=LSU 0=alu
output wire rd_r0_mux,
output wire rd_r1_mux,
//cr写控制
output wire statu_sel,
output wire ie_sel,
output wire epc_sel,
output wire cpc_sel,
output wire temp_sel,
output wire tcev0_sel,
output wire tcev1_sel,
output wire tcev2_sel,
output wire tcev3_sel,

output wire cr_write,
//寄存器索引和立即数
output wire ds1_r0,
output wire ds1_r1,
output wire ds1_r2,
output wire ds1_r3,
output wire ds1_r4,
output wire ds1_r5,
output wire ds1_r6,
output wire ds1_r7,
output wire ds2_r0,
output wire ds2_r1,
output wire ds2_r2,
output wire ds2_r3,
output wire ds2_r4,
output wire ds2_r5,
output wire ds2_r6,
output wire ds2_r7,


output wire [7:0]imm,	//立即数输出
output wire [15:0]branch_offset,	//偏移地址
//特殊功能控制
output wire bra,	//分支
output wire ret,	//返回
output wire apc,	//获取pc值
output wire jmp		//跳转

);
parameter opcode_r	=	2'b00;
parameter opcode_b	=	2'b01;
parameter opcode_sys=	2'b10;
parameter opcode_ls	=	2'b11;

parameter funct4_0	=	4'h0;
parameter funct4_1	=	4'h1;
parameter funct4_2	=	4'h2;
parameter funct4_3	=	4'h3;
parameter funct4_4	=	4'h4;
parameter funct4_5	=	4'h5;
parameter funct4_6	=	4'h6;
parameter funct4_7	=	4'h7;
parameter funct4_8	=	4'h8;
parameter funct4_9	=	4'h9;
parameter funct4_a	=	4'ha;
parameter funct4_b	=	4'hb;
parameter funct4_c	=	4'hb;
parameter funct4_d	=	4'hd;
parameter funct4_e	=	4'he;
parameter funct4_f	=	4'hf;

parameter statu_index=	7'h0;
parameter ie_index	=	7'h1;
parameter epc_index	=	7'h2;
parameter cpc_index = 	7'h3;
parameter temp_index=	7'h4;
parameter tvec0_index=	7'h5;
parameter tvec1_index=	7'h6;
parameter tvec2_index=	7'h7;
parameter tvec3_index=	7'h8;

//控制线
//控制线1，运算控制
assign alu_add	=	(ins[1:0]==opcode_r) & (ins[5:2]==funct4_0);
assign alu_sub	=	(ins[1:0]==opcode_r) & (ins[5:2]==funct4_1);
assign alu_and	=	(ins[1:0]==opcode_r) & (ins[5:2]==funct4_2);
assign alu_or	=	(ins[1:0]==opcode_r) & (ins[5:2]==funct4_3);
assign alu_xor	=	(ins[1:0]==opcode_r) & (ins[5:2]==funct4_4);
assign alu_sr	=	(ins[1:0]==opcode_r) & ((ins[5:2]==funct4_5)|(ins[5:2]==funct4_7));
assign alu_sl	=	(ins[1:0]==opcode_r) & (ins[5:2]==funct4_6);
assign alu_sra	=	(ins[1:0]==opcode_r) & (ins[5:2]==funct4_7);
assign alu_slt	=	(ins[1:0]==opcode_r) & ((ins[5:2]==funct4_8)|(ins[5:2]==funct4_9));
assign alu_sltu	=	(ins[1:0]==opcode_r) & (ins[5:2]==funct4_9);
assign alu_eq	=	(ins[1:0]==opcode_r) & (ins[5:2]==funct4_a);
assign alu_neq	=	(ins[1:0]==opcode_r) & (ins[5:2]==funct4_b);
assign unsign	=	alu_sra | alu_sltu;

assign mem_read	=	(ins[1:0]==opcode_ls) & (ins[5:2]==funct4_8);
assign mem_write=	(ins[1:0]==opcode_ls) & (ins[5:2]==funct4_9);

//gpr写控制
assign r0_write =	(ins[1:0]==opcode_r) & (ins[8:6]==3'b000) | 
					(ins[1:0]==opcode_ls) & ((ins[5:2]==funct4_9) | (ins[5:2]==funct4_0)) & (ins[8:6]==3'b000)|	//LS指令的LI和LB也可以写GPR
					(ins[1:0]==opcode_sys)&((ins[5:2]==funct4_4));	//JL和APC，RCR指令也可以写R0 R1寄存器
assign r1_write =	(ins[1:0]==opcode_r) & (ins[8:6]==3'b001) | 
					(ins[1:0]==opcode_ls) & ((ins[5:2]==funct4_9) | (ins[5:2]==funct4_0)) & (ins[8:6]==3'b001)|
					(ins[1:0]==opcode_sys)&((ins[5:2]==funct4_4));	//JL和APC，RCR指令也可以写R0 R1寄存器
assign r2_write	=	(ins[1:0]==opcode_r) & (ins[8:6]==3'b010) | 
					(ins[1:0]==opcode_ls) & ((ins[5:2]==funct4_9) | (ins[5:2]==funct4_0)) & (ins[8:6]==3'b010);
assign r3_write	=	(ins[1:0]==opcode_r) & (ins[8:6]==3'b011) | 
					(ins[1:0]==opcode_ls) & ((ins[5:2]==funct4_9) | (ins[5:2]==funct4_0)) & (ins[8:6]==3'b011);
assign r4_write	=	(ins[1:0]==opcode_r) & (ins[8:6]==3'b100) | 
					(ins[1:0]==opcode_ls) & ((ins[5:2]==funct4_9) | (ins[5:2]==funct4_0)) & (ins[8:6]==3'b100);
assign r5_write	=	(ins[1:0]==opcode_r) & (ins[8:6]==3'b101) | 
					(ins[1:0]==opcode_ls) & ((ins[5:2]==funct4_9) | (ins[5:2]==funct4_0)) & (ins[8:6]==3'b101);
assign r6_write	=	(ins[1:0]==opcode_r) & (ins[8:6]==3'b110) | 
					(ins[1:0]==opcode_ls) & ((ins[5:2]==funct4_9) | (ins[5:2]==funct4_0)) & (ins[8:6]==3'b110);
assign r7_write	=	(ins[1:0]==opcode_r) & (ins[8:6]==3'b111) | 
					(ins[1:0]==opcode_ls) & ((ins[5:2]==funct4_9) | (ins[5:2]==funct4_0)) & (ins[8:6]==3'b111);
					
assign rd_mux0	=	(ins[5:2]==funct4_0);	//选择rd是imm还是lsu
assign rd_mux1	=	(ins[1:0]==opcode_ls);	//选择rd是lsu还是alu
assign rd_r0_mux=	(ins[1:0]==opcode_sys)&((ins[5:2]==funct4_4));	//JL和APC指令也可以写R0 R1寄存器
assign rd_r1_mux=	(ins[1:0]==opcode_sys)&((ins[5:2]==funct4_4));	//JL和APC指令也可以写R0 R1寄存器		

//rs1控制
assign ds1_r0	=	(ins[11:9]==3'b000);	
assign ds1_r1	=	(ins[11:9]==3'b001);	
assign ds1_r2	=	(ins[11:9]==3'b010);	
assign ds1_r3	=	(ins[11:9]==3'b011);	
assign ds1_r4	=	(ins[11:9]==3'b100);	
assign ds1_r5	=	(ins[11:9]==3'b101);	
assign ds1_r6	=	(ins[11:9]==3'b110);	
assign ds1_r7	=	(ins[11:9]==3'b111);
assign ds2_r0	=	(ins[14:12]==3'b000);	
assign ds2_r1	=	(ins[14:12]==3'b001);	
assign ds2_r2	=	(ins[14:12]==3'b010);	
assign ds2_r3	=	(ins[14:12]==3'b011);	
assign ds2_r4	=	(ins[14:12]==3'b100);	
assign ds2_r5	=	(ins[14:12]==3'b101);	
assign ds2_r6	=	(ins[14:12]==3'b110);	
assign ds2_r7	=	(ins[14:12]==3'b111);			
					
//cr写控制
assign statu_sel=	(ins[15:9]==statu_index);
assign ie_sel	=	(ins[15:9]==ie_index);
assign epc_sel	=	(ins[15:9]==epc_index);
assign cpc_sel	=	(ins[15:9]==cpc_index);
assign temp_sel	=	(ins[15:9]==temp_index);
assign tcev0_sel=	(ins[15:9]==tvec0_index);
assign tcev1_sel=	(ins[15:9]==tvec1_index);
assign tcev2_sel=	(ins[15:9]==tvec2_index);
assign tcev3_sel=	(ins[15:9]==tvec3_index);
assign cr_write = 	(ins[1:0]==opcode_sys)&(ins[5:2]==funct4_3);	//WCR指令需要写CR

//特殊功能控制
assign jmp		=	(ins[1:0]==opcode_sys)&((ins[5:2]==funct4_0)|(ins[5:2]==funct4_2));	//JL和JMP均需要写CPC
assign apc		=	(ins[1:0]==opcode_sys)&((ins[5:2]==funct4_0)|(ins[5:2]==funct4_1));	//JL和APC均需要获取PC
assign ret		=	(ins[1:0]==opcode_sys)&	(ins[5:2]==funct4_5);		
assign bra		=	(ins[1:0]==opcode_b);				
					
assign imm		=	{1'b0,ins[15:9]};
assign branch_offset	=	{{8{ins[15]}},ins[15:12],ins[8:6],1'b0};		//符号位拓展到16位之后是跳转偏移地址			
					
					
					
					
endmodule					
					
					
					

