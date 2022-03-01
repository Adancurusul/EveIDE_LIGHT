;--------------------------------------------------------
; File Created by SDCC : free open source ANSI-C Compiler
; Version 3.8.6 #10998 (MINGW64)
;--------------------------------------------------------
	.module main
	.optsdcc -mmcs51 --model-small
	
;--------------------------------------------------------
; Public variables in this module
;--------------------------------------------------------
	.globl _TM0_Isr
	.globl _UART1_Isr
	.globl _main
	.globl _delay_ms
	.globl _Timer0Init
	.globl _GetUartData
	.globl _UartPrint
	.globl _GetUartRxdLen
	.globl _UartInit
	.globl _CCF0
	.globl _CCF1
	.globl _CCF2
	.globl _CR
	.globl _CF
	.globl _RI
	.globl _TI
	.globl _RB8
	.globl _TB8
	.globl _REN
	.globl _SM2
	.globl _SM1
	.globl _SM0
	.globl _IT0
	.globl _IE0
	.globl _IT1
	.globl _IE1
	.globl _TR0
	.globl _TF0
	.globl _TR1
	.globl _TF1
	.globl _PX0
	.globl _PT0
	.globl _PX1
	.globl _PT1
	.globl _PS
	.globl _PADC
	.globl _PLVD
	.globl _PPCA
	.globl _EX0
	.globl _ET0
	.globl _EX1
	.globl _ET1
	.globl _ES
	.globl _EADC
	.globl _ELVD
	.globl _EA
	.globl _P7_7
	.globl _P7_6
	.globl _P7_5
	.globl _P7_4
	.globl _P7_3
	.globl _P7_2
	.globl _P7_1
	.globl _P7_0
	.globl _P6_7
	.globl _P6_6
	.globl _P6_5
	.globl _P6_4
	.globl _P6_3
	.globl _P6_2
	.globl _P6_1
	.globl _P6_0
	.globl _P5_7
	.globl _P5_6
	.globl _P5_5
	.globl _P5_4
	.globl _P5_3
	.globl _P5_2
	.globl _P5_1
	.globl _P5_0
	.globl _P4_7
	.globl _P4_6
	.globl _P4_5
	.globl _P4_4
	.globl _P4_3
	.globl _P4_2
	.globl _P4_1
	.globl _P4_0
	.globl _P3_7
	.globl _P3_6
	.globl _P3_5
	.globl _P3_4
	.globl _P3_3
	.globl _P3_2
	.globl _P3_1
	.globl _P3_0
	.globl _P2_7
	.globl _P2_6
	.globl _P2_5
	.globl _P2_4
	.globl _P2_3
	.globl _P2_2
	.globl _P2_1
	.globl _P2_0
	.globl _P1_7
	.globl _P1_6
	.globl _P1_5
	.globl _P1_4
	.globl _P1_3
	.globl _P1_2
	.globl _P1_1
	.globl _P1_0
	.globl _P0_7
	.globl _P0_6
	.globl _P0_5
	.globl _P0_4
	.globl _P0_3
	.globl _P0_2
	.globl _P0_1
	.globl _P0_0
	.globl _P
	.globl _OV
	.globl _RS0
	.globl _RS1
	.globl _F0
	.globl _AC
	.globl _CY
	.globl _PWMFDCR
	.globl _PWMIF
	.globl _PWMCR
	.globl _PWMCFG
	.globl _CMPCR2
	.globl _CMPCR1
	.globl _CCAP2H
	.globl _CCAP1H
	.globl _CCAP0H
	.globl _PCA_PWM2
	.globl _PCA_PWM1
	.globl _PCA_PWM0
	.globl _CCAP2L
	.globl _CCAP1L
	.globl _CCAP0L
	.globl _CCAPM2
	.globl _CCAPM1
	.globl _CCAPM0
	.globl _CH
	.globl _CL
	.globl _CMOD
	.globl _CCON
	.globl _IAP_CONTR
	.globl _IAP_TRIG
	.globl _IAP_CMD
	.globl _IAP_ADDRL
	.globl _IAP_ADDRH
	.globl _IAP_DATA
	.globl _SPDAT
	.globl _SPCTL
	.globl _SPSTAT
	.globl _ADC_RESL
	.globl _ADC_RES
	.globl _ADC_CONTR
	.globl _SADEN
	.globl _SADDR
	.globl _S4BUF
	.globl _S4CON
	.globl _S3BUF
	.globl _S3CON
	.globl _S2BUF
	.globl _S2CON
	.globl _SBUF
	.globl _SCON
	.globl _WDT_CONTR
	.globl _WKTCH
	.globl _WKTCL
	.globl _TL2
	.globl _TH2
	.globl _TL3
	.globl _TH3
	.globl _TL4
	.globl _TH4
	.globl _T2L
	.globl _T2H
	.globl _T3L
	.globl _T3H
	.globl _T4L
	.globl _T4H
	.globl _T3T4M
	.globl _T4T3M
	.globl _TH1
	.globl _TH0
	.globl _TL1
	.globl _TL0
	.globl _TMOD
	.globl _TCON
	.globl _INT_CLKO
	.globl _IP2
	.globl _IE2
	.globl _IP
	.globl _IE
	.globl _P_SW2
	.globl _P1ASF
	.globl _BUS_SPEED
	.globl _CLK_DIV
	.globl _P_SW1
	.globl _AUXR1
	.globl _AUXR
	.globl _PCON
	.globl _P7M1
	.globl _P7M0
	.globl _P6M1
	.globl _P6M0
	.globl _P5M1
	.globl _P5M0
	.globl _P4M1
	.globl _P4M0
	.globl _P3M1
	.globl _P3M0
	.globl _P2M1
	.globl _P2M0
	.globl _P1M1
	.globl _P1M0
	.globl _P0M1
	.globl _P0M0
	.globl _P7
	.globl _P6
	.globl _P5
	.globl _P4
	.globl _P3
	.globl _P2
	.globl _P1
	.globl _P0
	.globl _DPH
	.globl _DPL
	.globl _SP
	.globl _PSW
	.globl _B
	.globl _ACC
