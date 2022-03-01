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
                                     11 	.globl _TM0_Isr
                                     12 	.globl _UART1_Isr
                                     13 	.globl _main
                                     14 	.globl _delay_ms
                                     15 	.globl _Timer0Init
                                     16 	.globl _GetUartData
                                     17 	.globl _UartPrint
                                     18 	.globl _GetUartRxdLen
                                     19 	.globl _UartInit
                                     20 	.globl _CCF0
                                     21 	.globl _CCF1
                                     22 	.globl _CCF2
                                     23 	.globl _CR
                                     24 	.globl _CF
                                     25 	.globl _RI
                                     26 	.globl _TI
                                     27 	.globl _RB8
                                     28 	.globl _TB8
                                     29 	.globl _REN
                                     30 	.globl _SM2
                                     31 	.globl _SM1
                                     32 	.globl _SM0
                                     33 	.globl _IT0
                                     34 	.globl _IE0
                                     35 	.globl _IT1
                                     36 	.globl _IE1
                                     37 	.globl _TR0
                                     38 	.globl _TF0
                                     39 	.globl _TR1
                                     40 	.globl _TF1
                                     41 	.globl _PX0
                                     42 	.globl _PT0
                                     43 	.globl _PX1
                                     44 	.globl _PT1
                                     45 	.globl _PS
                                     46 	.globl _PADC
                                     47 	.globl _PLVD
                                     48 	.globl _PPCA
                                     49 	.globl _EX0
                                     50 	.globl _ET0
                                     51 	.globl _EX1
                                     52 	.globl _ET1
                                     53 	.globl _ES
                                     54 	.globl _EADC
                                     55 	.globl _ELVD
                                     56 	.globl _EA
                                     57 	.globl _P7_7
                                     58 	.globl _P7_6
                                     59 	.globl _P7_5
                                     60 	.globl _P7_4
                                     61 	.globl _P7_3
                                     62 	.globl _P7_2
                                     63 	.globl _P7_1
                                     64 	.globl _P7_0
                                     65 	.globl _P6_7
                                     66 	.globl _P6_6
                                     67 	.globl _P6_5
                                     68 	.globl _P6_4
                                     69 	.globl _P6_3
                                     70 	.globl _P6_2
                                     71 	.globl _P6_1
                                     72 	.globl _P6_0
                                     73 	.globl _P5_7
                                     74 	.globl _P5_6
                                     75 	.globl _P5_5
                                     76 	.globl _P5_4
                                     77 	.globl _P5_3
                                     78 	.globl _P5_2
                                     79 	.globl _P5_1
                                     80 	.globl _P5_0
                                     81 	.globl _P4_7
                                     82 	.globl _P4_6
                                     83 	.globl _P4_5
                                     84 	.globl _P4_4
                                     85 	.globl _P4_3
                                     86 	.globl _P4_2
                                     87 	.globl _P4_1
                                     88 	.globl _P4_0
                                     89 	.globl _P3_7
                                     90 	.globl _P3_6
                                     91 	.globl _P3_5
                                     92 	.globl _P3_4
                                     93 	.globl _P3_3
                                     94 	.globl _P3_2
                                     95 	.globl _P3_1
                                     96 	.globl _P3_0
                                     97 	.globl _P2_7
                                     98 	.globl _P2_6
                                     99 	.globl _P2_5
                                    100 	.globl _P2_4
                                    101 	.globl _P2_3
                                    102 	.globl _P2_2
                                    103 	.globl _P2_1
                                    104 	.globl _P2_0
                                    105 	.globl _P1_7
                                    106 	.globl _P1_6
                                    107 	.globl _P1_5
                                    108 	.globl _P1_4
                                    109 	.globl _P1_3
                                    110 	.globl _P1_2
                                    111 	.globl _P1_1
                                    112 	.globl _P1_0
                                    113 	.globl _P0_7
                                    114 	.globl _P0_6
                                    115 	.globl _P0_5
                                    116 	.globl _P0_4
                                    117 	.globl _P0_3
                                    118 	.globl _P0_2
                                    119 	.globl _P0_1
                                    120 	.globl _P0_0
                                    121 	.globl _P
                                    122 	.globl _OV
                                    123 	.globl _RS0
                                    124 	.globl _RS1
                                    125 	.globl _F0
                                    126 	.globl _AC
                                    127 	.globl _CY
                                    128 	.globl _PWMFDCR
                                    129 	.globl _PWMIF
                                    130 	.globl _PWMCR
                                    131 	.globl _PWMCFG
                                    132 	.globl _CMPCR2
                                    133 	.globl _CMPCR1
                                    134 	.globl _CCAP2H
                                    135 	.globl _CCAP1H
                                    136 	.globl _CCAP0H
                                    137 	.globl _PCA_PWM2
                                    138 	.globl _PCA_PWM1
                                    139 	.globl _PCA_PWM0
                                    140 	.globl _CCAP2L
                                    141 	.globl _CCAP1L
                                    142 	.globl _CCAP0L
                                    143 	.globl _CCAPM2
                                    144 	.globl _CCAPM1
                                    145 	.globl _CCAPM0
                                    146 	.globl _CH
                                    147 	.globl _CL
                                    148 	.globl _CMOD
                                    149 	.globl _CCON
                                    150 	.globl _IAP_CONTR
                                    151 	.globl _IAP_TRIG
                                    152 	.globl _IAP_CMD
                                    153 	.globl _IAP_ADDRL
                                    154 	.globl _IAP_ADDRH
                                    155 	.globl _IAP_DATA
                                    156 	.globl _SPDAT
                                    157 	.globl _SPCTL
                                    158 	.globl _SPSTAT
                                    159 	.globl _ADC_RESL
                                    160 	.globl _ADC_RES
                                    161 	.globl _ADC_CONTR
                                    162 	.globl _SADEN
                                    163 	.globl _SADDR
                                    164 	.globl _S4BUF
                                    165 	.globl _S4CON
                                    166 	.globl _S3BUF
                                    167 	.globl _S3CON
                                    168 	.globl _S2BUF
                                    169 	.globl _S2CON
                                    170 	.globl _SBUF
                                    171 	.globl _SCON
                                    172 	.globl _WDT_CONTR
                                    173 	.globl _WKTCH
                                    174 	.globl _WKTCL
                                    175 	.globl _TL2
                                    176 	.globl _TH2
                                    177 	.globl _TL3
                                    178 	.globl _TH3
                                    179 	.globl _TL4
                                    180 	.globl _TH4
                                    181 	.globl _T2L
                                    182 	.globl _T2H
                                    183 	.globl _T3L
                                    184 	.globl _T3H
                                    185 	.globl _T4L
                                    186 	.globl _T4H
                                    187 	.globl _T3T4M
                                    188 	.globl _T4T3M
                                    189 	.globl _TH1
                                    190 	.globl _TH0
                                    191 	.globl _TL1
                                    192 	.globl _TL0
                                    193 	.globl _TMOD
                                    194 	.globl _TCON
                                    195 	.globl _INT_CLKO
                                    196 	.globl _IP2
                                    197 	.globl _IE2
                                    198 	.globl _IP
                                    199 	.globl _IE
                                    200 	.globl _P_SW2
                                    201 	.globl _P1ASF
                                    202 	.globl _BUS_SPEED
                                    203 	.globl _CLK_DIV
                                    204 	.globl _P_SW1
                                    205 	.globl _AUXR1
                                    206 	.globl _AUXR
                                    207 	.globl _PCON
                                    208 	.globl _P7M1
                                    209 	.globl _P7M0
                                    210 	.globl _P6M1
                                    211 	.globl _P6M0
                                    212 	.globl _P5M1
                                    213 	.globl _P5M0
                                    214 	.globl _P4M1
                                    215 	.globl _P4M0
                                    216 	.globl _P3M1
                                    217 	.globl _P3M0
                                    218 	.globl _P2M1
                                    219 	.globl _P2M0
                                    220 	.globl _P1M1
                                    221 	.globl _P1M0
                                    222 	.globl _P0M1
                                    223 	.globl _P0M0
                                    224 	.globl _P7
                                    225 	.globl _P6
                                    226 	.globl _P5
                                    227 	.globl _P4
                                    228 	.globl _P3
                                    229 	.globl _P2
                                    230 	.globl _P1
                                    231 	.globl _P0
                                    232 	.globl _DPH
                                    233 	.globl _DPL
                                    234 	.globl _SP
                                    235 	.globl _PSW
                                    236 	.globl _B
                                    237 	.globl _ACC
                                    238 ;--------------------------------------------------------
                                    239 ; special function registers
                                    240 ;--------------------------------------------------------
                                    241 	.area RSEG    (ABS,DATA)
      000000                        242 	.org 0x0000
                           0000E0   243 _ACC	=	0x00e0
                           0000F0   244 _B	=	0x00f0
                           0000D0   245 _PSW	=	0x00d0
                           000081   246 _SP	=	0x0081
                           000082   247 _DPL	=	0x0082
                           000083   248 _DPH	=	0x0083
                           000080   249 _P0	=	0x0080
                           000090   250 _P1	=	0x0090
                           0000A0   251 _P2	=	0x00a0
                           0000B0   252 _P3	=	0x00b0
                           0000C0   253 _P4	=	0x00c0
                           0000C8   254 _P5	=	0x00c8
                           0000E8   255 _P6	=	0x00e8
                           0000F8   256 _P7	=	0x00f8
                           000094   257 _P0M0	=	0x0094
                           000093   258 _P0M1	=	0x0093
                           000092   259 _P1M0	=	0x0092
                           000091   260 _P1M1	=	0x0091
                           000096   261 _P2M0	=	0x0096
                           000095   262 _P2M1	=	0x0095
                           0000B2   263 _P3M0	=	0x00b2
                           0000B1   264 _P3M1	=	0x00b1
                           0000B4   265 _P4M0	=	0x00b4
                           0000B3   266 _P4M1	=	0x00b3
                           0000CA   267 _P5M0	=	0x00ca
                           0000C9   268 _P5M1	=	0x00c9
                           0000CC   269 _P6M0	=	0x00cc
                           0000CB   270 _P6M1	=	0x00cb
                           0000E2   271 _P7M0	=	0x00e2
                           0000E1   272 _P7M1	=	0x00e1
                           000087   273 _PCON	=	0x0087
                           00008E   274 _AUXR	=	0x008e
                           0000A2   275 _AUXR1	=	0x00a2
                           0000A2   276 _P_SW1	=	0x00a2
                           000097   277 _CLK_DIV	=	0x0097
                           0000A1   278 _BUS_SPEED	=	0x00a1
                           00009D   279 _P1ASF	=	0x009d
                           0000BA   280 _P_SW2	=	0x00ba
                           0000A8   281 _IE	=	0x00a8
                           0000B8   282 _IP	=	0x00b8
                           0000AF   283 _IE2	=	0x00af
                           0000B5   284 _IP2	=	0x00b5
                           00008F   285 _INT_CLKO	=	0x008f
                           000088   286 _TCON	=	0x0088
                           000089   287 _TMOD	=	0x0089
                           00008A   288 _TL0	=	0x008a
                           00008B   289 _TL1	=	0x008b
                           00008C   290 _TH0	=	0x008c
                           00008D   291 _TH1	=	0x008d
                           0000D1   292 _T4T3M	=	0x00d1
                           0000D1   293 _T3T4M	=	0x00d1
                           0000D2   294 _T4H	=	0x00d2
                           0000D3   295 _T4L	=	0x00d3
                           0000D4   296 _T3H	=	0x00d4
                           0000D5   297 _T3L	=	0x00d5
                           0000D6   298 _T2H	=	0x00d6
                           0000D7   299 _T2L	=	0x00d7
                           0000D2   300 _TH4	=	0x00d2
                           0000D3   301 _TL4	=	0x00d3
                           0000D4   302 _TH3	=	0x00d4
                           0000D5   303 _TL3	=	0x00d5
                           0000D6   304 _TH2	=	0x00d6
                           0000D7   305 _TL2	=	0x00d7
                           0000AA   306 _WKTCL	=	0x00aa
                           0000AB   307 _WKTCH	=	0x00ab
                           0000C1   308 _WDT_CONTR	=	0x00c1
                           000098   309 _SCON	=	0x0098
                           000099   310 _SBUF	=	0x0099
                           00009A   311 _S2CON	=	0x009a
                           00009B   312 _S2BUF	=	0x009b
                           0000AC   313 _S3CON	=	0x00ac
                           0000AD   314 _S3BUF	=	0x00ad
                           000084   315 _S4CON	=	0x0084
                           000085   316 _S4BUF	=	0x0085
                           0000A9   317 _SADDR	=	0x00a9
                           0000B9   318 _SADEN	=	0x00b9
                           0000BC   319 _ADC_CONTR	=	0x00bc
                           0000BD   320 _ADC_RES	=	0x00bd
                           0000BE   321 _ADC_RESL	=	0x00be
                           0000CD   322 _SPSTAT	=	0x00cd
                           0000CE   323 _SPCTL	=	0x00ce
                           0000CF   324 _SPDAT	=	0x00cf
                           0000C2   325 _IAP_DATA	=	0x00c2
                           0000C3   326 _IAP_ADDRH	=	0x00c3
                           0000C4   327 _IAP_ADDRL	=	0x00c4
                           0000C5   328 _IAP_CMD	=	0x00c5
                           0000C6   329 _IAP_TRIG	=	0x00c6
                           0000C7   330 _IAP_CONTR	=	0x00c7
                           0000D8   331 _CCON	=	0x00d8
                           0000D9   332 _CMOD	=	0x00d9
                           0000E9   333 _CL	=	0x00e9
                           0000F9   334 _CH	=	0x00f9
                           0000DA   335 _CCAPM0	=	0x00da
                           0000DB   336 _CCAPM1	=	0x00db
                           0000DC   337 _CCAPM2	=	0x00dc
                           0000EA   338 _CCAP0L	=	0x00ea
                           0000EB   339 _CCAP1L	=	0x00eb
                           0000EC   340 _CCAP2L	=	0x00ec
                           0000F2   341 _PCA_PWM0	=	0x00f2
                           0000F3   342 _PCA_PWM1	=	0x00f3
                           0000F4   343 _PCA_PWM2	=	0x00f4
                           0000FA   344 _CCAP0H	=	0x00fa
                           0000FB   345 _CCAP1H	=	0x00fb
                           0000FC   346 _CCAP2H	=	0x00fc
                           0000E6   347 _CMPCR1	=	0x00e6
                           0000E7   348 _CMPCR2	=	0x00e7
                           0000F1   349 _PWMCFG	=	0x00f1
                           0000F5   350 _PWMCR	=	0x00f5
                           0000F6   351 _PWMIF	=	0x00f6
                           0000F7   352 _PWMFDCR	=	0x00f7
                                    353 ;--------------------------------------------------------
                                    354 ; special function bits
                                    355 ;--------------------------------------------------------
                                    356 	.area RSEG    (ABS,DATA)
      000000                        357 	.org 0x0000
                           0000D7   358 _CY	=	0x00d7
                           0000D6   359 _AC	=	0x00d6
                           0000D5   360 _F0	=	0x00d5
                           0000D4   361 _RS1	=	0x00d4
                           0000D3   362 _RS0	=	0x00d3
                           0000D2   363 _OV	=	0x00d2
                           0000D0   364 _P	=	0x00d0
                           000080   365 _P0_0	=	0x0080
                           000081   366 _P0_1	=	0x0081
                           000082   367 _P0_2	=	0x0082
                           000083   368 _P0_3	=	0x0083
                           000084   369 _P0_4	=	0x0084
                           000085   370 _P0_5	=	0x0085
                           000086   371 _P0_6	=	0x0086
                           000087   372 _P0_7	=	0x0087
                           000090   373 _P1_0	=	0x0090
                           000091   374 _P1_1	=	0x0091
                           000092   375 _P1_2	=	0x0092
                           000093   376 _P1_3	=	0x0093
                           000094   377 _P1_4	=	0x0094
                           000095   378 _P1_5	=	0x0095
                           000096   379 _P1_6	=	0x0096
                           000097   380 _P1_7	=	0x0097
                           0000A0   381 _P2_0	=	0x00a0
                           0000A1   382 _P2_1	=	0x00a1
                           0000A2   383 _P2_2	=	0x00a2
                           0000A3   384 _P2_3	=	0x00a3
                           0000A4   385 _P2_4	=	0x00a4
                           0000A5   386 _P2_5	=	0x00a5
                           0000A6   387 _P2_6	=	0x00a6
                           0000A7   388 _P2_7	=	0x00a7
                           0000B0   389 _P3_0	=	0x00b0
                           0000B1   390 _P3_1	=	0x00b1
                           0000B2   391 _P3_2	=	0x00b2
                           0000B3   392 _P3_3	=	0x00b3
                           0000B4   393 _P3_4	=	0x00b4
                           0000B5   394 _P3_5	=	0x00b5
                           0000B6   395 _P3_6	=	0x00b6
                           0000B7   396 _P3_7	=	0x00b7
                           0000C0   397 _P4_0	=	0x00c0
                           0000C1   398 _P4_1	=	0x00c1
                           0000C2   399 _P4_2	=	0x00c2
                           0000C3   400 _P4_3	=	0x00c3
                           0000C4   401 _P4_4	=	0x00c4
                           0000C5   402 _P4_5	=	0x00c5
                           0000C6   403 _P4_6	=	0x00c6
                           0000C7   404 _P4_7	=	0x00c7
                           0000C8   405 _P5_0	=	0x00c8
                           0000C9   406 _P5_1	=	0x00c9
                           0000CA   407 _P5_2	=	0x00ca
                           0000CB   408 _P5_3	=	0x00cb
                           0000CC   409 _P5_4	=	0x00cc
                           0000CD   410 _P5_5	=	0x00cd
                           0000CE   411 _P5_6	=	0x00ce
                           0000CF   412 _P5_7	=	0x00cf
                           0000E8   413 _P6_0	=	0x00e8
                           0000E9   414 _P6_1	=	0x00e9
                           0000EA   415 _P6_2	=	0x00ea
                           0000EB   416 _P6_3	=	0x00eb
                           0000EC   417 _P6_4	=	0x00ec
                           0000ED   418 _P6_5	=	0x00ed
                           0000EE   419 _P6_6	=	0x00ee
                           0000EF   420 _P6_7	=	0x00ef
                           0000F8   421 _P7_0	=	0x00f8
                           0000F9   422 _P7_1	=	0x00f9
                           0000FA   423 _P7_2	=	0x00fa
                           0000FB   424 _P7_3	=	0x00fb
                           0000FC   425 _P7_4	=	0x00fc
                           0000FD   426 _P7_5	=	0x00fd
                           0000FE   427 _P7_6	=	0x00fe
                           0000FF   428 _P7_7	=	0x00ff
                           0000AF   429 _EA	=	0x00af
                           0000AE   430 _ELVD	=	0x00ae
                           0000AD   431 _EADC	=	0x00ad
                           0000AC   432 _ES	=	0x00ac
                           0000AB   433 _ET1	=	0x00ab
                           0000AA   434 _EX1	=	0x00aa
                           0000A9   435 _ET0	=	0x00a9
                           0000A8   436 _EX0	=	0x00a8
                           0000BF   437 _PPCA	=	0x00bf
                           0000BE   438 _PLVD	=	0x00be
                           0000BD   439 _PADC	=	0x00bd
                           0000BC   440 _PS	=	0x00bc
                           0000BB   441 _PT1	=	0x00bb
                           0000BA   442 _PX1	=	0x00ba
                           0000B9   443 _PT0	=	0x00b9
                           0000B8   444 _PX0	=	0x00b8
                           00008F   445 _TF1	=	0x008f
                           00008E   446 _TR1	=	0x008e
                           00008D   447 _TF0	=	0x008d
                           00008C   448 _TR0	=	0x008c
                           00008B   449 _IE1	=	0x008b
                           00008A   450 _IT1	=	0x008a
                           000089   451 _IE0	=	0x0089
                           000088   452 _IT0	=	0x0088
                           00009F   453 _SM0	=	0x009f
                           00009E   454 _SM1	=	0x009e
                           00009D   455 _SM2	=	0x009d
                           00009C   456 _REN	=	0x009c
                           00009B   457 _TB8	=	0x009b
                           00009A   458 _RB8	=	0x009a
                           000099   459 _TI	=	0x0099
                           000098   460 _RI	=	0x0098
                           0000DF   461 _CF	=	0x00df
                           0000DE   462 _CR	=	0x00de
                           0000DA   463 _CCF2	=	0x00da
                           0000D9   464 _CCF1	=	0x00d9
                           0000D8   465 _CCF0	=	0x00d8
                                    466 ;--------------------------------------------------------
                                    467 ; overlayable register banks
                                    468 ;--------------------------------------------------------
                                    469 	.area REG_BANK_0	(REL,OVR,DATA)
      000000                        470 	.ds 8
                                    471 ;--------------------------------------------------------
                                    472 ; internal ram data
                                    473 ;--------------------------------------------------------
                                    474 	.area DSEG    (DATA)
                                    475 ;--------------------------------------------------------
                                    476 ; overlayable items in internal ram 
                                    477 ;--------------------------------------------------------
                                    478 ;--------------------------------------------------------
                                    479 ; Stack segment in internal ram 
                                    480 ;--------------------------------------------------------
                                    481 	.area	SSEG
      000033                        482 __start__stack:
      000033                        483 	.ds	1
                                    484 
                                    485 ;--------------------------------------------------------
                                    486 ; indirectly addressable internal ram data
                                    487 ;--------------------------------------------------------
                                    488 	.area ISEG    (DATA)
                                    489 ;--------------------------------------------------------
                                    490 ; absolute internal ram data
                                    491 ;--------------------------------------------------------
                                    492 	.area IABS    (ABS,DATA)
                                    493 	.area IABS    (ABS,DATA)
                                    494 ;--------------------------------------------------------
                                    495 ; bit data
                                    496 ;--------------------------------------------------------
                                    497 	.area BSEG    (BIT)
                                    498 ;--------------------------------------------------------
                                    499 ; paged external ram data
                                    500 ;--------------------------------------------------------
                                    501 	.area PSEG    (PAG,XDATA)
                                    502 ;--------------------------------------------------------
                                    503 ; external ram data
                                    504 ;--------------------------------------------------------
                                    505 	.area XSEG    (XDATA)
                                    506 ;--------------------------------------------------------
                                    507 ; absolute external ram data
                                    508 ;--------------------------------------------------------
                                    509 	.area XABS    (ABS,XDATA)
                                    510 ;--------------------------------------------------------
                                    511 ; external initialized ram data
                                    512 ;--------------------------------------------------------
                                    513 	.area XISEG   (XDATA)
                                    514 	.area HOME    (CODE)
                                    515 	.area GSINIT0 (CODE)
                                    516 	.area GSINIT1 (CODE)
                                    517 	.area GSINIT2 (CODE)
                                    518 	.area GSINIT3 (CODE)
                                    519 	.area GSINIT4 (CODE)
                                    520 	.area GSINIT5 (CODE)
                                    521 	.area GSINIT  (CODE)
                                    522 	.area GSFINAL (CODE)
                                    523 	.area CSEG    (CODE)
                                    524 ;--------------------------------------------------------
                                    525 ; interrupt vector 
                                    526 ;--------------------------------------------------------
                                    527 	.area HOME    (CODE)
      000000                        528 __interrupt_vect:
      000000 02 00 29         [24]  529 	ljmp	__sdcc_gsinit_startup
      000003 32               [24]  530 	reti
      000004                        531 	.ds	7
      00000B 02 01 7A         [24]  532 	ljmp	_TM0_Isr
      00000E                        533 	.ds	5
      000013 32               [24]  534 	reti
      000014                        535 	.ds	7
      00001B 32               [24]  536 	reti
      00001C                        537 	.ds	7
      000023 02 00 EA         [24]  538 	ljmp	_UART1_Isr
                                    539 ;--------------------------------------------------------
                                    540 ; global & static initialisations
                                    541 ;--------------------------------------------------------
                                    542 	.area HOME    (CODE)
                                    543 	.area GSINIT  (CODE)
                                    544 	.area GSFINAL (CODE)
                                    545 	.area GSINIT  (CODE)
                                    546 	.globl __sdcc_gsinit_startup
                                    547 	.globl __sdcc_program_startup
                                    548 	.globl __start__stack
                                    549 	.globl __mcs51_genXINIT
                                    550 	.globl __mcs51_genXRAMCLEAR
                                    551 	.globl __mcs51_genRAMCLEAR
                                    552 	.area GSFINAL (CODE)
      000082 02 00 26         [24]  553 	ljmp	__sdcc_program_startup
                                    554 ;--------------------------------------------------------
                                    555 ; Home
                                    556 ;--------------------------------------------------------
                                    557 	.area HOME    (CODE)
                                    558 	.area HOME    (CODE)
      000026                        559 __sdcc_program_startup:
      000026 02 00 85         [24]  560 	ljmp	_main
                                    561 ;	return from main will return to caller
                                    562 ;--------------------------------------------------------
                                    563 ; code
                                    564 ;--------------------------------------------------------
                                    565 	.area CSEG    (CODE)
                                    566 ;------------------------------------------------------------
                                    567 ;Allocation info for local variables in function 'main'
                                    568 ;------------------------------------------------------------
                                    569 ;tmp                       Allocated to registers r7 
                                    570 ;mybuf                     Allocated to stack - _bp +1
                                    571 ;------------------------------------------------------------
                                    572 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:13: void main(void)
                                    573 ;	-----------------------------------------
                                    574 ;	 function main
                                    575 ;	-----------------------------------------
      000085                        576 _main:
                           000007   577 	ar7 = 0x07
                           000006   578 	ar6 = 0x06
                           000005   579 	ar5 = 0x05
                           000004   580 	ar4 = 0x04
                           000003   581 	ar3 = 0x03
                           000002   582 	ar2 = 0x02
                           000001   583 	ar1 = 0x01
                           000000   584 	ar0 = 0x00
      000085 C0 0A            [24]  585 	push	_bp
      000087 E5 81            [12]  586 	mov	a,sp
      000089 F5 0A            [12]  587 	mov	_bp,a
      00008B 24 10            [12]  588 	add	a,#0x10
      00008D F5 81            [12]  589 	mov	sp,a
                                    590 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:18: UartInit();
      00008F 12 01 C5         [24]  591 	lcall	_UartInit
                                    592 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:19: Timer0Init();
      000092 12 02 C5         [24]  593 	lcall	_Timer0Init
                                    594 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:21: EA = 1;		//允许全局中断
                                    595 ;	assignBit
      000095 D2 AF            [12]  596 	setb	_EA
                                    597 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:23: UartPrint("0123456789012345abcdef");
      000097 90 03 3F         [24]  598 	mov	dptr,#___str_0
      00009A 75 F0 80         [24]  599 	mov	b,#0x80
      00009D 12 02 6F         [24]  600 	lcall	_UartPrint
                                    601 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:24: while (1)
      0000A0                        602 00104$:
                                    603 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:26: led1 = !led1;
      0000A0 B2 A6            [12]  604 	cpl	_P2_6
                                    605 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:27: P4_1 = !P4_1;
      0000A2 B2 C1            [12]  606 	cpl	_P4_1
                                    607 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:29: delay_ms(50);
      0000A4 75 82 32         [24]  608 	mov	dpl,#0x32
      0000A7 12 02 D8         [24]  609 	lcall	_delay_ms
                                    610 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:31: tmp = GetUartRxdLen();
      0000AA 12 02 6A         [24]  611 	lcall	_GetUartRxdLen
                                    612 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:33: if(tmp){
      0000AD E5 82            [12]  613 	mov	a,dpl
      0000AF FF               [12]  614 	mov	r7,a
      0000B0 60 EE            [24]  615 	jz	00104$
                                    616 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:35: GetUartData(mybuf,tmp);
      0000B2 AE 0A            [24]  617 	mov	r6,_bp
      0000B4 0E               [12]  618 	inc	r6
      0000B5 8E 03            [24]  619 	mov	ar3,r6
      0000B7 7C 00            [12]  620 	mov	r4,#0x00
      0000B9 7D 40            [12]  621 	mov	r5,#0x40
      0000BB C0 07            [24]  622 	push	ar7
      0000BD C0 06            [24]  623 	push	ar6
      0000BF C0 07            [24]  624 	push	ar7
      0000C1 8B 82            [24]  625 	mov	dpl,r3
      0000C3 8C 83            [24]  626 	mov	dph,r4
      0000C5 8D F0            [24]  627 	mov	b,r5
      0000C7 12 01 FC         [24]  628 	lcall	_GetUartData
      0000CA 15 81            [12]  629 	dec	sp
      0000CC D0 06            [24]  630 	pop	ar6
      0000CE D0 07            [24]  631 	pop	ar7
                                    632 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:36: mybuf[tmp] = 0;
      0000D0 EF               [12]  633 	mov	a,r7
      0000D1 2E               [12]  634 	add	a,r6
      0000D2 F8               [12]  635 	mov	r0,a
      0000D3 76 00            [12]  636 	mov	@r0,#0x00
                                    637 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:38: UartPrint((const u8 *)mybuf);
      0000D5 7F 00            [12]  638 	mov	r7,#0x00
      0000D7 7D 40            [12]  639 	mov	r5,#0x40
      0000D9 8E 82            [24]  640 	mov	dpl,r6
      0000DB 8F 83            [24]  641 	mov	dph,r7
      0000DD 8D F0            [24]  642 	mov	b,r5
      0000DF 12 02 6F         [24]  643 	lcall	_UartPrint
      0000E2 80 BC            [24]  644 	sjmp	00104$
                                    645 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:41: }
      0000E4 85 0A 81         [24]  646 	mov	sp,_bp
      0000E7 D0 0A            [24]  647 	pop	_bp
      0000E9 22               [24]  648 	ret
                                    649 ;------------------------------------------------------------
                                    650 ;Allocation info for local variables in function 'UART1_Isr'
                                    651 ;------------------------------------------------------------
                                    652 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:44: void UART1_Isr() __interrupt UART1_VECTOR
                                    653 ;	-----------------------------------------
                                    654 ;	 function UART1_Isr
                                    655 ;	-----------------------------------------
      0000EA                        656 _UART1_Isr:
      0000EA C0 E0            [24]  657 	push	acc
      0000EC C0 07            [24]  658 	push	ar7
      0000EE C0 06            [24]  659 	push	ar6
      0000F0 C0 01            [24]  660 	push	ar1
      0000F2 C0 00            [24]  661 	push	ar0
      0000F4 C0 D0            [24]  662 	push	psw
      0000F6 75 D0 00         [24]  663 	mov	psw,#0x00
                                    664 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:46: if (TI) {
                                    665 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:47: TI = 0;
                                    666 ;	assignBit
      0000F9 10 99 02         [24]  667 	jbc	_TI,00152$
      0000FC 80 2D            [24]  668 	sjmp	00116$
      0000FE                        669 00152$:
                                    670 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:48: if (txdData.index < txdData.len){
      0000FE 78 2F            [12]  671 	mov	r0,#(_txdData + 0x0010)
      000100 86 07            [24]  672 	mov	ar7,@r0
      000102 78 30            [12]  673 	mov	r0,#(_txdData + 0x0011)
      000104 86 06            [24]  674 	mov	ar6,@r0
      000106 C3               [12]  675 	clr	c
      000107 EF               [12]  676 	mov	a,r7
      000108 9E               [12]  677 	subb	a,r6
      000109 50 12            [24]  678 	jnc	00102$
                                    679 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:49: SBUF = txdData.buf[txdData.index];
      00010B 78 2F            [12]  680 	mov	r0,#(_txdData + 0x0010)
      00010D E6               [12]  681 	mov	a,@r0
      00010E 24 1F            [12]  682 	add	a,#_txdData
      000110 F9               [12]  683 	mov	r1,a
      000111 87 99            [24]  684 	mov	_SBUF,@r1
                                    685 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:50: txdData.index++;
      000113 78 2F            [12]  686 	mov	r0,#(_txdData + 0x0010)
      000115 E6               [12]  687 	mov	a,@r0
      000116 FF               [12]  688 	mov	r7,a
      000117 04               [12]  689 	inc	a
      000118 78 2F            [12]  690 	mov	r0,#(_txdData + 0x0010)
      00011A F6               [12]  691 	mov	@r0,a
      00011B 80 50            [24]  692 	sjmp	00118$
      00011D                        693 00102$:
                                    694 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:52: txdData.busy=false;
      00011D 78 31            [12]  695 	mov	r0,#(_txdData + 0x0012)
      00011F 76 00            [12]  696 	mov	@r0,#0x00
                                    697 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:53: txdData.len = 0;
      000121 78 30            [12]  698 	mov	r0,#(_txdData + 0x0011)
      000123 76 00            [12]  699 	mov	@r0,#0x00
                                    700 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:54: txdData.index = 0;
      000125 78 2F            [12]  701 	mov	r0,#(_txdData + 0x0010)
      000127 76 00            [12]  702 	mov	@r0,#0x00
      000129 80 42            [24]  703 	sjmp	00118$
      00012B                        704 00116$:
                                    705 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:56: }else if (RI){
                                    706 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:57: RI = 0;
                                    707 ;	assignBit
      00012B 10 98 02         [24]  708 	jbc	_RI,00154$
      00012E 80 3D            [24]  709 	sjmp	00118$
      000130                        710 00154$:
                                    711 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:58: if(rxdData.len < RXD_LENGTH){
      000130 78 1C            [12]  712 	mov	r0,#(_rxdData + 0x0011)
      000132 86 07            [24]  713 	mov	ar7,@r0
      000134 BF 10 00         [24]  714 	cjne	r7,#0x10,00155$
      000137                        715 00155$:
      000137 50 30            [24]  716 	jnc	00111$
                                    717 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:59: rxdData.buf[rxdData.len] = SBUF;
      000139 78 1C            [12]  718 	mov	r0,#(_rxdData + 0x0011)
      00013B E6               [12]  719 	mov	a,@r0
      00013C 24 0B            [12]  720 	add	a,#_rxdData
      00013E F8               [12]  721 	mov	r0,a
      00013F A6 99            [24]  722 	mov	@r0,_SBUF
                                    723 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:60: rxdData.len++;
      000141 78 1C            [12]  724 	mov	r0,#(_rxdData + 0x0011)
      000143 E6               [12]  725 	mov	a,@r0
      000144 04               [12]  726 	inc	a
      000145 78 1C            [12]  727 	mov	r0,#(_rxdData + 0x0011)
      000147 F6               [12]  728 	mov	@r0,a
                                    729 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:61: if(rxdData.len==3){
      000148 78 1C            [12]  730 	mov	r0,#(_rxdData + 0x0011)
      00014A 86 07            [24]  731 	mov	ar7,@r0
      00014C BF 03 1E         [24]  732 	cjne	r7,#0x03,00118$
                                    733 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:62: if((rxdData.buf[0]==0x5a)&&
      00014F 78 0B            [12]  734 	mov	r0,#_rxdData
      000151 86 07            [24]  735 	mov	ar7,@r0
      000153 BF 5A 17         [24]  736 	cjne	r7,#0x5a,00118$
                                    737 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:63: (rxdData.buf[1]==0x3a)&&
      000156 78 0C            [12]  738 	mov	r0,#(_rxdData + 0x0001)
      000158 86 07            [24]  739 	mov	ar7,@r0
      00015A BF 3A 10         [24]  740 	cjne	r7,#0x3a,00118$
                                    741 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:64: (rxdData.buf[2]==0x6c))
      00015D 78 0D            [12]  742 	mov	r0,#(_rxdData + 0x0002)
      00015F 86 07            [24]  743 	mov	ar7,@r0
      000161 BF 6C 09         [24]  744 	cjne	r7,#0x6c,00118$
                                    745 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:65: RS_ISP;
      000164 43 C7 60         [24]  746 	orl	_IAP_CONTR,#0x60
      000167 80 04            [24]  747 	sjmp	00118$
      000169                        748 00111$:
                                    749 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:68: rxdData.len = 0;
      000169 78 1C            [12]  750 	mov	r0,#(_rxdData + 0x0011)
      00016B 76 00            [12]  751 	mov	@r0,#0x00
      00016D                        752 00118$:
                                    753 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:71: }
      00016D D0 D0            [24]  754 	pop	psw
      00016F D0 00            [24]  755 	pop	ar0
      000171 D0 01            [24]  756 	pop	ar1
      000173 D0 06            [24]  757 	pop	ar6
      000175 D0 07            [24]  758 	pop	ar7
      000177 D0 E0            [24]  759 	pop	acc
      000179 32               [24]  760 	reti
                                    761 ;	eliminated unneeded push/pop dpl
                                    762 ;	eliminated unneeded push/pop dph
                                    763 ;	eliminated unneeded push/pop b
                                    764 ;------------------------------------------------------------
                                    765 ;Allocation info for local variables in function 'TM0_Isr'
                                    766 ;------------------------------------------------------------
                                    767 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:73: void TM0_Isr() __interrupt 1     //
                                    768 ;	-----------------------------------------
                                    769 ;	 function TM0_Isr
                                    770 ;	-----------------------------------------
      00017A                        771 _TM0_Isr:
      00017A C0 E0            [24]  772 	push	acc
                                    773 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:76: if(time_count)  time_count--;
      00017C E5 08            [12]  774 	mov	a,_time_count
      00017E 60 05            [24]  775 	jz	00103$
      000180 E5 08            [12]  776 	mov	a,_time_count
      000182 14               [12]  777 	dec	a
      000183 F5 08            [12]  778 	mov	_time_count,a
      000185                        779 00103$:
                                    780 ;	C:\Users\User\Documents\GitHub\EveIDE_LIGHT\source\t_workspace\02target002\main.c:77: }
      000185 D0 E0            [24]  781 	pop	acc
      000187 32               [24]  782 	reti
                                    783 ;	eliminated unneeded mov psw,# (no regs used in bank)
                                    784 ;	eliminated unneeded push/pop psw
                                    785 ;	eliminated unneeded push/pop dpl
                                    786 ;	eliminated unneeded push/pop dph
                                    787 ;	eliminated unneeded push/pop b
                                    788 	.area CSEG    (CODE)
                                    789 	.area CONST   (CODE)
      00033F                        790 ___str_0:
      00033F 30 31 32 33 34 35 36   791 	.ascii "0123456789012345abcdef"
             37 38 39 30 31 32 33
             34 35 61 62 63 64 65
             66
      000355 00                     792 	.db 0x00
                                    793 	.area XINIT   (CODE)
                                    794 	.area CABS    (ABS,CODE)
