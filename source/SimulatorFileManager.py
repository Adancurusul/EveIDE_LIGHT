import os
import re
from ProjectManage import ProjectManage
class SimulatorFileManager():
    def __init__(self, projectPath):
        self.projectPath = projectPath
        #self.testBenchPath = testBenchPath
        self.fileList = []
        self.simFiles = []
        self.modules = []
        self.simulateFileDict = self.scan_files()
        print(self.simulateFileDict)
    def rmComments(self,text):
        singLineComments = re.compile(r'//(.*)', re.MULTILINE)
        multiLineComments = re.compile(r'/\*(.*)\*/', re.DOTALL)
        text = singLineComments.sub('', text)
        text = multiLineComments.sub('', text)
        return text

    def get_module_name(self, fileDict):
        fullPath = fileDict.get("fullPath", None)
        fileDict["module"] = []
        fileDict["submodule"] = []
        if fullPath is not None:
            lineList = []
            # print(fullPath)

            with open(fullPath, "r",encoding="utf-8") as rFile:
                fileText = self.rmComments(rFile.read()).replace("\n", " ")
                # fileText = rmComments(rFile.read()).replace("\t", " ")
                fileList = re.split(";|endmodule|end", fileText)
                for each in fileList:
                    eachStr = each.lstrip()
                    # print(eachStr)
                    tp = r"(module)(\s+)(\w+)"
                    # patternStr = r"(\w+|_.+)(\s+|\t)(\w+|_.+)(\s+|\t|\s?)\("
                    pattern = re.compile(tp)
                    match = pattern.search(eachStr)
                    if match:
                        ms = match.group(3)
                        mdict = {"moduleName": ms, "submoduleName": []}
                        # print(ms)
                        fileDict["module"].append(mdict)
                        self.modules.append(ms)

            # print(fileDict.get("submodule",""))
        return fileDict


    def scan_files(self):
        import logging

        manager = ProjectManage(self.projectPath)
        self.fileList = manager.file_list
        verilogList = []

        """
        这里
        没法给dict添加
        gkd
        先睡觉

        """
        for eachFile in self.fileList:
            if eachFile.get("fileSuffix", "") == "v":
                # eachFile["moduleName"] = eachFile.get("name","").split(".")[0]
                eachFile = self.get_module_name(eachFile)
                # eachFile = self.get_submodule(eachFile)
                # verilogList.append(eachFile)
                verilogList.append(eachFile)
        for index in range(len(verilogList)):
            eachFileDict = verilogList[index]
            # for eachFileDict in verilogList:
            verilogList[index] = self.get_submodule(eachFileDict)
            logging.debug(eachFile.get("submodule", None))
            # print(eachFile.get("submodule",None))
            # verilogList.append(eachFileDict)
        #print(verilogList)
        return verilogList
    def get_submodule(self, fileDict):
        fullPath = fileDict.get("fullPath", None)
        # print(fullPath)
        # fileDict["module"] = []
        fileDict["submodule"] = []
        if fullPath is not None:
            # if fullPath == "..\\..\\..\\Tencent Files\\1016867898\\FileRecv\\LPCE20210501\\LPCE\\RTL\\LPCE_tx.v":
            with open(fullPath, "r",encoding="utf-8") as rFile:
                fileText = self.rmComments(rFile.read())
                # splitStr = ""
                fileList = re.split(r"module\s+\w+", fileText)
                # print(fullPath)

                # print(fileList)
                for index in range(1, len(fileList)):  # 例化一定是在module里面
                    # print(index)
                    # print(len(fileList))
                    # print(fileList[index])
                    #print(fullPath)
                    eachStr = fileList[index]
                    # print(eachStr)
                    for each in self.modules:
                        # tp = r"(" + each + ")([ \t\v\r\f]+|\()?"
                        tp = r"(" + each + ")(?!\w)"
                        # tt = r"(" + each + ")\s+\w+"
                        pattern = re.compile(tp)
                        match = pattern.search(eachStr)
                        # print(match)
                        if match:
                            #print(match)
                            if not fileDict["module"][index - 1]["moduleName"] == each:
                                fileDict["module"][index - 1]["submoduleName"].append(each)
                                fileDict["submodule"].append(each)

                # print(self.modules)

        #print(fileDict)
        return fileDict

    def get_file_of_module(self, moduleName):
        moduleFileList = []
        for eachFile in self.fileList:
            if eachFile.get("moduleName", "") == moduleName:
                moduleFileList.append(eachFile)
        for eachModule in moduleFileList:
            if eachModule not in self.simFiles:
                self.simFiles.append(eachModule)
        return moduleFileList
        # print(fileList)


if __name__ == '__main__':
    # initDark()

    c = SimulatorFileManager("C:\\Users\\User\\Documents\\Tencent Files\\1016867898\\FileRecv\\LPCE20210501\\LPCE")