;--------------------------------------------------------
; special function registers
;--------------------------------------------------------
	.area RSEG    (ABS,DATA)
	.org 0x0000
_ACC	=	0x00e0
_B	=	0x00f0
_PSW	=	0x00d0
_SP	=	0x0081
_DPL	=	0x0082
_DPH	=	0x0083
_P0	=	0x0080
_P1	=	0x0090
_P2	=	0x00a0
_P3	=	0x00b0
_P4	=	0x00c0
_P5	=	0x00c8
_P6	=	0x00e8
_P7	=	0x00f8
_P0M0	=	0x0094
_P0M1	=	0x0093
_P1M0	=	0x0092
_P1M1	=	0x0091
_P2M0	=	0x0096
_P2M1	=	0x0095
_P3M0	=	0x00b2
_P3M1	=	0x00b1
_P4M0	=	0x00b4
_P4M1	=	0x00b3
_P5M0	=	0x00ca
_P5M1	=	0x00c9
_P6M0	=	0x00cc
_P6M1	=	0x00cb
_P7M0	=	0x00e2
_P7M1	=	0x00e1
_PCON	=	0x0087
_AUXR	=	0x008e
_AUXR1	=	0x00a2
_P_SW1	=	0x00a2
_CLK_DIV	=	0x0097
_BUS_SPEED	=	0x00a1
_P1ASF	=	0x009d
_P_SW2	=	0x00ba
_IE	=	0x00a8
_IP	=	0x00b8
_IE2	=	0x00af
_IP2	=	0x00b5
_INT_CLKO	=	0x008f
_TCON	=	0x0088
_TMOD	=	0x0089
_TL0	=	0x008a
_TL1	=	0x008b
_TH0	=	0x008c
_TH1	=	0x008d
_T4T3M	=	0x00d1
_T3T4M	=	0x00d1
_T4H	=	0x00d2
_T4L	=	0x00d3
_T3H	=	0x00d4
_T3L	=	0x00d5
_T2H	=	0x00d6
_T2L	=	0x00d7
_TH4	=	0x00d2
_TL4	=	0x00d3
_TH3	=	0x00d4
_TL3	=	0x00d5
_TH2	=	0x00d6
_TL2	=	0x00d7
_WKTCL	=	0x00aa
_WKTCH	=	0x00ab
_WDT_CONTR	=	0x00c1
_SCON	=	0x0098
_SBUF	=	0x0099
_S2CON	=	0x009a
_S2BUF	=	0x009b
_S3CON	=	0x00ac
_S3BUF	=	0x00ad
_S4CON	=	0x0084
_S4BUF	=	0x0085
_SADDR	=	0x00a9
_SADEN	=	0x00b9
_ADC_CONTR	=	0x00bc
_ADC_RES	=	0x00bd
_ADC_RESL	=	0x00be
_SPSTAT	=	0x00cd
_SPCTL	=	0x00ce
_SPDAT	=	0x00cf
_IAP_DATA	=	0x00c2
_IAP_ADDRH	=	0x00c3
_IAP_ADDRL	=	0x00c4
_IAP_CMD	=	0x00c5
_IAP_TRIG	=	0x00c6
_IAP_CONTR	=	0x00c7
_CCON	=	0x00d8
_CMOD	=	0x00d9
_CL	=	0x00e9
_CH	=	0x00f9
_CCAPM0	=	0x00da
_CCAPM1	=	0x00db
_CCAPM2	=	0x00dc
_CCAP0L	=	0x00ea
_CCAP1L	=	0x00eb
_CCAP2L	=	0x00ec
_PCA_PWM0	=	0x00f2
_PCA_PWM1	=	0x00f3
_PCA_PWM2	=	0x00f4
_CCAP0H	=	0x00fa
_CCAP1H	=	0x00fb
_CCAP2H	=	0x00fc
_CMPCR1	=	0x00e6
_CMPCR2	=	0x00e7
_PWMCFG	=	0x00f1
_PWMCR	=	0x00f5
_PWMIF	=	0x00f6
_PWMFDCR	=	0x00f7
;--------------------------------------------------------
; special function bits
;--------------------------------------------------------
	.area RSEG    (ABS,DATA)
	.org 0x0000
