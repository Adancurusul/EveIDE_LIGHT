main: 
 lui x1, 0x01000 
 addi x2, x0, 0x010	//data length = 16 
 addi x1, x1, 0x001	//x1 is the address 
 sb x1, 0x000(x1)	//store x1 
 addi x1, x1, 0x001	//x1 increase 
 bne x1, x2, main  
 nop: 
 addi x0, x0, 0x000 
 jal x3, nop