#include "../inc/Delay.h"

void delay_ms(unsigned int ms)
{
     unsigned int i;
	 do{
	      i = MAIN_FOSC / 14000;
		  while(--i)	;   //14T per loop
     }while(--ms);
}