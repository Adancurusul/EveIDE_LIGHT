                                      1 ;--------------------------------------------------------
                                      2 ; File Created by SDCC : free open source ANSI-C Compiler
                                      3 ; Version 3.8.6 #10998 (MINGW64)
                                      4 ;--------------------------------------------------------
                                      5 	.module main
                                      6 	.optsdcc -mmcs51 --model-small
                                      7 	
                                      8 ;--------------------------------------------------------
                                      9 ; Public variables in this module
                                     10 ;--------------------------------------------------------
                                     11 	.globl _main
                                     12 	.globl _delay
                                     13 	.globl _LED0
                                     14 	.globl _LED5
                                     15 	.globl _LED4
                                     16 	.globl _LED1
                                     17 	.globl _LED2
                                     18 	.globl _LED3
                                     19 	.globl _CCF0
                                     20 	.globl _CCF1
                                     21 	.globl _CCF2
                                     22 	.globl _CR
                                     23 	.globl _CF
                                     24 	.globl _RI
                                     25 	.globl _TI
                                     26 	.globl _RB8
                                     27 	.globl _TB8
                                     28 	.globl _REN
                                     29 	.globl _SM2
                                     30 	.globl _SM1
                                     31 	.globl _SM0
                                     32 	.globl _IT0
                                     33 	.globl _IE0
                                     34 	.globl _IT1
                                     35 	.globl _IE1
                                     36 	.globl _TR0
                                     37 	.globl _TF0
                                     38 	.globl _TR1
                                     39 	.globl _TF1
                                     40 	.globl _PX0
                                     41 	.globl _PT0
                                     42 	.globl _PX1
                                     43 	.globl _PT1
                                     44 	.globl _PS
                                     45 	.globl _PADC
                                     46 	.globl _PLVD
                                     47 	.globl _PPCA
                                     48 	.globl _EX0
                                     49 	.globl _ET0
                                     50 	.globl _EX1
                                     51 	.globl _ET1
                                     52 	.globl _ES
                                     53 	.globl _EADC
                                     54 	.globl _ELVD
                                     55 	.globl _EA
                                     56 	.globl _P77
                                     57 	.globl _P76
                                     58 	.globl _P75
                                     59 	.globl _P74
                                     60 	.globl _P73
                                     61 	.globl _P72
                                     62 	.globl _P71
                                     63 	.globl _P70
                                     64 	.globl _P67
                                     65 	.globl _P66
                                     66 	.globl _P65
                                     67 	.globl _P64
                                     68 	.globl _P63
                                     69 	.globl _P62
                                     70 	.globl _P61
                                     71 	.globl _P60
                                     72 	.globl _P57
                                     73 	.globl _P56
                                     74 	.globl _P55
                                     75 	.globl _P54
                                     76 	.globl _P53
                                     77 	.globl _P52
                                     78 	.globl _P51
                                     79 	.globl _P50
                                     80 	.globl _P47
                                     81 	.globl _P46
                                     82 	.globl _P45
                                     83 	.globl _P44
                                     84 	.globl _P43
                                     85 	.globl _P42
                                     86 	.globl _P41
                                     87 	.globl _P40
                                     88 	.globl _P37
                                     89 	.globl _P36
                                     90 	.globl _P35
                                     91 	.globl _P34
                                     92 	.globl _P33
                                     93 	.globl _P32
                                     94 	.globl _P31
                                     95 	.globl _P30
                                     96 	.globl _P27
                                     97 	.globl _P26
                                     98 	.globl _P25
                                     99 	.globl _P24
                                    100 	.globl _P23
                                    101 	.globl _P22
                                    102 	.globl _P21
                                    103 	.globl _P20
                                    104 	.globl _P17
                                    105 	.globl _P16
                                    106 	.globl _P15
                                    107 	.globl _P14
                                    108 	.globl _P13
                                    109 	.globl _P12
                                    110 	.globl _P11
                                    111 	.globl _P10
                                    112 	.globl _P07
                                    113 	.globl _P06
                                    114 	.globl _P05
                                    115 	.globl _P04
                                    116 	.globl _P03
                                    117 	.globl _P02
                                    118 	.globl _P01
                                    119 	.globl _P00
                                    120 	.globl _P
                                    121 	.globl _OV
                                    122 	.globl _RS0
                                    123 	.globl _RS1
                                    124 	.globl _F0
                                    125 	.globl _AC
                                    126 	.globl _CY
                                    127 	.globl _P1M1
                                    128 	.globl _P1M0
                                    129 	.globl _CCAP2H
                                    130 	.globl _CCAP1H
                                    131 	.globl _CCAP0H
                                    132 	.globl _PCA_PWM2
                                    133 	.globl _PCA_PWM1
                                    134 	.globl _PCA_PWM0
                                    135 	.globl _CCAP2L
                                    136 	.globl _CCAP1L
                                    137 	.globl _CCAP0L
                                    138 	.globl _CCAPM2
                                    139 	.globl _CCAPM1
                                    140 	.globl _CCAPM0
                                    141 	.globl _CH
                                    142 	.globl _CL
                                    143 	.globl _CMOD
                                    144 	.globl _CCON
                                    145 	.globl _IAP_CONTR
                                    146 	.globl _IAP_TRIG
                                    147 	.globl _IAP_CMD
                                    148 	.globl _IAP_ADDRL
                                    149 	.globl _IAP_ADDRH
                                    150 	.globl _IAP_DATA
                                    151 	.globl _SPDAT
                                    152 	.globl _SPCTL
                                    153 	.globl _SPSTAT
                                    154 	.globl _ADC_RESL
                                    155 	.globl _ADC_RES
                                    156 	.globl _ADC_CONTR
                                    157 	.globl _SADEN
                                    158 	.globl _SADDR
                                    159 	.globl _S4BUF
                                    160 	.globl _S4CON
                                    161 	.globl _S3BUF
                                    162 	.globl _S3CON
                                    163 	.globl _S2BUF
                                    164 	.globl _S2CON
                                    165 	.globl _SBUF
                                    166 	.globl _SCON
                                    167 	.globl _WDT_CONTR
                                    168 	.globl _WKTCH
                                    169 	.globl _WKTCL
                                    170 	.globl _T2L
                                    171 	.globl _T2H
                                    172 	.globl _T3L
                                    173 	.globl _T3H
                                    174 	.globl _T4L
                                    175 	.globl _T4H
                                    176 	.globl _T3T4M
                                    177 	.globl _T4T3M
                                    178 	.globl _TH1
                                    179 	.globl _TH0
                                    180 	.globl _TL1
                                    181 	.globl _TL0
                                    182 	.globl _TMOD
                                    183 	.globl _TCON
                                    184 	.globl _INT_CLKO
                                    185 	.globl _IP2
                                    186 	.globl _IE2
                                    187 	.globl _IP
                                    188 	.globl _IE
                                    189 	.globl _IRC_CLKO
                                    190 	.globl _P_SW2
                                    191 	.globl _P1ASF
                                    192 	.globl _BUS_SPEED
                                    193 	.globl _CLK_DIV
                                    194 	.globl _P_SW1
                                    195 	.globl _AUXR1
                                    196 	.globl _AUXR
                                    197 	.globl _PCON
                                    198 	.globl _P7M1
                                    199 	.globl _P7M0
                                    200 	.globl _P6M1
                                    201 	.globl _P6M0
                                    202 	.globl _P5M1
                                    203 	.globl _P5M0
                                    204 	.globl _P4M1
                                    205 	.globl _P4M0
                                    206 	.globl _P3M1
                                    207 	.globl _P3M0
                                    208 	.globl _P2M1
                                    209 	.globl _P2M0
                                    210 	.globl _P0M1
                                    211 	.globl _P0M0
                                    212 	.globl _P7
                                    213 	.globl _P6
                                    214 	.globl _P5
                                    215 	.globl _P4
                                    216 	.globl _P3
                                    217 	.globl _P2
                                    218 	.globl _P1
                                    219 	.globl _P0
                                    220 	.globl _DPH
                                    221 	.globl _DPL
                                    222 	.globl _SP
                                    223 	.globl _PSW
                                    224 	.globl _B
                                    225 	.globl _ACC
                                    226 ;--------------------------------------------------------
                                    227 ; special function registers
                                    228 ;--------------------------------------------------------
                                    229 	.area RSEG    (ABS,DATA)
      000000                        230 	.org 0x0000
                           0000E0   231 _ACC	=	0x00e0
                           0000F0   232 _B	=	0x00f0
                           0000D0   233 _PSW	=	0x00d0
                           000081   234 _SP	=	0x0081
                           000082   235 _DPL	=	0x0082
                           000083   236 _DPH	=	0x0083
                           000080   237 _P0	=	0x0080
                           000090   238 _P1	=	0x0090
                           0000A0   239 _P2	=	0x00a0
                           0000B0   240 _P3	=	0x00b0
                           0000C0   241 _P4	=	0x00c0
                           0000C8   242 _P5	=	0x00c8
                           0000E8   243 _P6	=	0x00e8
                           0000F8   244 _P7	=	0x00f8
                           000094   245 _P0M0	=	0x0094
                           000093   246 _P0M1	=	0x0093
                           000096   247 _P2M0	=	0x0096
                           000095   248 _P2M1	=	0x0095
                           0000B2   249 _P3M0	=	0x00b2
                           0000B1   250 _P3M1	=	0x00b1
                           0000B4   251 _P4M0	=	0x00b4
                           0000B3   252 _P4M1	=	0x00b3
                           0000CA   253 _P5M0	=	0x00ca
                           0000C9   254 _P5M1	=	0x00c9
                           0000CC   255 _P6M0	=	0x00cc
                           0000CB   256 _P6M1	=	0x00cb
                           0000E2   257 _P7M0	=	0x00e2
                           0000E1   258 _P7M1	=	0x00e1
                           000087   259 _PCON	=	0x0087
                           00008E   260 _AUXR	=	0x008e
                           0000A2   261 _AUXR1	=	0x00a2
                           0000A2   262 _P_SW1	=	0x00a2
                           000097   263 _CLK_DIV	=	0x0097
                           0000A1   264 _BUS_SPEED	=	0x00a1
                           00009D   265 _P1ASF	=	0x009d
                           0000BA   266 _P_SW2	=	0x00ba
                           0000BB   267 _IRC_CLKO	=	0x00bb
                           0000A8   268 _IE	=	0x00a8
                           0000B8   269 _IP	=	0x00b8
                           0000AF   270 _IE2	=	0x00af
                           0000B5   271 _IP2	=	0x00b5
                           00008F   272 _INT_CLKO	=	0x008f
                           000088   273 _TCON	=	0x0088
                           000089   274 _TMOD	=	0x0089
                           00008A   275 _TL0	=	0x008a
                           00008B   276 _TL1	=	0x008b
                           00008C   277 _TH0	=	0x008c
                           00008D   278 _TH1	=	0x008d
                           0000D1   279 _T4T3M	=	0x00d1
                           0000D1   280 _T3T4M	=	0x00d1
                           0000D2   281 _T4H	=	0x00d2
                           0000D3   282 _T4L	=	0x00d3
                           0000D4   283 _T3H	=	0x00d4
                           0000D5   284 _T3L	=	0x00d5
                           0000D6   285 _T2H	=	0x00d6
                           0000D7   286 _T2L	=	0x00d7
                           0000AA   287 _WKTCL	=	0x00aa
                           0000AB   288 _WKTCH	=	0x00ab
                           0000C1   289 _WDT_CONTR	=	0x00c1
                           000098   290 _SCON	=	0x0098
                           000099   291 _SBUF	=	0x0099
                           00009A   292 _S2CON	=	0x009a
                           00009B   293 _S2BUF	=	0x009b
                           0000AC   294 _S3CON	=	0x00ac
                           0000AD   295 _S3BUF	=	0x00ad
                           000084   296 _S4CON	=	0x0084
                           000085   297 _S4BUF	=	0x0085
                           0000A9   298 _SADDR	=	0x00a9
                           0000B9   299 _SADEN	=	0x00b9
                           0000BC   300 _ADC_CONTR	=	0x00bc
                           0000BD   301 _ADC_RES	=	0x00bd
                           0000BE   302 _ADC_RESL	=	0x00be
                           0000CD   303 _SPSTAT	=	0x00cd
                           0000CE   304 _SPCTL	=	0x00ce
                           0000CF   305 _SPDAT	=	0x00cf
                           0000C2   306 _IAP_DATA	=	0x00c2
                           0000C3   307 _IAP_ADDRH	=	0x00c3
                           0000C4   308 _IAP_ADDRL	=	0x00c4
                           0000C5   309 _IAP_CMD	=	0x00c5
                           0000C6   310 _IAP_TRIG	=	0x00c6
                           0000C7   311 _IAP_CONTR	=	0x00c7
                           0000D8   312 _CCON	=	0x00d8
                           0000D9   313 _CMOD	=	0x00d9
                           0000E9   314 _CL	=	0x00e9
                           0000F9   315 _CH	=	0x00f9
                           0000DA   316 _CCAPM0	=	0x00da
                           0000DB   317 _CCAPM1	=	0x00db
                           0000DC   318 _CCAPM2	=	0x00dc
                           0000EA   319 _CCAP0L	=	0x00ea
                           0000EB   320 _CCAP1L	=	0x00eb
                           0000EC   321 _CCAP2L	=	0x00ec
                           0000F2   322 _PCA_PWM0	=	0x00f2
                           0000F3   323 _PCA_PWM1	=	0x00f3
                           0000F4   324 _PCA_PWM2	=	0x00f4
                           0000FA   325 _CCAP0H	=	0x00fa
                           0000FB   326 _CCAP1H	=	0x00fb
                           0000FC   327 _CCAP2H	=	0x00fc
                           000092   328 _P1M0	=	0x0092
                           000091   329 _P1M1	=	0x0091
                                    330 ;--------------------------------------------------------
                                    331 ; special function bits
                                    332 ;--------------------------------------------------------
                                    333 	.area RSEG    (ABS,DATA)
      000000                        334 	.org 0x0000
                           0000D7   335 _CY	=	0x00d7
                           0000D6   336 _AC	=	0x00d6
                           0000D5   337 _F0	=	0x00d5
                           0000D4   338 _RS1	=	0x00d4
                           0000D3   339 _RS0	=	0x00d3
                           0000D2   340 _OV	=	0x00d2
                           0000D0   341 _P	=	0x00d0
                           000080   342 _P00	=	0x0080
                           000081   343 _P01	=	0x0081
                           000082   344 _P02	=	0x0082
                           000083   345 _P03	=	0x0083
                           000084   346 _P04	=	0x0084
                           000085   347 _P05	=	0x0085
                           000086   348 _P06	=	0x0086
                           000087   349 _P07	=	0x0087
                           000090   350 _P10	=	0x0090
                           000091   351 _P11	=	0x0091
                           000092   352 _P12	=	0x0092
                           000093   353 _P13	=	0x0093
                           000094   354 _P14	=	0x0094
                           000095   355 _P15	=	0x0095
                           000096   356 _P16	=	0x0096
                           000097   357 _P17	=	0x0097
                           0000A0   358 _P20	=	0x00a0
                           0000A1   359 _P21	=	0x00a1
                           0000A2   360 _P22	=	0x00a2
                           0000A3   361 _P23	=	0x00a3
                           0000A4   362 _P24	=	0x00a4
                           0000A5   363 _P25	=	0x00a5
                           0000A6   364 _P26	=	0x00a6
                           0000A7   365 _P27	=	0x00a7
                           0000B0   366 _P30	=	0x00b0
                           0000B1   367 _P31	=	0x00b1
                           0000B2   368 _P32	=	0x00b2
                           0000B3   369 _P33	=	0x00b3
                           0000B4   370 _P34	=	0x00b4
                           0000B5   371 _P35	=	0x00b5
                           0000B6   372 _P36	=	0x00b6
                           0000B7   373 _P37	=	0x00b7
                           0000C0   374 _P40	=	0x00c0
                           0000C1   375 _P41	=	0x00c1
                           0000C2   376 _P42	=	0x00c2
                           0000C3   377 _P43	=	0x00c3
                           0000C4   378 _P44	=	0x00c4
                           0000C5   379 _P45	=	0x00c5
                           0000C6   380 _P46	=	0x00c6
                           0000C7   381 _P47	=	0x00c7
                           0000C8   382 _P50	=	0x00c8
                           0000C9   383 _P51	=	0x00c9
                           0000CA   384 _P52	=	0x00ca
                           0000CB   385 _P53	=	0x00cb
                           0000CC   386 _P54	=	0x00cc
                           0000CD   387 _P55	=	0x00cd
                           0000CE   388 _P56	=	0x00ce
                           0000CF   389 _P57	=	0x00cf
                           0000E8   390 _P60	=	0x00e8
                           0000E9   391 _P61	=	0x00e9
                           0000EA   392 _P62	=	0x00ea
                           0000EB   393 _P63	=	0x00eb
                           0000EC   394 _P64	=	0x00ec
                           0000ED   395 _P65	=	0x00ed
                           0000EE   396 _P66	=	0x00ee
                           0000EF   397 _P67	=	0x00ef
                           0000F8   398 _P70	=	0x00f8
                           0000F9   399 _P71	=	0x00f9
                           0000FA   400 _P72	=	0x00fa
                           0000FB   401 _P73	=	0x00fb
                           0000FC   402 _P74	=	0x00fc
                           0000FD   403 _P75	=	0x00fd
                           0000FE   404 _P76	=	0x00fe
                           0000FF   405 _P77	=	0x00ff
                           0000AF   406 _EA	=	0x00af
                           0000AE   407 _ELVD	=	0x00ae
                           0000AD   408 _EADC	=	0x00ad
                           0000AC   409 _ES	=	0x00ac
                           0000AB   410 _ET1	=	0x00ab
                           0000AA   411 _EX1	=	0x00aa
                           0000A9   412 _ET0	=	0x00a9
                           0000A8   413 _EX0	=	0x00a8
                           0000BF   414 _PPCA	=	0x00bf
                           0000BE   415 _PLVD	=	0x00be
                           0000BD   416 _PADC	=	0x00bd
                           0000BC   417 _PS	=	0x00bc
                           0000BB   418 _PT1	=	0x00bb
                           0000BA   419 _PX1	=	0x00ba
                           0000B9   420 _PT0	=	0x00b9
                           0000B8   421 _PX0	=	0x00b8
                           00008F   422 _TF1	=	0x008f
                           00008E   423 _TR1	=	0x008e
                           00008D   424 _TF0	=	0x008d
                           00008C   425 _TR0	=	0x008c
                           00008B   426 _IE1	=	0x008b
                           00008A   427 _IT1	=	0x008a
                           000089   428 _IE0	=	0x0089
                           000088   429 _IT0	=	0x0088
                           00009F   430 _SM0	=	0x009f
                           00009E   431 _SM1	=	0x009e
                           00009D   432 _SM2	=	0x009d
                           00009C   433 _REN	=	0x009c
                           00009B   434 _TB8	=	0x009b
                           00009A   435 _RB8	=	0x009a
                           000099   436 _TI	=	0x0099
                           000098   437 _RI	=	0x0098
                           0000DF   438 _CF	=	0x00df
                           0000DE   439 _CR	=	0x00de
                           0000DA   440 _CCF2	=	0x00da
                           0000D9   441 _CCF1	=	0x00d9
                           0000D8   442 _CCF0	=	0x00d8
                           0000B3   443 _LED3	=	0x00b3
                           0000B2   444 _LED2	=	0x00b2
                           0000B1   445 _LED1	=	0x00b1
                           0000B4   446 _LED4	=	0x00b4
                           0000B5   447 _LED5	=	0x00b5
                           0000B0   448 _LED0	=	0x00b0
                                    449 ;--------------------------------------------------------
                                    450 ; overlayable register banks
                                    451 ;--------------------------------------------------------
                                    452 	.area REG_BANK_0	(REL,OVR,DATA)
      000000                        453 	.ds 8
                                    454 ;--------------------------------------------------------
                                    455 ; internal ram data
                                    456 ;--------------------------------------------------------
                                    457 	.area DSEG    (DATA)
                                    458 ;--------------------------------------------------------
                                    459 ; overlayable items in internal ram 
                                    460 ;--------------------------------------------------------
                                    461 ;--------------------------------------------------------
                                    462 ; Stack segment in internal ram 
                                    463 ;--------------------------------------------------------
                                    464 	.area	SSEG
      000008                        465 __start__stack:
      000008                        466 	.ds	1
                                    467 
                                    468 ;--------------------------------------------------------
                                    469 ; indirectly addressable internal ram data
                                    470 ;--------------------------------------------------------
                                    471 	.area ISEG    (DATA)
                                    472 ;--------------------------------------------------------
                                    473 ; absolute internal ram data
                                    474 ;--------------------------------------------------------
                                    475 	.area IABS    (ABS,DATA)
                                    476 	.area IABS    (ABS,DATA)
                                    477 ;--------------------------------------------------------
                                    478 ; bit data
                                    479 ;--------------------------------------------------------
                                    480 	.area BSEG    (BIT)
                                    481 ;--------------------------------------------------------
                                    482 ; paged external ram data
                                    483 ;--------------------------------------------------------
                                    484 	.area PSEG    (PAG,XDATA)
                                    485 ;--------------------------------------------------------
                                    486 ; external ram data
                                    487 ;--------------------------------------------------------
                                    488 	.area XSEG    (XDATA)
                                    489 ;--------------------------------------------------------
                                    490 ; absolute external ram data
                                    491 ;--------------------------------------------------------
                                    492 	.area XABS    (ABS,XDATA)
                                    493 ;--------------------------------------------------------
                                    494 ; external initialized ram data
                                    495 ;--------------------------------------------------------
                                    496 	.area XISEG   (XDATA)
                                    497 	.area HOME    (CODE)
                                    498 	.area GSINIT0 (CODE)
                                    499 	.area GSINIT1 (CODE)
                                    500 	.area GSINIT2 (CODE)
                                    501 	.area GSINIT3 (CODE)
                                    502 	.area GSINIT4 (CODE)
                                    503 	.area GSINIT5 (CODE)
                                    504 	.area GSINIT  (CODE)
                                    505 	.area GSFINAL (CODE)
                                    506 	.area CSEG    (CODE)
                                    507 ;--------------------------------------------------------
                                    508 ; interrupt vector 
                                    509 ;--------------------------------------------------------
                                    510 	.area HOME    (CODE)
      000000                        511 __interrupt_vect:
      000000 02 00 06         [24]  512 	ljmp	__sdcc_gsinit_startup
                                    513 ;--------------------------------------------------------
                                    514 ; global & static initialisations
                                    515 ;--------------------------------------------------------
                                    516 	.area HOME    (CODE)
                                    517 	.area GSINIT  (CODE)
                                    518 	.area GSFINAL (CODE)
                                    519 	.area GSINIT  (CODE)
                                    520 	.globl __sdcc_gsinit_startup
                                    521 	.globl __sdcc_program_startup
                                    522 	.globl __start__stack
                                    523 	.globl __mcs51_genXINIT
                                    524 	.globl __mcs51_genXRAMCLEAR
                                    525 	.globl __mcs51_genRAMCLEAR
                                    526 	.area GSFINAL (CODE)
      00005F 02 00 03         [24]  527 	ljmp	__sdcc_program_startup
                                    528 ;--------------------------------------------------------
                                    529 ; Home
                                    530 ;--------------------------------------------------------
                                    531 	.area HOME    (CODE)
                                    532 	.area HOME    (CODE)
      000003                        533 __sdcc_program_startup:
      000003 02 00 8B         [24]  534 	ljmp	_main
                                    535 ;	return from main will return to caller
                                    536 ;--------------------------------------------------------
                                    537 ; code
                                    538 ;--------------------------------------------------------
                                    539 	.area CSEG    (CODE)
                                    540 ;------------------------------------------------------------
                                    541 ;Allocation info for local variables in function 'delay'
                                    542 ;------------------------------------------------------------
                                    543 ;ms                        Allocated to registers r6 r7 
                                    544 ;i                         Allocated to registers r4 r5 
                                    545 ;------------------------------------------------------------
                                    546 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\C51FirstTest\main.c:28: void delay(unsigned int ms)
                                    547 ;	-----------------------------------------
                                    548 ;	 function delay
                                    549 ;	-----------------------------------------
      000062                        550 _delay:
                           000007   551 	ar7 = 0x07
                           000006   552 	ar6 = 0x06
                           000005   553 	ar5 = 0x05
                           000004   554 	ar4 = 0x04
                           000003   555 	ar3 = 0x03
                           000002   556 	ar2 = 0x02
                           000001   557 	ar1 = 0x01
                           000000   558 	ar0 = 0x00
      000062 AE 82            [24]  559 	mov	r6,dpl
      000064 AF 83            [24]  560 	mov	r7,dph
                                    561 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\C51FirstTest\main.c:31: do{
      000066                        562 00104$:
                                    563 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\C51FirstTest\main.c:32: i = 100;
      000066 7C 64            [12]  564 	mov	r4,#0x64
      000068 7D 00            [12]  565 	mov	r5,#0x00
                                    566 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\C51FirstTest\main.c:33: while(--i)	;   //14T per loop
      00006A                        567 00101$:
      00006A EC               [12]  568 	mov	a,r4
      00006B 24 FF            [12]  569 	add	a,#0xff
      00006D FA               [12]  570 	mov	r2,a
      00006E ED               [12]  571 	mov	a,r5
      00006F 34 FF            [12]  572 	addc	a,#0xff
      000071 FB               [12]  573 	mov	r3,a
      000072 8A 04            [24]  574 	mov	ar4,r2
      000074 8B 05            [24]  575 	mov	ar5,r3
      000076 EA               [12]  576 	mov	a,r2
      000077 4B               [12]  577 	orl	a,r3
      000078 70 F0            [24]  578 	jnz	00101$
                                    579 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\C51FirstTest\main.c:34: }while(--ms);
      00007A EE               [12]  580 	mov	a,r6
      00007B 24 FF            [12]  581 	add	a,#0xff
      00007D FC               [12]  582 	mov	r4,a
      00007E EF               [12]  583 	mov	a,r7
      00007F 34 FF            [12]  584 	addc	a,#0xff
      000081 FD               [12]  585 	mov	r5,a
      000082 8C 06            [24]  586 	mov	ar6,r4
      000084 8D 07            [24]  587 	mov	ar7,r5
      000086 EC               [12]  588 	mov	a,r4
      000087 4D               [12]  589 	orl	a,r5
      000088 70 DC            [24]  590 	jnz	00104$
                                    591 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\C51FirstTest\main.c:35: }
      00008A 22               [24]  592 	ret
                                    593 ;------------------------------------------------------------
                                    594 ;Allocation info for local variables in function 'main'
                                    595 ;------------------------------------------------------------
                                    596 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\C51FirstTest\main.c:36: void main(void) 
                                    597 ;	-----------------------------------------
                                    598 ;	 function main
                                    599 ;	-----------------------------------------
      00008B                        600 _main:
                                    601 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\C51FirstTest\main.c:38: P1M1 = 0x0;
      00008B 75 91 00         [24]  602 	mov	_P1M1,#0x00
                                    603 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\C51FirstTest\main.c:39: P1M0 = 0x0;
      00008E 75 92 00         [24]  604 	mov	_P1M0,#0x00
                                    605 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\C51FirstTest\main.c:43: LED1 = 1;
                                    606 ;	assignBit
      000091 D2 B1            [12]  607 	setb	_LED1
                                    608 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\C51FirstTest\main.c:44: LED0 = 1;
                                    609 ;	assignBit
      000093 D2 B0            [12]  610 	setb	_LED0
                                    611 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\C51FirstTest\main.c:45: LED2 = 1;
                                    612 ;	assignBit
      000095 D2 B2            [12]  613 	setb	_LED2
                                    614 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\C51FirstTest\main.c:46: LED3 = 1;
                                    615 ;	assignBit
      000097 D2 B3            [12]  616 	setb	_LED3
                                    617 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\C51FirstTest\main.c:47: LED5 = 1;
                                    618 ;	assignBit
      000099 D2 B5            [12]  619 	setb	_LED5
                                    620 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\C51FirstTest\main.c:48: LED4 = 1;
                                    621 ;	assignBit
      00009B D2 B4            [12]  622 	setb	_LED4
                                    623 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\C51FirstTest\main.c:52: while(1) 
      00009D                        624 00102$:
                                    625 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\C51FirstTest\main.c:54: LED0 = 1;
                                    626 ;	assignBit
      00009D D2 B0            [12]  627 	setb	_LED0
                                    628 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\C51FirstTest\main.c:55: LED1 = 1;
                                    629 ;	assignBit
      00009F D2 B1            [12]  630 	setb	_LED1
                                    631 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\C51FirstTest\main.c:56: LED2 = 1;
                                    632 ;	assignBit
      0000A1 D2 B2            [12]  633 	setb	_LED2
                                    634 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\C51FirstTest\main.c:57: LED3 = 1;
                                    635 ;	assignBit
      0000A3 D2 B3            [12]  636 	setb	_LED3
                                    637 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\C51FirstTest\main.c:58: LED4 = 1;
                                    638 ;	assignBit
      0000A5 D2 B4            [12]  639 	setb	_LED4
                                    640 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\C51FirstTest\main.c:59: LED5 = 1;
                                    641 ;	assignBit
      0000A7 D2 B5            [12]  642 	setb	_LED5
                                    643 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\C51FirstTest\main.c:60: delay(500);	
      0000A9 90 01 F4         [24]  644 	mov	dptr,#0x01f4
      0000AC 12 00 62         [24]  645 	lcall	_delay
                                    646 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\C51FirstTest\main.c:61: LED0 = 0;
                                    647 ;	assignBit
      0000AF C2 B0            [12]  648 	clr	_LED0
                                    649 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\C51FirstTest\main.c:62: LED1 = 0;
                                    650 ;	assignBit
      0000B1 C2 B1            [12]  651 	clr	_LED1
                                    652 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\C51FirstTest\main.c:63: LED2 = 0;
                                    653 ;	assignBit
      0000B3 C2 B2            [12]  654 	clr	_LED2
                                    655 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\C51FirstTest\main.c:64: LED3 = 0;
                                    656 ;	assignBit
      0000B5 C2 B3            [12]  657 	clr	_LED3
                                    658 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\C51FirstTest\main.c:65: LED4 = 0;
                                    659 ;	assignBit
      0000B7 C2 B4            [12]  660 	clr	_LED4
                                    661 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\C51FirstTest\main.c:66: LED5 = 0;
                                    662 ;	assignBit
      0000B9 C2 B5            [12]  663 	clr	_LED5
                                    664 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\C51FirstTest\main.c:67: delay(500);	
      0000BB 90 01 F4         [24]  665 	mov	dptr,#0x01f4
      0000BE 12 00 62         [24]  666 	lcall	_delay
                                    667 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\C51FirstTest\main.c:69: }
      0000C1 80 DA            [24]  668 	sjmp	00102$
                                    669 	.area CSEG    (CODE)
                                    670 	.area CONST   (CODE)
                                    671 	.area XINIT   (CODE)
                                    672 	.area CABS    (ABS,CODE)
