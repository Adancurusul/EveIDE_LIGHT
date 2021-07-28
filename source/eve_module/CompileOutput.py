import os

'''filePathNow = "E:\\codes\\MCU\\stm23cubeide\\dryer-prototype-f030\\Debug\\dryer-prototype-f030.bin"

with open(filePathNow,"rb")as r:
    byteStr = r.read()
    print("finish")
hexList = list(byteStr)
dataHex = byteStr.hex()

print(dataHex)
print(hexList)
for _ in hexList:
    pass
    #print(str(hex(_))[2:].zfill(2))'''




class CompileOutput():
    '''
    a = CompileOutput()
    str = a.get_hexStr_from_bin(filePath)
    '''

    def get_byte_str(self,filePath):
        with open(filePath, "rb")as r:
            byteStr = r.read()
        return byteStr
    def bin2coe(self,byteStr):
        hexList = self.get_hex_list(byteStr)
        headStr = "memory_initialization_radix=16;\nmemory_initialization_vector=\n"
        mainStr = ""
        for eachHexIndex in range(len(hexList)):
            if eachHexIndex == len(hexList)-1:
                mainStr += hexList[eachHexIndex] + ";\n"
            else:

                mainStr += hexList[eachHexIndex]+",\n"
        fullStr = headStr+mainStr
        return fullStr
    def bin2mif(self,byteStr):
        hexList = self.get_hex_list(byteStr)
        headStr1 = "DEPTH = "+str(len(hexList))+"; \n"
        headStr2 = '''WIDTH = 8;
ADDRESS_RADIX = DEC;
DATA_RADIX = HEX;
CONTENT
BEGIN
'''
        mainStr = ""
        endStr = "\nEND;"
        for eachHexIndex in range(len(hexList)) :
            mainStr += str(eachHexIndex)+" : "+ str(hexList[eachHexIndex]) +" ; \n"
        fullStr = headStr1+headStr2+mainStr+endStr
        return fullStr


    def bin2hexText(self,binPath):
        if os.path.exists(binPath) :
            dirpath = os.path.dirname(binPath)
            baseName = os.path.basename(binPath).split(".")[0]
            hexPath = dirpath + baseName + ".txt"
    def get_hexStr_from_bin(self,filePath) -> str:
        with open(filePath, "rb")as r:
            byteStr = r.read()
        return self.bin2hexStr(byteStr)
    def bin2hexStr(self,byteStr):
        firstLineStr = "/*********open as Little endian, word length 64bit,do not edit !*********/ \n"
        hexList = self.get_hex_list(byteStr)
        wordLen = 64
        lenHex = len(hexList)
        lines = int(lenHex/(wordLen/8))
        codeStr = ""
        codeStr+=firstLineStr
        for line in range(lines):
            for i in range(int(wordLen/8)):
                indexNow = 7-i+line*int((wordLen/8))
                codeStr += str(hexList[indexNow])
            codeStr+="\n"
        #print (codeStr)
        return codeStr




    def get_dec_list(self,byteStr) -> list:
        return list(byteStr)
    def get_hex_list(self,byteStr) -> list:
        decList = self.get_dec_list(byteStr)
        hexList = []
        for decNow in decList:
            hexnum = str(hex(decNow))[2:].zfill(2)
            hexList.append(hexnum)
        return hexList
    def get_bin_list(self,byteStr)->list:
        decList = self.get_dec_list(byteStr)
        binList = []
        for decNow in  decList:
            binNum = str(bin(decNow))[2:].zfill(2)
            binList.append(binNum)
        return binList

if __name__ == '__main__':
    filePathNow = r"D:\codes\EveIDE_Plus\EveIDE_Plus\source\t_workspace\unname\build\main.bin"
    t = CompileOutput()
    #byteStr = t.get_byte_str(filePathNow)
    hexStr = t.get_hexStr_from_bin(filePathNow)
    print(hexStr)
    byteStr = t.get_byte_str(filePathNow)
    mifStr = t.bin2mif(byteStr)
    #print(mifStr)
    with open("./test.mif","w+",newline="") as w:
        w.write(mifStr)
    coeStr = t.bin2coe(byteStr)
    with open("./test.coe","w+",newline="") as w:
        w.write(coeStr)
