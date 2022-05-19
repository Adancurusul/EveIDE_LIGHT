"""
    	*************************** 
    	--------EveIDE_LIGHT-------- 
 	 Author: Adancurusul
 	 Date: 2021-07-23 08:53:01
 	 LastEditors: Adancurusul
 	 LastEditTime: 2021-07-31 14:10:17
 	 Github: https://github.com/Adancurusul
 	 Email: adancurusul@gmail.com

    	***************************
    """
import os
import re
import logging
g_allFuncList = [] 
def get1stSymPos( s, fromPos=0):
    g_DictSymbols = {'"': '"', '/*': '*/', '//': '\n'}
    listPos = []  # 位置,符号
    for b in g_DictSymbols:
        pos = s.find(b, fromPos)
        listPos.append((pos, b))  # 插入位置以及结束符号
    minIndex = -1  # 最小位置在listPos中的索引
    index = 0  # 索引
    while index < len(listPos):
        pos = listPos[index][0]  # 位置
        if minIndex < 0 and pos >= 0:  # 第一个非负位置
            minIndex = index
        if 0 <= pos < listPos[minIndex][0]:  # 后面出现的更靠前的位置
            minIndex = index
        index = index + 1
    if minIndex == -1:  # 没找到
        return (-1, None)
    else:
        return (listPos[minIndex])

def rmCommentsInCFile(s):
    g_DictSymbols = {'"': '"', '/*': '*/', '//': '\n'}

    if not isinstance(s, str):
        raise TypeError(s)
    fromPos = 0
    while (fromPos < len(s)):
        result = get1stSymPos(s, fromPos)

        if result[0] == -1:  # 没有符号了
            return s
        else:
            endPos = s.find(g_DictSymbols[result[1]], result[0] + len(result[1]))
            if result[1] == '//':  # 单行注释
                if endPos == -1:  # 没有换行符也可以
                    endPos = len(s)
                s = s.replace(s[result[0]:endPos], ' ', 1)
                fromPos = result[0]
            elif result[1] == '/*':  # 区块注释
                if endPos == -1:  # 没有结束符就报错
                    raise ValueError("块状注释未闭合")
                s = s.replace(s[result[0]:endPos + 2], ' ', 1)
                fromPos = result[0]
            else:  # 字符串
                if endPos == -1:  # 没有结束符就报错
                    raise ValueError("符号未闭合")
                fromPos = endPos + len(g_DictSymbols[result[1]])
    return s
rgl_exp1 = r'''  
            ((VOID)|(void)|(char)|(short)|(int)|(float)|(long)|(double)) # 识别函数返回值类型
            (\s*(\*)?\s*)                                                # 识别返回值是否为指针类型以及中间是否包含空格
            (\w+)                                                        # 识别函数名
            ((\s*)(\()(\n)?)                                             # 函数开始小括号
            ((\s*)?(const)?(\s*)?                                        # 参数前是否有const
            ((void)|(char)|(short)|(int)|(float)|(long)|(double))?        # 参数类型
            (\s*)(\*)?(\s*)?(restrict)?(\s*)?(\w+)(\s*)?(\,)?(\n)?(.*)?)?# 最后的*表示有多个参数
            ((\s*)(\))(\n)?)                                             # 函数结束小括号
            '''

rgl_exp12 = r'''  
            ((VOID)|(void)|(char)|(short)|(int)|(float)|(long)|(double)) # 识别函数返回值类型
            (\s*(\*)?\s*)                                                # 识别返回值是否为指针类型以及中间是否包含空格
            (\w+)                                                        # 识别函数名
            ((\s*)(\()(\n)?)                                             # 函数开始括号
            (?P<name>(.+)?)
            ((\s*)(\))(\n)?)                                             # 函数结束括号
            ((\s*)(\{)(\n)?)
            '''
compileStrA = r'((VOID)|(void)|(char)|(short)|(int)|(float)|(long)|(double))(\s*(\*)?\s*)(\w+)((\s*)(\()(\n)?)(.+)?((\s*)(\))(\n)?)((\s*)(\{)(\n)?)'
compileStrB = r"((VOID)|(void)|(char)|(short)|(int)|(float)|(long)|(double))(\s*(\*)?\s*)(\w+)((\s*)(\()(\n)?)((\s*)?(const)?(\s*)?((void)|(char)|(short)|(int)|(float)|(long)|(double))?(\s*)(\*)?(\s*)?(restrict)?(\s*)?(\w+)(\s*)?(\,)?(\n)?(.*)?)?((\s*)(\))(\n)?)"

class GetFunctionInC:
    def __init__(self,filePath):
        self.filePath = filePath
        self.fuctionList = []
        if os.path.exists(filePath):
            pass
        try :
            with open(filePath,"r",encoding='utf-8') as rFile:
                code0 = rFile.read()
                code0 = rmCommentsInCFile(code0)
            self.codeNow = code0
            self.fuctionList = self.get_function(self.codeNow)
            logging.debug("finishGettingFunction")
        except Exception as e:
            logging.debug("fail to get function in file "+str(e))
    def get_function(self,codeNow):
        functionList = []
        pat1 = re.compile(compileStrA, re.X)
        ret = pat1.findall(codeNow)
        if ret:
            for ea in ret:
                logging.debug("find function in c file "+self.filePath+str(ea[11]))
                functionList.append(ea[11])
        return functionList




