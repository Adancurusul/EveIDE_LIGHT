#lang racket
(require racket/file)
;(define in (open-input-file "data.txt"))
;(read-line in)
;(close-input-port in)
;(call-with-input-file "data.txt"
;                       (lambda (in)
;                             (read-string 100 in)))

;(define args (current-command-line-arguments))
;(define c (string->number(car args)))
;(define re_commentSingleLine #rx"\\/\\/(.*?)\n")
;(define commentMultipleLine #rx"\\/\\*(?:[^\\*]|\\*+[^\\/\\*])*\\*+\\/")
;(define re_commentMultipleLine #rx"\\/\\*.*?\\*\\/")
;(define strFile (file->string "test.v" #:mode 'text))
;(define re_moduleInit  #rx"(module)(\\s+)(\\w+)")
;(\\s*(input|output|inout)\\s+)((wire|reg)\\s*)*((signed)\\s*)*(\\[.*?:.*?\\]\\s*)*(.*\\s*)(=?)(.*)(?=\\binput\\b|\boutput\\b|\\binout\\b|\\))

(define (createInstanceFile inputFile outputFile)
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
                          (display (append listNow (hash "name" portName "direction" portDirection "width" portWidth))))))])
                     (display portDictList)
                     )))
            )))))

;(output|input|inout)(\s+)(wire|reg)?(\[[\w\-\:]+\])?(\s+)?(\w+) 
;(let*-values ([(withoutMultipleCommentStr) (regexp-replace* re_commentMultipleLine strFile "")] 
;      [(withoutCommentStr) (regexp-replace* re_commentSingleLine withoutMultipleCommentStr "")])
;  withoutCommentStr)

(createInstanceFile "test.v" "t")