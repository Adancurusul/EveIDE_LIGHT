import re
import os
class GetSimDumpFile():
    def rmComments(self,text):
        singLineComments = re.compile(r'//(.*)', re.MULTILINE)
        multiLineComments = re.compile(r'/\*(.*)\*/', re.DOTALL)
        text = singLineComments.sub('', text)
        text = multiLineComments.sub('', text)
        return text
    def getDumpFile(self,fileName)->str:
        stPath = ""
        with open(fileName, "r", encoding="utf-8") as rFile:
            fileText = self.rmComments(rFile.read())
            tp = r"(\$dumpfile)(.+)[\;]"
            # patternStr = r"(\w+|_.+)(\s+|\t)(\w+|_.+)(\s+|\t|\s?)\("
            pattern = re.compile(tp)
            match = pattern.search(fileText)
            if (match):
                st = match.group(2).replace(" ", "").replace("(", "").replace(")", "").replace("\"", "")
                stPath = os.path.dirname(fileName)+"/"+st
        return stPath