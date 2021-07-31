"""
    	*************************** 
    	--------EveIDE_LIGHT-------- 
 	 Author: Adancurusul
 	 Date: 2021-07-19 18:34:30
 	 LastEditors: Adancurusul
 	 LastEditTime: 2021-07-31 14:09:45
 	 Github: https://github.com/Adancurusul
 	 Email: adancurusul@gmail.com

    	***************************
    """
# -*- coding: utf-8 -*-

import os 
import sys
# import codecs
import chardet
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
        print("0000000000000000000000000000000000000000000000")
        print(type(f))

        source_encoding = chardet.detect(content_bytes).get('encoding')
        print(chardet.detect(content_bytes))

        with open(filename, 'r', encoding=source_encoding) as f:
            content_str = f.read()
        print(type(content_str))
        print("1111111111111111111111111111111111111111111111")
        print(filename)
        #    print(content_str)

        with open(filename, 'w', encoding=out_enc) as f:
            f.write(content_str)

        with open(filename, 'rb') as f:
            content_bb = f.read()
        print(chardet.detect(content_bb))

        statinfo = os.stat(filename)
        print(statinfo)

    except IOError as err:
        print("I/O error:{0}".format(err))


def explore(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            if os.path.splitext(file)[1] == '.txt':
                print(file)
                path = os.path.join(root, file)
                convert(path)


def main():
    #  explore(os.getcwd())
    explore("C:/Users/y_smile/Desktop/coding_2_utf8")


#    explore('C:\\Users\\y_smile\\Desktop\\coding_2_utf8')

if __name__ == "__main__":
    main()
