"""
    	*************************** 
    	--------EveIDE_LIGHT-------- 
 	 Author: Adancurusul
 	 Date: 2021-07-30 08:45:47
 	 LastEditors: Adancurusul
 	 LastEditTime: 2021-07-31 14:10:06
 	 Github: https://github.com/Adancurusul
 	 Email: adancurusul@gmail.com

    	***************************
    """

import re


class HdlError(Exception):
    def __init__(self,ErrorInfo):
        super().__init__(self)
        self.errorinfo=ErrorInfo
    def __str__(self):
        return self.errorinfo
 
def rmComments(text):
    singLineComments = re.compile(r'//(.*)', re.MULTILINE)
    multiLineComments = re.compile(r'/\*(.*)\*/', re.DOTALL)
    text = singLineComments.sub('', text)
    text = multiLineComments.sub('', text)
    return text

def findModuleName(text):
    modulePos = text.find('module')
    if modulePos==-1:
        raise HdlError('Syntax error: Can not find module!')
    text = text[modulePos+7:]
    modNameRe = re.match(r'\w*\s*', text)
    modName = modNameRe.group(0).strip()
    return modName

def findParams(text):
    param = r'\sparameter\s[\w\W]*?[;,)]'
    paralst = re.findall(param, text)
    if paralst!=[]:
        paramStr = '\n'.join(paralst)
        pat = r'(\w*)\s*=\s*([\w\W]*?)\s*[;,)]'
        p = re.findall(pat, paramStr)
        paramNameLst = [i[0] for i in p]
        paramValLst = [i[1] for i in p]
        return paramNameLst,paramValLst
    else:
        return [], []

def paramInstTempl(paramNameLst, paramValLst):
    if paramValLst==[]:
        return ''
    else:
        nameLen = max(len(i) for i in paramNameLst)
        valLen = max(len(i) for i in paramValLst)
        paraInst = '#(\n' + ',\n'.join('    .' + i.ljust(nameLen)
                    + '(' + k.ljust(valLen) + ')'
                    for (i,k) in zip(paramNameLst,paramValLst)) + '\n)'
        return paraInst

def findIoPorts(text):
    '''
    IO port declare syntax:
        (input | output | inout) (wire | reg) (signed) ([High:Low]) (port1,port2,port3) = (x'hxx) (,;'')
    example:
        output reg signed [MAX_WIDTH-1:0] out1, out2 = 10'd0,
    :param text: hdl context without comments and keyword 'module'
    :return: all io ports declare, include: port_name port_width port_type
    '''
    portPair = {'input':'reg', 'output':'wire', 'inout':'inout'}
    portNameLst = []
    portWidthLst = []
    portTypeLst = []

    portPat = r'(\s*(input|output|inout)\s+)((wire|reg)\s*)*((signed)\s*)*(\[.*?:.*?\]\s*)*' \
              r'(.*\s*)(=?)(.*)(?=\binput\b|\boutput\b|\binout\b|\))'

    portLst = re.findall(portPat, text)
    if len(portLst)==0:
        raise HdlError('Syntax error: Can not find io port!')
    for port in portLst:
        portnames = re.findall(r'(\S*)',port[-3])[0].split(',')
        if portnames[-1] == '':
            portnames.pop()
        for item in portnames:
            if "wire" not in item:
                portNameLst.append(item)
                portTypeLst.append(portPair[port[1]])
                portWidthLst.append(port[-4])
    return portNameLst, portWidthLst, portTypeLst

def portInstTempl(portNameLst, portWidthLst, portTypeLst):
    nameLen = max(len(i) for i in portNameLst)
    typeLen = 6 # input output inout
    widthLen = max(len(i) for i in portWidthLst)
    portInst = '(\n' + ',\n'.join('    .' + port.ljust(nameLen) + '      ('  ')' \
                for port in portNameLst)  + '\n);'
    portDeclare = '\n' + ';\n'.join(typ.ljust(typeLen) + ' ' + width.ljust(widthLen) + ' ' + name \
                            for (typ,width,name) in zip(portTypeLst,portWidthLst,portNameLst)) + ';\n\n'

    return portDeclare,portInst


def genHdlInst(text):
    textRmComments = rmComments(text)
    moduleName = findModuleName(textRmComments)
    #if moduleName=='':

    paramNameLst, paramValLst = findParams(textRmComments)

    portNameLst, portWidthLst, portTypeLst = findIoPorts(textRmComments)
    #logging.debug(portNameLst)
    portDeclare, portInst = portInstTempl(portNameLst, portWidthLst, portTypeLst)
    paraInst = paramInstTempl(paramNameLst, paramValLst)
    ts = "*******************\n"
    instTempl = portDeclare + moduleName + paraInst + ' inst_' + moduleName + portInst
    #instTempl = "protDeclare::::"+portDeclare + "moduleName:::"+moduleName +"pataInst:::"+ paraInst + ' inst_' + "moduleName:::"+moduleName + "protInst:::"+portInst
    return instTempl
class CreateInsance():

    def CreateInsance(self,inFile,outFile):#os.path.dirname(path)
        import sys
        import os
        #inFile = "C:\\Users\\User\\Documents\\Tencent Files\\1016867898\\FileRecv\\LPCE20210501\\LPCE\\RTL\\LPCE_rx.v"
        infile = open(inFile, encoding='UTF-8')
        fileCont = infile.read()
        instTempl = genHdlInst(fileCont)
        # logging.debug(instTempl)
        #outFile = "C:\\Users\\User\\Documents\\Tencent Files\\1016867898\\FileRecv\\LPCE20210501\\LPCE\\RTL\\t_LPCE_rx.v"
        outfile = open(outFile, 'w+', encoding='UTF-8')
        outfile.write(instTempl)
        infile.close()
        outfile.close()