_CY	=	0x00d7
_AC	=	0x00d6
_F0	=	0x00d5
_RS1	=	0x00d4
_RS0	=	0x00d3
_OV	=	0x00d2
_P	=	0x00d0
_P0_0	=	0x0080
_P0_1	=	0x0081
_P0_2	=	0x0082
_P0_3	=	0x0083
_P0_4	=	0x0084
_P0_5	=	0x0085
_P0_6	=	0x0086
_P0_7	=	0x0087
_P1_0	=	0x0090
_P1_1	=	0x0091
_P1_2	=	0x0092
_P1_3	=	0x0093
_P1_4	=	0x0094
_P1_5	=	0x0095
_P1_6	=	0x0096
_P1_7	=	0x0097
_P2_0	=	0x00a0
_P2_1	=	0x00a1
_P2_2	=	0x00a2
_P2_3	=	0x00a3
_P2_4	=	0x00a4
_P2_5	=	0x00a5
_P2_6	=	0x00a6
_P2_7	=	0x00a7
_P3_0	=	0x00b0
_P3_1	=	0x00b1
_P3_2	=	0x00b2
_P3_3	=	0x00b3
_P3_4	=	0x00b4
_P3_5	=	0x00b5
_P3_6	=	0x00b6
_P3_7	=	0x00b7
_P4_0	=	0x00c0
_P4_1	=	0x00c1
_P4_2	=	0x00c2
_P4_3	=	0x00c3
_P4_4	=	0x00c4
_P4_5	=	0x00c5
_P4_6	=	0x00c6
_P4_7	=	0x00c7
_P5_0	=	0x00c8
_P5_1	=	0x00c9
_P5_2	=	0x00ca
_P5_3	=	0x00cb
_P5_4	=	0x00cc
_P5_5	=	0x00cd
_P5_6	=	0x00ce
_P5_7	=	0x00cf
_P6_0	=	0x00e8
_P6_1	=	0x00e9
_P6_2	=	0x00ea
_P6_3	=	0x00eb
_P6_4	=	0x00ec
_P6_5	=	0x00ed
_P6_6	=	0x00ee
_P6_7	=	0x00ef
_P7_0	=	0x00f8
_P7_1	=	0x00f9
_P7_2	=	0x00fa
_P7_3	=	0x00fb
_P7_4	=	0x00fc
_P7_5	=	0x00fd
_P7_6	=	0x00fe
_P7_7	=	0x00ff
_EA	=	0x00af
_ELVD	=	0x00ae
_EADC	=	0x00ad
_ES	=	0x00ac
_ET1	=	0x00ab
_EX1	=	0x00aa
_ET0	=	0x00a9
_EX0	=	0x00a8
_PPCA	=	0x00bf
_PLVD	=	0x00be
_PADC	=	0x00bd
_PS	=	0x00bc
_PT1	=	0x00bb
_PX1	=	0x00ba
_PT0	=	0x00b9
_PX0	=	0x00b8
_TF1	=	0x008f
_TR1	=	0x008e
_TF0	=	0x008d
_TR0	=	0x008c
_IE1	=	0x008b
_IT1	=	0x008a
_IE0	=	0x0089
_IT0	=	0x0088
_SM0	=	0x009f
_SM1	=	0x009e
_SM2	=	0x009d
_REN	=	0x009c
_TB8	=	0x009b
_RB8	=	0x009a
_TI	=	0x0099
_RI	=	0x0098
_CF	=	0x00df
_CR	=	0x00de
_CCF2	=	0x00da
_CCF1	=	0x00d9
_CCF0	=	0x00d8
;--------------------------------------------------------
; overlayable register banks
;--------------------------------------------------------
	.area REG_BANK_0	(REL,OVR,DATA)
	.ds 8
