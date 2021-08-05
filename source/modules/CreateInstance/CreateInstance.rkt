#lang racket
(require racket/file
         racket/string
         racket/list)
;how to use
;racket CreateInstance.rkt  <inputFile> <outputFile> 
;eg :racket CreateInstance.rkt ATU.v tt.v
(define (stringLength>? str1 str2)
  (if (> (string-length str1) (string-length str2)) #t #f))
(define (stringLength<? str1 str2)
  (if (< (string-length str1) (string-length str2)) #t #f))

(define (initPort moduleDict)
  (let*-values ([(strToReturn) ""]
                [(moduleName) ((lambda ()
                                  (if (hash? moduleDict)
                                      (hash-ref moduleDict "moduleName")
                                      empty)))]
                [(subportList) ((lambda ()
                                  (if (hash? moduleDict)
                                      (hash-ref moduleDict "subportList")
                                      null)))]
                [(parameterList) ((lambda ()
                                  (if (hash? moduleDict)
                                      (hash-ref moduleDict "paramDictList")
                                      null)))]
                
                [(parameterNameList) (for/list ([eachPortDict parameterList])
                                                           (if (hash? eachPortDict)
                                                               (hash-ref eachPortDict "paraName")
                                                               "") )]
                [(nameList) (for/list ([eachPortDict subportList])
                                                           (if (hash? eachPortDict)
                                                               (hash-ref eachPortDict "name")
                                                               "") )]
                [(widthList) (for/list ([eachPortDict subportList])
                                                           (if (hash? eachPortDict)
                                                               (if (boolean? (hash-ref eachPortDict "width"))
                                                                   ""
                                                                   (hash-ref eachPortDict "width"))
                                                               "") )]
                ;获取最长端口名
                [(longestPort) (if (> (length nameList) 0 ) (let*-values (
                                             [(sortedList) (sort nameList stringLength>?)]
                                            [(lengthFirst) (string-length (list-ref sortedList 0))]) lengthFirst ) 0)]
                [(longestWidth) (if (> (length nameList) 0 )(let*-values (
                                             [(sortedList) (sort widthList stringLength>?)]
                                            [(lengthFirst) (string-length (list-ref sortedList 0))])  lengthFirst )0)]
                [(lastParameter) (if (> (length parameterNameList) 0 )(list-ref  (reverse parameterNameList) 0 )"")]
                [(lastPort) (if (> (length nameList) 0 )(list-ref  (reverse nameList) 0 )"")]
                [(strFirstListStr) (string-append* ""
                                                ((lambda ()
                                                         ;遍历
                                                         (for/list ([eachPortDict subportList])
                                                           ;(if (list? eachPortDict))
                                                           (let*-values ([(nameNow) (if (hash? eachPortDict)
                                                                                        (hash-ref eachPortDict "name")
                                                                                        null)]
                                                                         [(directionNow) (if (hash? eachPortDict)
                                                                                        (hash-ref eachPortDict "direction")
                                                                                        null)]
                                                                         [(widthNow) (if (hash? eachPortDict)
                                                                                        (if (boolean? (hash-ref eachPortDict "width"))
                                                                                            ""
                                                                                            (hash-ref eachPortDict "width"))
                                                                                        "")]
                                                                         [(allStrfirst) (if (string=? directionNow "input")
                                                                                       ;direct input
                                                                                       (let*-values ([(direction) "reg"]
                                                                                                     )
                                                                                         (string-append* direction
                                                                                                         "  "
                                                                                                         (~a widthNow #:min-width (+ longestWidth 1) #:align 'left)
                                                                                                         " " nameNow
                                                                                                         '(";\n")))
                                                                                       ;direct output)
                                                                                       (let*-values ([(direction) "wire"]
                                                                                                     )
                                                                                         (string-append* direction
                                                                                                         " "
                                                                                                         (~a widthNow #:min-width (+ longestWidth 1) #:align 'left)
                                                                                                         " "nameNow
                                                                                                         '(";\n"))))]
                                                                         )
                                                             allStrfirst)
                                                           )
                                                         )))]
                ;需要加上parameter
                [(strParameter) (if (list? parameterList)
                                    (string-append (string-append* "\n#(\n" (for/list ([eachParamDict parameterList])
                                                                                                    (let*-values ([(paramNameNow) (if (hash? eachParamDict)
                                                                                                                                      (hash-ref eachParamDict "paraName")
                                                                                                                                      null)]
                                                                                                                  [(paramValueNow) (if (hash? eachParamDict)
                                                                                                                                      (hash-ref eachParamDict "paraValue")
                                                                                                                                      null)])
                                                                                                      (string-append* "    ."
                                                                                                                      (~a paramNameNow #:min-width (+ longestPort 1) #:align 'left)
                                                                                                                      " ("
                                                                                                                      (~a paramValueNow #:min-width (+ longestPort 1) #:align 'left)
                                                                                                                      ") "
                                                                                                                      (if (string=? lastParameter paramNameNow) " " ",")
                                                                                                                      "\n" '()
                                                                                                                      ))
                                                                              ))
                                                   "\n)\n") "")]
                [(strInstListStr) (if (list? moduleName)
                                   " \n \n"
                                   (string-append
                                    (string-append* moduleName strParameter " inst_" moduleName "(\n"
                                                  ((lambda ()
                                                    ;遍历
                                                    (for/list ([eachPortDict subportList])
                                                      (let*-values ([(nameNow) (if (hash? eachPortDict)
                                                                                        (hash-ref eachPortDict "name")
                                                                                        null)]
                                                                         [(directionNow) (if (hash? eachPortDict)
                                                                                        (hash-ref eachPortDict "direction")
                                                                                        null)]
                                                                         [(widthNow) (if (hash? eachPortDict)
                                                                                        (if (boolean? (hash-ref eachPortDict "width"))
                                                                                            ""
                                                                                            (hash-ref eachPortDict "width"))
                                                                                        "")]
                                                                         [(allStr) (string-append* "    ."
                                                                                                   (~a nameNow #:min-width (+ longestPort 1) #:align 'left)
                                                                                                   " ("
                                                                                                   (~a nameNow #:min-width (+ longestPort 1) #:align 'left)
                                                                                                   ") "
                                                                                                   (if (string=? lastPort nameNow) " " ",")
                                                                                                   "// " directionNow " width : " (if (string=? widthNow "") "[0:0]" (~a widthNow #:min-width (+ longestWidth 1) #:align 'left) )
                                                                                                   "\n" '())]
                                                                         
                                                                         )
                                                             allStr)
                                                      )
                                                    ))
                                                  ) "\n);\n")) ]
                )
     (string-append strFirstListStr strInstListStr "\n")
    )
  )






(define (InstanceFileWithoutParameters inputFile outputFile)
  (if (not (file-exists? inputFile))
      inputFile
      (let*-values ([(re_commentSingleLine) #rx"\\/\\/(.*?)\n"]
              [(re_commentMultipleLine) #rx"\\/\\*.*?\\*\\/"]
              [(strFile) (file->string inputFile #:mode 'text)]
              [(withoutMultipleCommentStr) (regexp-replace* re_commentMultipleLine strFile "")]
              [(withoutCommentStr) (regexp-replace* re_commentSingleLine withoutMultipleCommentStr "")])
        (let*-values ([(eachModuleList) (regexp-split #rx"endmodule" withoutCommentStr)]
                      [(moduleNum) (- (length eachModuleList) 1)])
          (for ([eachModule eachModuleList])
            (let*-values([(re_moduleInit) #px"module\\s+(\\w+)"]
                         [(re_port) #px"(output|input|inout)(\\s+)?(wire|reg)?\\s*?(\\[.*?:.*?\\])?\\s*?(\\s+)?(\\w+)"]
                         [(re_portTest) #px"(\\s*(input|output|inout)\\s+)((wire|reg)\\s*)*((signed)\\s*)*(\\[.*?:.*?\\]\\s*)*(.*\\s*)(=?)(.*)(?=\\binput\\b|\boutput\\b|\\binout\\b|\\))"]
                         
                         [(moduleNameList) (regexp-match* re_moduleInit eachModule #:match-select cadr)]
                         [(portList) (regexp-match* re_port eachModule #:match-select rest )])
              (if  (= (length moduleNameList) 0)
                   moduleNameList
                   (let*-values ([(moduleName) (list-ref moduleNameList 0)]
                                 [(listNow) (list '())]
                                 [(portDictList) (list (for ([eachPortList portList])
                       (let*-values([(portDirection) (list-ref eachPortList 0)]
                                    [(portName) (list-ref eachPortList 5)]
                                    [(portWidth) (list-ref eachPortList 3)]
                                    )
                          (append listNow (hash "name" portName "direction" portDirection "width" portWidth)))))])
                      portDictList
                     )))
            )))))
;#px"(output|input|inout)(\\s+)?(wire|reg)?\\s*?(\\[.*?:.*?\\])?\\s*?(\\s+)?(\\(?\\w+)"
(define (InstanceFileList inputFile )
  (if (not (file-exists? inputFile))
      inputFile
      (let*-values ([(re_commentSingleLine) #rx"\\/\\/(.*?)\n"]
              [(re_commentMultipleLine) #rx"\\/\\*.*?\\*\\/"]
              [(strFile) (file->string inputFile #:mode 'text)]
              [(withoutMultipleCommentStr) (regexp-replace* re_commentMultipleLine strFile "")]
              [(withoutCommentStr) (regexp-replace* re_commentSingleLine withoutMultipleCommentStr "")]
              [(eachModuleList) (regexp-split #rx"endmodule" withoutCommentStr)]
                      [(moduleNum) (- (length eachModuleList) 1)]
                      )
  
          (for/list ([eachModule eachModuleList])
            (let*-values([(re_moduleInit) #px"module\\s+(\\w+)"]
                         [(re_port) #px"(output|input|inout)(\\s+)?(wire|reg)?\\s*?(\\[.*?:.*?\\])?\\s*?(\\s+)?(\\w+)"]
                         [(re_portTest) #px"(\\s*(input|output|inout)\\s+)((wire|reg)\\s*)*((signed)\\s*)*(\\[.*?:.*?\\]\\s*)*(.*\\s*)(=?)(.*)(?=\\binput\\b|\boutput\\b|\\binout\\b|\\))"]
                         [(re_parameter) #px"\\#\\((\\s+)?(parameter)?(.+?)(\\))"]
                         [(re_parameterValue) #px"(parameter)?(\\s+)?(\\w+?)(\\s+)?(=)(\\s+)?(.+?)(\\s+)?\n"]
                         [(moduleNameList) (regexp-match* re_moduleInit eachModule #:match-select cadr)]
                         
                         [(pamrameterDictList) (let*-values([(parameterArea)  (if (boolean?
                                                                               (regexp-match re_parameter eachModule ) )
                                                                              ""
                                                                              (list-ref (regexp-match re_parameter eachModule ) 0))]
                                                        [(parameterList)  (regexp-match* re_parameterValue parameterArea #:match-select rest)]
                                                        )
                                             ;(print ((hash "paraName" (list-ref parameterList 3) "paramValue" (list-ref parameterList 7) ))
                                             ;(print (length parameterArea) )
                                              (if (empty? parameterList) "" (for/list ([eachList parameterList]) 
                                                                             (hash "paraName" (list-ref eachList 2) "paraValue" (list-ref eachList 6))) )
                                             )]
                         [(portList) (regexp-match* re_port eachModule #:match-select rest )]
                         ;[(portDictList) ]
                         )
              (if  (= (length moduleNameList) 0)
                   #f
                   (let*-values ([(moduleName) (list-ref moduleNameList 0)]
                                 [(eachModulePortDictList)
                                  (for/list ([eachPortList portList])
                       (let*-values([(portDirection) (list-ref eachPortList 0)]
                                    [(portName) (list-ref eachPortList 5)]
                                    [(portWidth) (list-ref eachPortList 3)]
                                    [(portDict) (hash "name" portName "direction" portDirection "width" portWidth)]
                                    [(tp) '(1 2)]
                                    )
                             portDict))   ])
                         (hash "moduleName" moduleName "paramDictList" pamrameterDictList "subportList" eachModulePortDictList)
                     )))
            )
        )))

(define (CreateInstanceFile inputFile outputFile)
  (let*-values ([(moduleList) (InstanceFileList inputFile)]
                [(instStrList) (for/list ([eachModuleDict moduleList])
      (if (boolean? eachModuleDict) "" (let*-values ([(initPortStr) (initPort eachModuleDict)]
                     ;[(initInstanceStr) (initInstance eachModuleDict)]
                     )
         ;(display-to-file	initPortStr outputFile  #:exists 'replace)
                                         initPortStr
         ))
       )]
                [(instStr) (string-append* "//generate by EveIDE_LIGHT V0.0.2-alpha \n " instStrList)]
                )
    
    (display-to-file	instStr outputFile  #:exists 'replace)
  ))

(command-line
 #:args (inputFile outputFile)
 (CreateInstanceFile inputFile outputFile )
 )
