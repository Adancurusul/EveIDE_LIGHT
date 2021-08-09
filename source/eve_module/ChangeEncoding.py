"""
    	*************************** 
    	--------EveIDE_LIGHT-------- 
 	 Author: Adancurusul
 	 Date: 2021-07-19 18:34:30
 	 LastEditors: Adancurusul
 	 LastEditTime: 2021-08-02 14:27:31
 	 Github: https://github.com/Adancurusul
 	 Email: adancurusul@gmail.com

    	***************************
    """



import os 
import sys
# import codecs
import chardet
import argparse
class ChangeEncoding():
    #def __init__(self):
    def convert(self,filePath,outEncoding = "utf-8"):
        with open(filePath,"rb") as f :
            bytesNow = f.read()

        sourceEncoding = chardet.detect(bytesNow).get("encoding")
        with open(filePath,"r",encoding=sourceEncoding) as f:
            strNow = f.read()
        with open (filePath,"w",encoding=outEncoding) as f:
            f.write(strNow)
    def getEncoding(self,filePath):
        with open(filePath, "rb") as f:
            bytesNow = f.read()

        sourceEncoding = chardet.detect(bytesNow).get("encoding")
        return sourceEncoding


def convert(filename, out_enc='utf-8'):
    try:
        with open(filename, 'rb') as f:
            content_bytes = f.read()
        print("#"*20)
        print(type(f))

        source_encoding = chardet.detect(content_bytes).get('encoding')
        print(chardet.detect(content_bytes))

        with open(filename, 'r', encoding=source_encoding) as f:
            content_str = f.read()
        print(type(content_str))
        print(filename)
        print("#"*20)


        with open(filename, 'w', encoding=out_enc) as f:
            f.write(content_str)

        with open(filename, 'rb') as f:
            content_bb = f.read()
        print(chardet.detect(content_bb))

        statinfo = os.stat(filename)
        print(statinfo)

    except IOError as err:
        print("I/O error:{0}".format(err))


def explore(dir,suffixList):
    print(dir)
    print(suffixList)
    for root, dirs, files in os.walk(dir):
        for file in files:
            for eachSuffix in suffixList:
                if os.path.splitext(file)[1] == eachSuffix:
                    print("converting : " + file)
                    path = os.path.join(root, file)
                    convert(path)



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Convert specific suffix files in the directory to utf-8 encoding')
    parser.add_argument('path', type=str, help='Folder path')
    parser.add_argument('suffix', type=str, nargs='+', help='file suffix eg: .v .c .txt')
    args = parser.parse_args()
    suffixList = args.suffix
    folderPath = args.path
    explore(folderPath, suffixList)