;--------------------------------------------------------
; internal ram data
;--------------------------------------------------------
	.area DSEG    (DATA)
;--------------------------------------------------------
; overlayable items in internal ram 
;--------------------------------------------------------
;--------------------------------------------------------
; Stack segment in internal ram 
;--------------------------------------------------------
	.area	SSEG
__start__stack:
	.ds	1

;--------------------------------------------------------
; indirectly addressable internal ram data
;--------------------------------------------------------
	.area ISEG    (DATA)
;--------------------------------------------------------
; absolute internal ram data
;--------------------------------------------------------
	.area IABS    (ABS,DATA)
	.area IABS    (ABS,DATA)
;--------------------------------------------------------
; bit data
;--------------------------------------------------------
	.area BSEG    (BIT)
;--------------------------------------------------------
; paged external ram data
;--------------------------------------------------------
	.area PSEG    (PAG,XDATA)
;--------------------------------------------------------
; external ram data
;--------------------------------------------------------
	.area XSEG    (XDATA)
;--------------------------------------------------------
; absolute external ram data
;--------------------------------------------------------
	.area XABS    (ABS,XDATA)
;--------------------------------------------------------
; external initialized ram data
;--------------------------------------------------------
	.area XISEG   (XDATA)
	.area HOME    (CODE)
	.area GSINIT0 (CODE)
	.area GSINIT1 (CODE)
	.area GSINIT2 (CODE)
	.area GSINIT3 (CODE)
	.area GSINIT4 (CODE)
	.area GSINIT5 (CODE)
	.area GSINIT  (CODE)
	.area GSFINAL (CODE)
	.area CSEG    (CODE)
;--------------------------------------------------------
; interrupt vector 
;--------------------------------------------------------
	.area HOME    (CODE)
__interrupt_vect:
	ljmp	__sdcc_gsinit_startup
	reti
	.ds	7
	ljmp	_TM0_Isr
	.ds	5
	reti
	.ds	7
	reti
	.ds	7
	ljmp	_UART1_Isr
