import re

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
            ((\s*)(\()(\n)?)                                             # 函数开始小括号
            (?P<name>(.+)?)
            ((\s*)(\))(\n)?)                                             # 函数结束小括号
            ((\s*)(\{)(\n)?)
            '''
compileStrA = r'((VOID)|(void)|(char)|(short)|(int)|(float)|(long)|(double))(\s*(\*)?\s*)(\w+)((\s*)(\()(\n)?)(.+)?((\s*)(\))(\n)?)((\s*)(\{)(\n)?)'
compileStrB = r"((VOID)|(void)|(char)|(short)|(int)|(float)|(long)|(double))(\s*(\*)?\s*)(\w+)((\s*)(\()(\n)?)((\s*)?(const)?(\s*)?((void)|(char)|(short)|(int)|(float)|(long)|(double))?(\s*)(\*)?(\s*)?(restrict)?(\s*)?(\w+)(\s*)?(\,)?(\n)?(.*)?)?((\s*)(\))(\n)?)"
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
if __name__ == "__main__":
    code = """
void FuncName(int param1,char param2, int  *param3, double *parma4){
    printf("hello world!\n");
}
    """
    filePath =r"C:\Users\User\Documents\GitHub\EveIDE_Plus\source\t_workspace\t_exCpro\main.c"
    with open(filePath,'r')as r:
        code0 = r.read()
        code0 = rmCommentsInCFile(code0)

    pat1 = re.compile(compileStrA, re.X)
    ret = pat1.findall(code0)
    if ret:
        for ea in ret:
            print(ea[11])
    #print(code)
    '''cl = code.split(";")

    for e in cl:
        print(e)
        ret = pat1.search(e)
        if None == ret:
            pass
            #print('不包含C函数定义!')
        else:
            #for eachIndex in range(len(ret.group())):
            print("定义"+str(ret))
        #print(ret.group())'''

