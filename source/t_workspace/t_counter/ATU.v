`include "../RTL/PRV564Config.v"
`include "../RTL/PRV564Define.v"
//////////////////////////////////////////////////////////////////////////////////////////////////
//  Date    : 2021                                                                              //
//  Author  : Jack.Pan                                                                          //
//  Desc    : Address Translate Unit for PRV564 processor, which include a TLB and MMU          //
//  Version : 2.0(Version 2) Huge-page now avilible!                                            //
//////////////////////////////////////////////////////////////////////////////////////////////////
module ATU
#(
    parameter FIB_ID = 8'h00
    parameter qqd = 213
)
(
//Global Signals
    input wire              ATUi_CLK,
    input wire              ATUi_ARST,
    input wire              ATUi_Flush,             //Request FLush pipline
    input wire              ATUi_ModifyPermit,      //允许模块进行内容修改
    input wire [7:0]        ATUi_ModifyPermitID,    //允许修改的指令ID，如果当前ID等于此ID，则开始修改
    input wire              ATUi_TLBrefersh,        //(From Master) Request refersh TLB
    output wire             ATUo_TLBrefersh,        //(To slave)refersh TLB
    input wire              ATUi_CSR_mxr,
    input wire              ATUi_CSR_sum,
    input wire [`XLEN-1:0]  ATUi_CSR_satp,
//Pipline input signals
    input  wire             PIP_ATUi_MSC_valid,     //操作有效
    input  wire  [7:0]      PIP_ATUi_Opcode,        //8bit opcode
    input  wire  [1:0]      PIP_ATUi_OpInfo,        //Operation Information, include Unsign/Sign and RV32/64
    input  wire  [3:0]      PIP_ATUi_OpSize,
    input  wire  [7:0]      PIP_ATUi_INFO_ITAG,
    input  wire  [1:0]      PIP_ATUi_INFO_priv,     //权限
    input  wire             PIP_ATUi_INFO_unpage,   //unpage mode enable
    input  wire  [`XLEN-1:0]PIP_ATUi_INFO_PC,       //Instruction Infomation: PC value
    input  wire  [`XLEN-1:0]PIP_ATUi_DATA_VA,       //虚拟地址输入
    input  wire  [`XLEN-1:0]PIP_ATUi_DATA_ds1,      //Data Source 1
    input  wire  [`XLEN-1:0]PIP_ATUi_DATA_ds2,
    input  wire             PIP_ATUi_FC_ready,
//流水线输出信号
    output  reg  [7:0]      PIP_ATUo_Opcode,        //Opcode for Load/Store
    output  reg  [1:0]      PIP_ATUo_OpInfo,
    output  reg  [3:0]      PIP_ATUo_OpSize,
    output  reg             PIP_ATUo_MSC_valid,     //全局有效
    output  reg             PIP_ATUo_MSC_LoadPageFlt,
    output  reg             PIP_ATUo_MSC_StorePageFlt,
    output  reg             PIP_ATUo_MSC_InstPageFlt,
    output  reg  [`XLEN-1:0]PIP_ATUo_DATA_PA,        //物理地址输出
    output  reg  [7:0]      PIP_ATUo_INFO_ITAG,
    output  reg  [1:0]      PIP_ATUo_INFO_priv,
    output  reg  [`XLEN-1:0]PIP_ATUo_INFO_PC,        //程序地址输出
    output  reg             PIP_ATUo_DATA_Cacheable, //可以被缓存
    output  reg             PIP_ATUo_DATA_WrThrough, //此地址需要被写穿透
    output  reg  [`XLEN-1:0]PIP_ATUo_DATA_ds1,
    output  reg  [`XLEN-1:0]PIP_ATUo_DATA_ds2,
    output  reg             PIP_ATUo_FC_ready,
//------------FIB bus interface--------------
    output  wire              ATUo_FIB_WREN,        //write to FIB enable
    output  wire              ATUo_FIB_REQ,         //request FIB trans
    input   wire              ATUi_FIB_ACK,         //request acknowledge
    input   wire              ATUi_FIB_FULL,        //FIB FIFO full
    output  wire [7:0]        ATUo_FIB_ID,
    output  wire [7:0]        ATUo_FIB_CMD,
    output  wire [3:0]        ATUo_FIB_BURST,
    output  wire [3:0]        ATUo_FIB_SIZE,
    output  wire [`XLEN-1:0]  ATUo_FIB_ADDR,      
    output  wire [`XLEN-1:0]  ATUo_FIB_DATA,
    input   wire [7:0]        ATUi_FIB_ID,
    input   wire [7:0]        ATUi_FIB_RPL,
    input   wire              ATUi_FIB_V,
    input   wire [`XLEN-1:0]  ATUi_FIB_DATA

);
//---------------------Global Valid For This Module-------------------------
    wire            valid;                                                      