;--------------------------------------------------------
; global & static initialisations
;--------------------------------------------------------
	.area HOME    (CODE)
	.area GSINIT  (CODE)
	.area GSFINAL (CODE)
	.area GSINIT  (CODE)
	.globl __sdcc_gsinit_startup
	.globl __sdcc_program_startup
	.globl __start__stack
	.globl __mcs51_genXINIT
	.globl __mcs51_genXRAMCLEAR
	.globl __mcs51_genRAMCLEAR
	.area GSFINAL (CODE)
	ljmp	__sdcc_program_startup
;--------------------------------------------------------
; Home
;--------------------------------------------------------
	.area HOME    (CODE)
	.area HOME    (CODE)
__sdcc_program_startup:
	ljmp	_main
;	return from main will return to caller
;--------------------------------------------------------
; code
;--------------------------------------------------------
	.area CSEG    (CODE)
;------------------------------------------------------------
;Allocation info for local variables in function 'main'
;------------------------------------------------------------
;tmp                       Allocated to registers r7 
;mybuf                     Allocated to stack - _bp +1
;------------------------------------------------------------
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:13: void main(void)
;	-----------------------------------------
;	 function main
;	-----------------------------------------
_main:
	ar7 = 0x07
	ar6 = 0x06
	ar5 = 0x05
	ar4 = 0x04
	ar3 = 0x03
	ar2 = 0x02
	ar1 = 0x01
	ar0 = 0x00
	push	_bp
	mov	a,sp
	mov	_bp,a
	add	a,#0x10
	mov	sp,a
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:18: UartInit();
	lcall	_UartInit
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:19: Timer0Init();
	lcall	_Timer0Init
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:21: EA = 1;		//允许全局中断
;	assignBit
	setb	_EA
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:23: UartPrint("0123456789012345abcdef");
	mov	dptr,#___str_0
	mov	b,#0x80
	lcall	_UartPrint
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:24: while (1)
00104$:
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:26: led1 = !led1;
	cpl	_P2_6
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:27: P4_1 = !P4_1;
	cpl	_P4_1
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:29: delay_ms(50);
	mov	dpl,#0x32
	lcall	_delay_ms
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:31: tmp = GetUartRxdLen();
	lcall	_GetUartRxdLen
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:33: if(tmp){
	mov	a,dpl
	mov	r7,a
	jz	00104$
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:35: GetUartData(mybuf,tmp);
	mov	r6,_bp
	inc	r6
	mov	ar3,r6
	mov	r4,#0x00
	mov	r5,#0x40
	push	ar7
	push	ar6
	push	ar7
	mov	dpl,r3
	mov	dph,r4
	mov	b,r5
	lcall	_GetUartData
	dec	sp
	pop	ar6
	pop	ar7
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:36: mybuf[tmp] = 0;
	mov	a,r7
	add	a,r6
	mov	r0,a
	mov	@r0,#0x00
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:38: UartPrint((const u8 *)mybuf);
	mov	r7,#0x00
	mov	r5,#0x40
	mov	dpl,r6
	mov	dph,r7
	mov	b,r5
	lcall	_UartPrint
	sjmp	00104$
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:41: }
	mov	sp,_bp
	pop	_bp
	ret
