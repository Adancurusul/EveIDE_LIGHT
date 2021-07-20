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
        firstLineStr = "/*********Little endian, word length 64bit*********/"
        hexList = self.get_hex_list(byteStr)
        lenHex = len(hexList)
        lines = int(lenHex/4)
        codeStr = ""
        for line in range(lines):
            for i in range(4):
                indexNow = 3-i+line*4
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