class GetFunctionInCWithoutRe:
    def __init__(self, fileFullName):
        self.KEYWORD_LIST_FUNC = ['if', 'while', 'for', 'switch']
        self.current_row = -1
        self.current_line = 0
        self.fullName = fileFullName
        if not os.path.exists(fileFullName):
            return None  # 文件名为空  或者 文件不存在
        try:
            fin = open(self.fullName, "r", encoding='utf-8', errors="ignore")
            input_file = fin.read()
            fin.close()
        except:
            fin.close()
            return None  # 打开文件失败
        self.input_str = input_file.splitlines(False)
        self.max_line = len(self.input_str) - 1

    def getchar(self):  # 从整个文档中取出一个 char
        self.current_row += 1
        if self.current_row == len(self.input_str[self.current_line]):
            self.current_line += 1
            self.current_row = 0
            while True:
                print(self.current_row)
                print(self.input_str)
                # print("*")
                if len(self.input_str[self.current_line]) != 0:
                    break
                self.current_line += 1
        if self.current_line == self.max_line:
            return 'SCANEOF'
        return self.input_str[self.current_line][self.current_row]

    def ungetchar(self):  # 往文档存回一个 char
        self.current_row = self.current_row - 1
        if self.current_row < 0:
            self.current_line = self.current_line - 1
            self.current_row = len(self.input_str[self.current_line]) - 1
        return self.input_str[self.current_line][self.current_row]

    def getFunctionNameInLine(self, strline):
        for i in range(0, len(strline)):
            if strline[i] == '(':
                break
        else:
            return None
        j = i - 1
        for i in range(j, -1, -1):
            if ord(strline[i]) > 127:  # 非 ASCII 码
                return None
            if strline[i].isalnum() == False and strline[i] != '_':  # 含有非函数名字符则停止
                str1 = strline[i + 1: j + 1]
                if str1 in self.KEYWORD_LIST_FUNC:  # 不是关键字
                    break
                else:  # 函数名
                    return str1
        return None

    def scanFunction(self):
        global g_allFuncList
        if self.current_line == self.max_line:
            return ('SCANEOF', self.max_line)

        str1 = self.input_str[self.current_line].strip()
        if len(str1) == 0:  # 空行
            self.current_line += 1
            self.current_row = -1
            return None
        if '(' not in str1:  # 没有 左括号
            self.current_line += 1
            self.current_row = -1
            return None
        # 本行出现(,记录行号
        lineOfLeft = self.current_line
        while (True):
            # 查找‘)’  -->  {
            current_char = self.getchar()
            if current_char == ')':  # 后面可能有注释 /**/  或者  //    跳过   ;还有=跳过
                while (True):
                    current_char = self.getchar()
                    if current_char == '{':  # 当前行中包含函数名，记录行号和获取函数名
                        str1 = self.getFunctionNameInLine(self.input_str[lineOfLeft])
                        if str1:
                            g_allFuncList.append(str1)
                            return (str1, lineOfLeft)
                        return None
                    elif current_char == '(':
                        lineOfLeft = self.current_line
                        continue
                    elif current_char == ';' or current_char == '=':  # 分号表示此处为函数调用，并非函数体跳过  =可能是函数指针数组
                        self.current_line += 1
                        self.current_row = -1
                        return None
                    elif current_char == '/':
                        next_char = self.getchar()
                        if next_char == '/':  # 单行注释跳过当前行，下面已经是下一行
                            self.current_line += 1
                            self.current_row = -1
                            next_char = self.getchar()  # 换行的第一个是 ｛ 认为是函数所在行
                            if next_char == '{':  # 行首是 { ,将字符存回去 ，回到当前的while开始处
                                self.ungetchar()
                                continue
                            elif next_char == 'SCANEOF':
                                return ('SCANEOF', 0)
                            else:
                                return None
                        elif current_char == '*':  # 块注释  /**/
                            next_char = self.getchar()
                            while True:
                                if next_char == '*':
                                    end_char = self.getchar()
                                    if end_char == '/':
                                        break
                                    if end_char == 'SCANEOF':
                                        return ('SCANEOF', 0)
                                elif next_char == 'SCANEOF':
                                    return ('SCANEOF', 0)
                                next_char = self.getchar()

    #
    # find and return the filename and functiondict
    # fileanme ,functiondict{key = funname,value = line}
    def lexer_analysis(self):
        [dirname, filename] = os.path.split(self.fullName)
        # print(self.fullName)
        funcDict = {}  # 本字典 属于 子自典，key = 函数名,value = 行号
        # 分析c文件，一直到文档结束
        while True:
            r = self.scanFunction()
            if r is not None:
                if r[0] == 'SCANEOF':  # 文档结尾，结束查找
                    break
                funcDict.setdefault(r[0], r[1])  # 查找到函数名，记录所在行号
        return (filename, funcDict)

if __name__ == '__main__':
    pass