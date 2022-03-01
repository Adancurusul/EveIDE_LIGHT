/*
 */
#include <mcs51/STC15.h>
#include "driver/hardware.h"

/*************	本地变量声明	**************/
#define led1 P2_6
#define RX1_Lenth 16
extern UartRxdData volatile __idata rxdData;
extern UartRxdData volatile __idata txdData;
extern u8  volatile time_count;

void main(void)
{
    u8 tmp;//,i;
    u8 mybuf[16];

	UartInit();
	Timer0Init();

	EA = 1;		//允许全局中断

    UartPrint("0123456789012345abcdef");
	while (1)
	{
        led1 = !led1;
        P4_1 = !P4_1;
        //delay_100us(10);
        delay_ms(50);

		tmp = GetUartRxdLen();
		//SendData('R');
		if(tmp){
            //SendData(tmp+0x30);
            GetUartData(mybuf,tmp);
            mybuf[tmp] = 0;
            //for(i=0;i<tmp;i++)
            UartPrint((const u8 *)mybuf);
		}
	}
}


void UART1_Isr() __interrupt UART1_VECTOR
{
    if (TI) {
        TI = 0;
        if (txdData.index < txdData.len){
           SBUF = txdData.buf[txdData.index];
           txdData.index++;
        }else {
            txdData.busy=false;
            txdData.len = 0;
            txdData.index = 0;
        }
    }else if (RI){
		RI = 0;
		if(rxdData.len < RXD_LENGTH){
            rxdData.buf[rxdData.len] = SBUF;
            rxdData.len++;
            if(rxdData.len==3){
                if((rxdData.buf[0]==0x5a)&&
                   (rxdData.buf[1]==0x3a)&&
                   (rxdData.buf[2]==0x6c))
                    RS_ISP;
            }
		}else{//   避免溢出处理
		    rxdData.len = 0;
		}
    }
}

void TM0_Isr() __interrupt 1     //
{
    //led1 = !led1;
    if(time_count)  time_count--;
}
