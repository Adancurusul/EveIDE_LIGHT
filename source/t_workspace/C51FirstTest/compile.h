/** SDCC - Small Device C Compiler
  * http://sdcc.sf.net
 */
#if defined(SDCC) || defined(__SDCC)
#define SBIT(name, addr, bit) __sbit __at(addr + bit) name
#define SFR(name, addr) __sfr __at(addr) name
#define SFRX(name, addr) __xdata volatile unsigned char __at(addr) name
#define SFR16(name, addr) __sfr16 __at(((addr + 1U) << 8) | addr) name
#define SFR16E(name, fulladdr) __sfr16 __at(fulladdr) name
#define SFR16LEX(name, addr) __xdata volatile unsigned short __at(addr) name
#define SFR32(name, addr) __sfr32 __at(((addr + 3UL) << 24) | ((addr + 2UL) << 16) | ((addr + 1UL) << 8) | addr) name
#define SFR32E(name, fulladdr) __sfr32 __at(fulladdr) name

#define INTERRUPT(name, vector) void name(void) __interrupt(vector)
#define INTERRUPT_USING(name, vector, regnum) void name(void) __interrupt(vector) __using(regnum)

// NOP () macro support
#define NOP() __asm NOP __endasm

/** Keil C51
  * http://www.keil.com
 */
#elif defined __CX51__
#define SBIT(name, addr, bit) sbit name = addr ^ bit
#define SFR(name, addr) sfr name = addr
#define SFRX(name, addr) volatile unsigned char xdata name _at_ addr
#define SFR16(name, addr) sfr16 name = addr
#define SFR16E(name, fulladdr) /* not supported */
#define SFR16LEX(name, addr)   /* not supported */
#define SFR32(name, fulladdr)  /* not supported */
#define SFR32E(name, fulladdr) /* not supported */

#define INTERRUPT(name, vector) void name(void) interrupt vector
#define INTERRUPT_USING(name, vector, regnum) void name(void) interrupt vector using regnum

// NOP () macro support
extern void _nop_(void);
#define NOP() _nop_()

#endif