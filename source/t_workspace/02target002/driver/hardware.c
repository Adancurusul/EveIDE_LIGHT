#include <mcs51/STC15.h>
#include "./hardware.h"
UartRxdData volatile __idata rxdData;
UartRxdData volatile __idata txdData;
u8 volatile time_count;
u8  RecIspStat;
void    ClearUartData(UartRxdData * puartData)
{
    puartData->len = 0;
    puartData->index = 0;
    puartData->busy = 0;
}
#define FOSC 22118400L
#define BAUD  115200L
#define MAIN_Fosc		22118400L	//定义主时钟
#define	RX1_Lenth		32			//串口接收缓冲长度
#define	BaudRate1		115200UL	//选择波特率

//#define	Timer1_Reload	(65536UL -(MAIN_Fosc / 4 / BaudRate1))		//Timer 1 重装值， 对应300KHZ
#define	Timer2_Reload	(65536UL -(MAIN_Fosc / 4 / BaudRate1))		//Timer 2 重装值， 对应300KHZ
void UartInit(void)		//115200bps@22.1184MHz
{
	S1_8bit();				//8位数据
	S1_USE_P30P31();		//UART1 使用P30 P31口	默认//	S1_USE_P36P37();//UART1 使用P36 P37口//	S1_USE_P16P17();//UART1 使用P16 P17口

	AUXR &= ~(1<<4);	//Timer stop		波特率使用Timer2产生
	AUXR |= 0x01;		//S1 BRT Use Timer2;
	AUXR |=  (1<<2);	//Timer2 set as 1T mode
	TH2 = (u8)(Timer2_Reload >> 8);
	TL2 = (u8)Timer2_Reload;
	AUXR |=  (1<<4);	//Timer run enable

	REN = 1;	//允许接收
	ES  = 1;	//允许中断
	ClearUartData(&rxdData);
	ClearUartData(&txdData);
	RecIspStat = 0;

}

void    GetUartData(u8 mybuf[],u8 len)
{
    u8 i;
    if(len >RXD_LENGTH) return;
    mybuf[0] = 0;
    for(i=0;i<len;i++){
        mybuf[i] = rxdData.buf[i];
    }
    //ClearUartData(&rxdData);
    rxdData.len = 0;
}
u8  GetUartRxdLen(void)
{
    return rxdData.len;
}

/*----------------------------
发送字符串
void SendData(u8 dat)
{
    while(TI);
    SBUF = dat;
    TI=0;
}
void SendString(char *s)
{
    while (*s){                  //检测字符串结束标志
        SendData(*s++);         //发送当前字符
    }
}
----------------------------*/
void    UartPrint(const u8 * pstr)
{
    while(txdData.busy);
    txdData.len = 0;
    while(*pstr){
        txdData.buf[txdData.len] = *pstr;
        txdData.len++;
        pstr++;
        if(txdData.len>=RXD_LENGTH){ // 发送缓冲区满，开始发送并等待
            txdData.index = 0;
            txdData.busy = true;
            TI = 1;
            while(txdData.busy);
            txdData.len = 0;
        }
    }
    txdData.index = 0;
    txdData.busy = true;
    TI = 1;
}

//==============定时器1==================

#define T0_1MS (65536-FOSC/1000)      //1T模式
void Timer0Init(void)		//20毫秒@22.1184MHz
{
    AUXR |= 0x80;       //定时器时钟1T模式
	//AUXR &= 0x7F;		//定时器时钟12T模式
	TMOD &= 0xF0;		//设置定时器模式
	TL0 = (u8)T0_1MS;		    //设置定时初值
	TH0 = (u8)(T0_1MS>>8);		    //设置定时初值
	//TH0 = 0x70;		    //设置定时初值 0x70 <->40ms  //0xEE <->5ms
	TF0 = 0;		    //清除TF0标志
	TR0 = 1;		    //定时器0开始计时
    ET0 = 1;            //使能定时器中断
}

void    delay_ms(u8 ms)// 注意ms的类型，最大值只有255
{
    time_count = ms;
    while(time_count);
}
void delay_100us(unsigned int ms)   //  软件延时，注意数据类型，100us
{
        unsigned int x, y;
        for (y = ms; y > 0; y--) {
                for (x = 11; x > 0; x--);
        }
}

