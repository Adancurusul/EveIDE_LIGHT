
#include "stc15f104e.h"

//#include <string.h>
//#include "public/inc/RS-232.h"
//#include "public/inc/timer.h"
//#include "public/inc/delay.h"  


__sbit __at 0xB3 LED3 ;
__sbit __at 0xB2 LED2 ;
__sbit __at 0xB1 LED1 ;
__sbit __at 0xB4 LED4 ;
__sbit __at 0xB5 LED5 ;
__sbit __at 0xB0 LED0 ;
//#define LED3 P33
//SBIT( LED0 , P3 ,  0);
//SBIT( LED1 , P3 ,  1);
//SBIT( LED2 , P3 ,  2);
//SBIT( LED3 , P3 ,  3);
//SBIT( LED4 , P3 ,  4);
//SBIT( LED5 , P3 ,  5);
#define SFR(name, addr) __sfr __at(addr) name
SFR( P1M0        ,   0x92);   //0000,0000 端口3模式寄存器0
SFR( P1M1        ,   0x91);   //0000,0000 端口3模式寄存器1


			void delay(unsigned int ms)
{
     unsigned int i;
	 do{
	      i = 100;
		  while(--i)	;   //14T per loop
     }while(--ms);
}
void main(void) 
{
	P1M1 = 0x0;
	P1M0 = 0x0;
    
    //EX1 = 1;
    //IT1 = 1;
    LED1 = 1;
    LED0 = 1;
    LED2 = 1;
    LED3 = 1;
    LED5 = 1;
    LED4 = 1;



	while(1) 
	{ 
        LED0 = 1;
        LED1 = 1;
        LED2 = 1;
        LED3 = 1;
        LED4 = 1;
        LED5 = 1;
        delay(500);	
        LED0 = 0;
        LED1 = 0;
        LED2 = 0;
        LED3 = 0;
        LED4 = 0;
        LED5 = 0;
        delay(500);	
	} //end of while
}



