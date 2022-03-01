#ifndef __SERIAL_H_
#define __SERIAL_H_
#include <mcs51/STC15.h>

#define RXD_LENGTH  16
typedef struct{  // 目前Rxd，Txd统一用这个结构体    ；后面有需要再区分
    u8  buf[RXD_LENGTH];
    u8  index;
    u8  len;
    u8  busy;
    u8  reserverd;
} UartRxdData;
#define TXD_LENGTH  16
typedef struct{
    u8  buf[TXD_LENGTH];
    u8  index;
    u8  len;
    u8  busy;
    u8  reserverd;
} UartTxdData;
void UartInit(void)	;
u8  GetUartRxdLen(void);
void    UartPrint(const u8 * pstr);
void    ClearUartData(UartRxdData * puartData);
void SendData(u8 dat);
void    GetUartData(u8 mybuf[],u8 len);


void Timer0Init()	;
void    delay_ms(u8 ms);
void delay_100us(unsigned int ms);   //  软件延时，注意数据类型，100us


#endif