assign valid = PIP_ATUi_MSC_valid & !ATUi_Flush;                                //When FLush is 1, set global valid = 0
//--------------------Flags--------------------------------------------------
    reg             r_LoadPageFlt, r_StorePageFlt, r_InstPageFlt;               //页面错误寄存器，如果页面错误的话
//Physical address generated
    reg [`XLEN-1:0] PA;                                                         //Physical Address Generate
//TLB control
    reg             TLBi_Dset, TLBi_access, TLBi_replace;
    wire [43:0]     TLBo_PPN;
    wire [9:0]      TLBo_PTE;
    wire            TLBo_miss;
    reg             TLBrefershPending;      //TLB刷新等待标志位
// MMU input signal
    reg  [7:0]      MMUi_CMD;
    reg             MMUi_V;
    wire [26:0]     MMUi_VPN;
    wire [43:0]     MMUo_PPN;
    wire [9:0]      MMUo_PTE;               //页表信息
    wire [1:0]      MMUo_PageSize;          //当前页大小
    wire [7:0]      MMUo_RPL;
	wire            MMUo_V;
//Page Check Signal
    wire            page_checkOK;           //页面检查成功

//当虚拟内存打开，且当前操作命令需要进行内存地址转换时TLB介入操作
always@(*)begin
    if(valid & ((PIP_ATUi_Opcode!=`LSU_NOP) | (PIP_ATUi_Opcode!=`LSU_TLBRef) | (PIP_ATUi_Opcode!=`LSU_CacheRef)) & (ATUi_CSR_satp[63:60]==`Sv39) & !PIP_ATUi_INFO_unpage)begin
        TLBi_access <= 1'b1;
    end
    else begin
        TLBi_access <= 1'b0;
    end
end
//--------------------TLB entry replace signal--------
always@(*)begin
    if(valid & (PIP_ATUi_Opcode!=`LSU_NOP) & (ATUi_CSR_satp[63:60]==`Sv39))begin
        if((MMUo_RPL==`TLB_PRL_RDY) & MMUo_V & TLBo_miss)begin
            case(MMUi_CMD)
                `TLB_CMD_rLUT : TLBi_replace <= 1'b1;
                `TLB_CMD_wLUT : TLBi_replace <= 1'b1;
                `TLB_CMD_xLUT : TLBi_replace <= 1'b1;
                default:        TLBi_replace <= 1'b0;
            endcase
		  end
        else begin
            TLBi_replace <= 1'b0;
        end
    end
    else begin
            TLBi_replace <= 1'b0;
    end
end
//------------------TLB D set signal------------------
always@(*)begin
    if(valid & (PIP_ATUi_Opcode!=`LSU_NOP) & (ATUi_CSR_satp[63:60]==`Sv39))begin
        if((MMUo_RPL==`TLB_PRL_RDY) & MMUo_V & (MMUi_CMD==`TLB_CMD_wLUT))begin
		    TLBi_Dset <= 1'b1;
		end
        else begin
            TLBi_Dset <= 1'b0;
        end
    end
    else begin
            TLBi_Dset <= 1'b0;
    end
end

// ------------------------------MMU控制--------------------------------
// 使用纯粹的组合逻辑来控制MMU行为，尽量避免在一个流水线级中使用大量状态机
always@(*)begin
    if(r_LoadPageFlt | r_StorePageFlt | r_InstPageFlt)begin
        MMUi_CMD <= `TLB_CMD_NOP;               //如果MMU转换后发生页面异常，则停止MMU
        MMUi_V   <= 1'b0;
    end
    else if(valid & (PIP_ATUi_Opcode!=`LSU_NOP) & (ATUi_CSR_satp[63:60]==`Sv39) & !PIP_ATUi_INFO_unpage)begin //当Sv39分页方案打开后，ATU介入控制
        if(PIP_ATUi_Opcode==`LSU_TLBRef)begin
            MMUi_CMD <= `TLB_CMD_NOP;           //如果要求TLB刷新，则MMU无命令
            MMUi_V   <= 1'b0;
        end
        else if(PIP_ATUi_Opcode==`LSU_CacheRef)begin
            MMUi_CMD <= `TLB_CMD_NOP;           //同上
            MMUi_V   <= 1'b0;
        end
        else if((PIP_ATUi_Opcode==`LSU_eXecute))begin
            if(TLBo_miss)begin
                MMUi_CMD <= `TLB_CMD_xLUT;
                MMUi_V   <= 1'b1;
            end
            else begin
                MMUi_CMD <= `TLB_CMD_NOP;
                MMUi_V   <= 1'b0;
            end
        end
        else if((PIP_ATUi_Opcode==`LSU_READ)|(PIP_ATUi_Opcode==`LSU_READ_Lock))begin
            if(TLBo_miss)begin
                MMUi_CMD <= `TLB_CMD_rLUT;
                MMUi_V   <= 1'b1;
            end
            else begin
                MMUi_CMD <= `TLB_CMD_NOP;
                MMUi_V   <= 1'b0;
            end
        end
        else if((PIP_ATUi_Opcode==`LSU_WRITE)|(PIP_ATUi_Opcode==`LSU_WRITE_Unloc)|(PIP_ATUi_Opcode==`LSU_AMOSWAP)|
                (PIP_ATUi_Opcode==`LSU_AMOADD)|(PIP_ATUi_Opcode==`LSU_AMOXOR)|(PIP_ATUi_Opcode==`LSU_AMOAND)|
                (PIP_ATUi_Opcode==`LSU_AMOOR)|(PIP_ATUi_Opcode==`LSU_AMOMAX)|(PIP_ATUi_Opcode==`LSU_AMOMIN))begin
            if(TLBo_miss)begin
                MMUi_CMD <= `TLB_CMD_wLUT;  //如果页面miss且要被写入，则转到写页面状态
                MMUi_V   <= 1'b1;
            end
            else if(!TLBo_PTE[`D] & page_checkOK)begin  //如果页面命中并检查通过，但是没有置D位，则置位
                MMUi_CMD <= `TLB_CMD_wLUT;
                MMUi_V   <= 1'b1;
            end
            else begin
                MMUi_CMD <= `TLB_CMD_NOP;
                MMUi_V   <= 1'b0;
            end
        end
        else begin
            MMUi_CMD <= `TLB_CMD_NOP;
            MMUi_V   <= 1'b0;
        end
    end
    else begin                      //如果虚拟内存没有打开，MMU摸鱼
        MMUi_CMD <= `TLB_CMD_NOP;
        MMUi_V   <= 1'b0;
    end
end

//错误信息暂存寄存器
//如果MMU转换过程中出现错误，则由该寄存器保存，直到这条指令被传递给下一级流水线
always@(posedge ATUi_CLK or posedge ATUi_ARST)begin
    if(ATUi_ARST)begin
        r_LoadPageFlt <= 1'b0;
        r_StorePageFlt<= 1'b0;
        r_InstPageFlt <= 1'b0;
    end
    else if(MMUi_V)begin
        r_LoadPageFlt <= (MMUo_RPL==`TLB_RPL_rPERR) & MMUo_V;
        r_StorePageFlt<= (MMUo_RPL==`TLB_RPL_wPERR) & MMUo_V;
        r_InstPageFlt <= (MMUo_RPL==`TLB_RPL_xPERR) & MMUo_V;
    end
    else if(PIP_ATUi_FC_ready)begin
        r_LoadPageFlt <= 1'b0;
        r_StorePageFlt<= 1'b0;
        r_InstPageFlt <= 1'b0;
    end
end
assign MMUi_VPN = PIP_ATUi_DATA_VA[38:12];          //提取虚拟页号VPN
//--------------------------------------Generate Physical Address---------------------------------
always@(*)begin
    if(r_LoadPageFlt | r_StorePageFlt | r_InstPageFlt | !page_checkOK)begin
        PA <= PIP_ATUi_DATA_VA;                     //If page fault happen, physical address = virtual address
    end
    else if((ATUi_CSR_satp[63:60]==`Sv39) & (!PIP_ATUi_INFO_unpage))begin
        PA <= {8'b0,TLBo_PPN,PIP_ATUi_DATA_VA[11:0]};//If Virtual Memory is on, physical address = xxxxx
    end
    else begin
        PA <= PIP_ATUi_DATA_VA;                     //else, the virtual memery is NOT on
    end
end
TLBcore     	TLB(
//global signals
    .TLBi_CLK               (ATUi_CLK),               //Clock input
    .TLBi_ARST              (ATUi_ARST),              //Async reset input(Active High)
//control signals
    .TLBi_access            (TLBi_access),            //access enable
    .TLBi_refersh           (ATUo_TLBrefersh | ATUi_TLBrefersh),        //refersh the TLB
    .TLBi_Dset              (TLBi_Dset),              //set D bit for entry
    .TLBi_replace           (TLBi_replace),           //replace enable
//
    .TLBi_PPN               (MMUo_PPN),               //New PPN input
    .TLBi_PTE               (MMUo_PTE),               //New PTE input
    .TLBi_PageSize          (MMUo_PageSize),          //
    .TLBi_VPN               (PIP_ATUi_DATA_VA[38:12]),//Virtual Page Number input
//
    .TLBo_PPN               (TLBo_PPN),               //Physical Page Number output
    .TLBo_PTE               (TLBo_PTE),               //Page Table output
    .TLBo_miss              (TLBo_miss)               //TLB miss happen
);
PageCheck           ATU_PageCheck(
//csr
    .CSR_priv               (PIP_ATUi_INFO_priv),      //CPU privlage input
    .CSR_mxr                (ATUi_CSR_mxr),            //CSR MXR bit input
    .CSR_sum                (ATUi_CSR_sum),            //CSR SUM bit input
//read or write
    .OP_read                ((PIP_ATUi_Opcode==`LSU_READ)|(PIP_ATUi_Opcode==`LSU_READ_Lock)),
    .OP_write               ((PIP_ATUi_Opcode==`LSU_WRITE)|(PIP_ATUi_Opcode==`LSU_WRITE_Unloc)|(PIP_ATUi_Opcode==`LSU_AMOSWAP)|(PIP_ATUi_Opcode==`LSU_AMOADD)|(PIP_ATUi_Opcode==`LSU_AMOXOR)|(PIP_ATUi_Opcode==`LSU_AMOAND)|(PIP_ATUi_Opcode==`LSU_AMOOR)|(PIP_ATUi_Opcode==`LSU_AMOMAX)|(PIP_ATUi_Opcode==`LSU_AMOMIN)),
    .OP_execute             (PIP_ATUi_Opcode==`LSU_eXecute),
    .PTE_U                  (TLBo_PTE[`U]),
    .PTE_W                  (TLBo_PTE[`W]),
    .PTE_R                  (TLBo_PTE[`R]),
    .PTE_X                  (TLBo_PTE[`X]),
    .PTE_D                  (TLBo_PTE[`D]),
    .check_ok               (page_checkOK)
);


//MMU
MMU     
#(
    .FIB_ID                 (FIB_ID)
)
MMU
(
//---------Global Signals-------------
    .MMUi_CLK               (ATUi_CLK),
    .MMUi_ARST              (ATUi_ARST),
    .MMUi_CSR_privlage      (PIP_ATUi_INFO_priv),  //privlage input
    .MMUi_CSR_sum           (ATUi_CSR_sum),
    .MMUi_CSR_mxr           (ATUi_CSR_mxr),
    .MMUi_CSR_satpppn       (ATUi_CSR_satp[43:0]),   //satp's VPN segment
    .MMUi_ModifyPermit      (ATUi_ModifyPermit & (ATUi_ModifyPermitID == PIP_ATUi_INFO_ITAG)),
    .MMUi_Flush             (ATUi_Flush),
//---------Command & Data signals------------
    .MMUi_CMD               (MMUi_CMD),           //command 
    .MMUi_V                 (MMUi_V),             //Valid
    .MMUi_VPN               (MMUi_VPN),           //Virtual Address Input
//---------PTE and PPN Reply-----------------
    .MMUo_PPN               (MMUo_PPN),           //Physical Page Number Output(After Translation)
    .MMUo_RPL               (MMUo_RPL),
    .MMUo_V                 (MMUo_V),
    .MMUo_PTE               (MMUo_PTE),           //Page Table Entry
    .MMUo_PageSize          (MMUo_PageSize),
//------------FIB bus interface--------------
    .MMUo_FIB_WREN          (ATUo_FIB_WREN),      //write to FIB enable
    .MMUo_FIB_REQ           (ATUo_FIB_REQ),       //request FIB trans
    .MMUi_FIB_ACK           (ATUi_FIB_ACK),       //request acknowledge
    .MMUi_FIB_FULL          (ATUi_FIB_FULL),      //FIB FIFO full
    .MMUo_FIB_ID            (ATUi_FIB_ID),
    .MMUo_FIB_CMD           (ATUo_FIB_CMD),
    .MMUo_FIB_BURST         (ATUo_FIB_BURST),
    .MMUo_FIB_SIZE          (ATUo_FIB_SIZE),
    .MMUo_FIB_ADDR          (ATUo_FIB_ADDR), 
    .MMUo_FIB_DATA          (ATUo_FIB_DATA),
    .MMUi_FIB_ID            (ATUo_FIB_ID),
    .MMUi_FIB_V             (ATUi_FIB_V),
    .MMUi_FIB_RPL           (ATUi_FIB_RPL),
    .MMUi_FIB_DATA          (ATUi_FIB_DATA)

);
//------------------------Refersh request-----------------------------------------
//refersh pending 
always@(*)begin
    if(valid & (PIP_ATUi_Opcode!=`LSU_NOP) & (ATUi_CSR_satp[63:60]==`Sv39) & !PIP_ATUi_INFO_unpage)begin 
        if(PIP_ATUi_Opcode==`LSU_TLBRef)begin
            TLBrefershPending <=  1'b1;
        end
        else begin
            TLBrefershPending <= 1'b0;
        end
	 end
    else begin
        TLBrefershPending <= 1'b0;
    end
end
assign ATUo_TLBrefersh = (ATUi_ModifyPermitID==PIP_ATUi_INFO_ITAG) & ATUi_ModifyPermit & TLBrefershPending; //当一个刷新在等待，且更改允许后进行TLB刷新

//------------------------pipiline output registers-----------------------------
always@(posedge ATUi_CLK or posedge ATUi_ARST)begin
    if(ATUi_ARST)begin
        PIP_ATUo_Opcode             <= 8'b0;           //Opcode for Load/Store
        PIP_ATUo_OpInfo             <= 2'b0;
        PIP_ATUo_OpSize             <= 4'h0;
        PIP_ATUo_MSC_valid          <= 1'b0;            //全局有效
        PIP_ATUo_MSC_LoadPageFlt    <= 1'b0;
        PIP_ATUo_MSC_StorePageFlt   <= 1'b0;
        PIP_ATUo_MSC_InstPageFlt    <= 1'b0;
        PIP_ATUo_DATA_PA            <= 64'h0;           //物理地址输出
        PIP_ATUo_INFO_ITAG          <= 6'h0;
        PIP_ATUo_INFO_priv          <= 2'h0;
        PIP_ATUo_INFO_PC            <= 64'h0;           //程序地址输出
        PIP_ATUo_DATA_Cacheable     <= 1'b0;            //可以被缓存
        PIP_ATUo_DATA_WrThrough     <= 1'b0;            //此地址需要被写穿透
        PIP_ATUo_DATA_ds1           <= 64'h0;
        PIP_ATUo_DATA_ds2           <= 64'h0;
    end
    //如果后级正在执行指令，且没有完成，则输出等待
    else if(PIP_ATUo_MSC_valid & !PIP_ATUi_FC_ready)begin      
        PIP_ATUo_Opcode             <= PIP_ATUo_Opcode;
        PIP_ATUo_OpInfo             <= PIP_ATUo_OpInfo;
        PIP_ATUo_OpSize             <= PIP_ATUo_OpSize;    
        PIP_ATUo_MSC_valid          <= PIP_ATUo_MSC_valid;     
        PIP_ATUo_MSC_LoadPageFlt    <= PIP_ATUo_MSC_LoadPageFlt;
        PIP_ATUo_MSC_StorePageFlt   <= PIP_ATUo_MSC_StorePageFlt;
        PIP_ATUo_MSC_InstPageFlt    <= PIP_ATUo_MSC_InstPageFlt;
        PIP_ATUo_DATA_PA            <= PIP_ATUo_DATA_PA;        
        PIP_ATUo_INFO_ITAG          <= PIP_ATUo_INFO_ITAG;
        PIP_ATUo_INFO_priv          <= PIP_ATUo_INFO_priv;
        PIP_ATUo_INFO_PC            <= PIP_ATUo_INFO_PC;      
        PIP_ATUo_DATA_Cacheable     <= PIP_ATUo_DATA_Cacheable; 
        PIP_ATUo_DATA_WrThrough     <= PIP_ATUo_DATA_WrThrough;
        PIP_ATUo_DATA_ds1           <= PIP_ATUo_DATA_ds1;
        PIP_ATUo_DATA_ds2           <= PIP_ATUo_DATA_ds2;
    end
    else if(MMUi_V | (TLBrefershPending & !((ATUi_ModifyPermitID==PIP_ATUi_INFO_ITAG) & ATUi_ModifyPermit)))begin //如果MMU正在执行指令，或者一个刷新正在等待，则输出插空
        PIP_ATUo_MSC_valid          <= 1'b0;
    end
    else begin
        PIP_ATUo_Opcode             <= PIP_ATUi_Opcode;
        PIP_ATUo_OpInfo             <= PIP_ATUi_OpInfo;
        PIP_ATUo_OpSize             <= PIP_ATUi_OpSize;      
        PIP_ATUo_MSC_valid          <= valid;     
        PIP_ATUo_MSC_LoadPageFlt    <= ((ATUi_CSR_satp[63:60]==`Sv39) & !PIP_ATUi_INFO_unpage) ? (r_LoadPageFlt | ((PIP_ATUi_Opcode==`LSU_READ_Lock)|(PIP_ATUi_Opcode==`LSU_READ)) & !page_checkOK) : 1'b0;
        PIP_ATUo_MSC_StorePageFlt   <= ((ATUi_CSR_satp[63:60]==`Sv39) & !PIP_ATUi_INFO_unpage) ? (r_StorePageFlt | ((PIP_ATUi_Opcode==`LSU_WRITE)|(PIP_ATUi_Opcode==`LSU_WRITE_Unloc)|(PIP_ATUi_Opcode==`LSU_AMOSWAP)|(PIP_ATUi_Opcode==`LSU_AMOADD)|(PIP_ATUi_Opcode==`LSU_AMOXOR)|(PIP_ATUi_Opcode==`LSU_AMOAND)|(PIP_ATUi_Opcode==`LSU_AMOOR)|(PIP_ATUi_Opcode==`LSU_AMOMAX)|(PIP_ATUi_Opcode==`LSU_AMOMIN)) & !page_checkOK) : 1'b0;
        PIP_ATUo_MSC_InstPageFlt    <= ((ATUi_CSR_satp[63:60]==`Sv39) & !PIP_ATUi_INFO_unpage) ? (r_InstPageFlt | (PIP_ATUi_Opcode==`LSU_READ_Lock) & !page_checkOK) : 1'b0;
        PIP_ATUo_DATA_PA            <= PA;        
        PIP_ATUo_INFO_ITAG          <= PIP_ATUi_INFO_ITAG;
        PIP_ATUo_INFO_priv          <= PIP_ATUi_INFO_priv;
        PIP_ATUo_INFO_PC            <= PIP_ATUi_INFO_PC;      
        PIP_ATUo_DATA_Cacheable     <= ((PA & `Cacheable_MASK) == `Cacheable_ADDR);
        PIP_ATUo_DATA_WrThrough     <= 1'b0;                        //Write Through Not used
        PIP_ATUo_DATA_ds1           <= PIP_ATUi_DATA_ds1;
        PIP_ATUo_DATA_ds2           <= PIP_ATUi_DATA_ds2;
    end
end
//-----------------------产生ATU向前级的握手信号-----------------------
//产生原则：
// 如果当前级没有指令，即输入valid=0，则ready=0
// 如果后级指令执行完成即ATUo_valid=1且后级的ready信号为1，没有工作处于等待状态（MMUi_V=1或者TLBrefershPending=1），则流水线继续
// 如果后面没有指令，即ATUo_valid=0，则Ready信号取决于当前级是否有操作等待
//---------------------------------------------------------------------
always@(*)begin
    if(PIP_ATUi_MSC_valid)begin //当前级有指令
        if(ATUi_Flush)begin
            PIP_ATUo_FC_ready <= 1'b1;
        end
        else begin
            case({PIP_ATUo_MSC_valid, PIP_ATUi_FC_ready})
                2'b00 : if(MMUi_V | TLBrefershPending & !((ATUi_ModifyPermitID==PIP_ATUi_INFO_ITAG) & ATUi_ModifyPermit))begin
                            PIP_ATUo_FC_ready <= 1'b0;  //后级无指令，但当前级有操作，则握手失败
                        end
                        else begin
                            PIP_ATUo_FC_ready <= 1'b1;  //后级无指令，当前级无操作，握手成功
                        end
                2'b01 : if(MMUi_V | TLBrefershPending & !((ATUi_ModifyPermitID==PIP_ATUi_INFO_ITAG) & ATUi_ModifyPermit))begin
                            PIP_ATUo_FC_ready <= 1'b0;  //后级无指令，但当前级有操作，则握手失败
                        end
                        else begin
                            PIP_ATUo_FC_ready <= 1'b1;  //后级无指令，当前级无操作，握手成功
                        end
                2'b10 : PIP_ATUo_FC_ready <= 1'b0;      //后级有指令在等待，握手失败
                2'b11 : if(MMUi_V | TLBrefershPending & !((ATUi_ModifyPermitID==PIP_ATUi_INFO_ITAG) & ATUi_ModifyPermit))begin
                            PIP_ATUo_FC_ready <= 1'b0;  //后级有指令且执行完成，但当前级有操作，则握手失败
                        end
                        else begin
                            PIP_ATUo_FC_ready <= 1'b1;  //后级有指令且执行完成，当前级无操作，握手成功
                        end
                default: PIP_ATUo_FC_ready <= 1'b0;
            endcase
        end
    end
    else begin
        PIP_ATUo_FC_ready <= 1'b0;  //当前级无指令，ready信号为0
    end
end
endmodule