;------------------------------------------------------------
;Allocation info for local variables in function 'UART1_Isr'
;------------------------------------------------------------
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:44: void UART1_Isr() __interrupt UART1_VECTOR
;	-----------------------------------------
;	 function UART1_Isr
;	-----------------------------------------
_UART1_Isr:
	push	acc
	push	ar7
	push	ar6
	push	ar1
	push	ar0
	push	psw
	mov	psw,#0x00
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:46: if (TI) {
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:47: TI = 0;
;	assignBit
	jbc	_TI,00152$
	sjmp	00116$
00152$:
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:48: if (txdData.index < txdData.len){
	mov	r0,#(_txdData + 0x0010)
	mov	ar7,@r0
	mov	r0,#(_txdData + 0x0011)
	mov	ar6,@r0
	clr	c
	mov	a,r7
	subb	a,r6
	jnc	00102$
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:49: SBUF = txdData.buf[txdData.index];
	mov	r0,#(_txdData + 0x0010)
	mov	a,@r0
	add	a,#_txdData
	mov	r1,a
	mov	_SBUF,@r1
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:50: txdData.index++;
	mov	r0,#(_txdData + 0x0010)
	mov	a,@r0
	mov	r7,a
	inc	a
	mov	r0,#(_txdData + 0x0010)
	mov	@r0,a
	sjmp	00118$
00102$:
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:52: txdData.busy=false;
	mov	r0,#(_txdData + 0x0012)
	mov	@r0,#0x00
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:53: txdData.len = 0;
	mov	r0,#(_txdData + 0x0011)
	mov	@r0,#0x00
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:54: txdData.index = 0;
	mov	r0,#(_txdData + 0x0010)
	mov	@r0,#0x00
	sjmp	00118$
00116$:
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:56: }else if (RI){
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:57: RI = 0;
;	assignBit
	jbc	_RI,00154$
	sjmp	00118$
00154$:
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:58: if(rxdData.len < RXD_LENGTH){
	mov	r0,#(_rxdData + 0x0011)
	mov	ar7,@r0
	cjne	r7,#0x10,00155$
00155$:
	jnc	00111$
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:59: rxdData.buf[rxdData.len] = SBUF;
	mov	r0,#(_rxdData + 0x0011)
	mov	a,@r0
	add	a,#_rxdData
	mov	r0,a
	mov	@r0,_SBUF
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:60: rxdData.len++;
	mov	r0,#(_rxdData + 0x0011)
	mov	a,@r0
	inc	a
	mov	r0,#(_rxdData + 0x0011)
	mov	@r0,a
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:61: if(rxdData.len==3){
	mov	r0,#(_rxdData + 0x0011)
	mov	ar7,@r0
	cjne	r7,#0x03,00118$
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:62: if((rxdData.buf[0]==0x5a)&&
	mov	r0,#_rxdData
	mov	ar7,@r0
	cjne	r7,#0x5a,00118$
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:63: (rxdData.buf[1]==0x3a)&&
	mov	r0,#(_rxdData + 0x0001)
	mov	ar7,@r0
	cjne	r7,#0x3a,00118$
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:64: (rxdData.buf[2]==0x6c))
	mov	r0,#(_rxdData + 0x0002)
	mov	ar7,@r0
	cjne	r7,#0x6c,00118$
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:65: RS_ISP;
	orl	_IAP_CONTR,#0x60
	sjmp	00118$
00111$:
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:68: rxdData.len = 0;
	mov	r0,#(_rxdData + 0x0011)
	mov	@r0,#0x00
00118$:
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:71: }
	pop	psw
	pop	ar0
	pop	ar1
	pop	ar6
	pop	ar7
	pop	acc
	reti
;	eliminated unneeded push/pop dpl
;	eliminated unneeded push/pop dph
;	eliminated unneeded push/pop b
;------------------------------------------------------------
;Allocation info for local variables in function 'TM0_Isr'
;------------------------------------------------------------
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:73: void TM0_Isr() __interrupt 1     //
;	-----------------------------------------
;	 function TM0_Isr
;	-----------------------------------------
_TM0_Isr:
	push	acc
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:76: if(time_count)  time_count--;
	mov	a,_time_count
	jz	00103$
	mov	a,_time_count
	dec	a
	mov	_time_count,a
00103$:
;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:77: }
	pop	acc
	reti
;	eliminated unneeded mov psw,# (no regs used in bank)
;	eliminated unneeded push/pop psw
;	eliminated unneeded push/pop dpl
;	eliminated unneeded push/pop dph
;	eliminated unneeded push/pop b
	.area CSEG    (CODE)
	.area CONST   (CODE)
___str_0:
	.ascii "0123456789012345abcdef"
	.db 0x00
	.area XINIT   (CODE)
	.area CABS    (ABS,CODE)
