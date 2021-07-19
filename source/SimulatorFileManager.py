import os
import re
import logging
from ProjectManage import ProjectManage
from eve_module.ChangeEncoding import ChangeEncoding
class SimulatorFileManager():
    def __init__(self, projectPath):
        self.projectPath = projectPath
        #self.testBenchPath = testBenchPath
        self.fileList = []
        self.simFiles = []
        self.modules = []
        self.ChangeEncoding = ChangeEncoding()
        self.simulateFileDict = self.scan_files()
        print(self.simulateFileDict)
        #print(self.simulateFileDict)
        self.includeFileList = self.get_includes()
        #print(self.includeFileList)
        logging.debug(self.simulateFileDict)
    def get_includes(self):
        incList = []
        for each in self.simulateFileDict:
            pathnameNow = os.path.dirname(each.get("fullPath",""))
            #print(pathnameNow)
            if not pathnameNow  in incList:
                incList.append(pathnameNow)
        return incList
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
            # logging.debug(fullPath)

            with open(fullPath, "r",encoding="utf-8") as rFile:
                print(fullPath)
                fileText = rFile.read()
                #fileText = self.rmComments(rFile.read())#.replace("\n", " ")
                #print(fileText)
                # logging.debug(eachStr)
                tp = r"(module)(\s+)(\w+)"
                # patternStr = r"(\w+|_.+)(\s+|\t)(\w+|_.+)(\s+|\t|\s?)\("
                pattern = re.compile(tp)
                match = pattern.search(fileText)
                if match:
                    ms = match.group(3)
                    mdict = {"moduleName": ms, "submoduleName": []}
                    print("searchModule:",ms)
                    fileDict["module"].append(mdict)
                    self.modules.append(ms)
                # fileText = rmComments(rFile.read()).replace("\t", " ")
                '''fileList = re.split(";|endmodule|end", fileText)
                for each in fileList:
                    eachStr = each.lstrip()
                    # logging.debug(eachStr)
                    tp = r"(module)(\s+)(\w+)"
                    # patternStr = r"(\w+|_.+)(\s+|\t)(\w+|_.+)(\s+|\t|\s?)\("
                    pattern = re.compile(tp)
                    match = pattern.search(eachStr)
                    if match:
                        ms = match.group(3)
                        mdict = {"moduleName": ms, "submoduleName": []}
                        print(ms)
                        fileDict["module"].append(mdict)
                        self.modules.append(ms)'''

            # logging.debug(fileDict.get("submodule",""))
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
        befVerilogList = []
        for eachFile in self.fileList:
            if (eachFile.get("fileSuffix", "") == "v") or (eachFile.get("fileSuffix", "") == "sv"):
                befVerilogList.append(eachFile)
        for eachFile in befVerilogList:
            self.ChangeEncoding.convert(filePath=eachFile.get("fullPath"))
        for eachFile in self.fileList:
            if (eachFile.get("fileSuffix", "") == "v") or (eachFile.get("fileSuffix", "") == "sv"):
                # eachFile["moduleName"] = eachFile.get("name","").split(".")[0]
                eachFile = self.get_module_name(eachFile)
                # eachFile = self.get_submodule(eachFile)
                # verilogList.append(eachFile)
                verilogList.append(eachFile)
                print(verilogList)

        for index in range(len(verilogList)):
            eachFileDict = verilogList[index]
            # for eachFileDict in verilogList:
            verilogList[index] = self.get_submodule(eachFileDict,verilogList)
            logging.debug(eachFile.get("submodule", None))
            # logging.debug(eachFile.get("submodule",None))
            # verilogList.append(eachFileDict)
        #logging.debug(verilogList)
        return verilogList

    def get_submodule(self, fileDict,verilogList):
        fullPath = fileDict.get("fullPath", None)
        # logging.debug(fullPath)
        # fileDict["module"] = []
        fileDict["submodule"] = []
        if fullPath is not None:
            # if fullPath == "..\\..\\..\\Tencent Files\\1016867898\\FileRecv\\LPCE20210501\\LPCE\\RTL\\LPCE_tx.v":
            with open(fullPath, "r",encoding="utf-8") as rFile:
                fileText = rFile.read()
                #print(fileText)
                # splitStr = ""
                fileList = re.split(r"module\s+\w+", fileText)
                for index in range(1, len(fileList)):  # 例化一定是在module里面
                    # logging.debug(index)
                    # logging.debug(len(fileList))
                    # logging.debug(fileList[index])
                    #logging.debug(fullPath)
                    eachStr = fileList[index]
                    # logging.debug(eachStr)
                    for each in self.modules:
                        # tp = r"(" + each + ")([ \t\v\r\f]+|\()?"
                        tp = r"(" + each + ")(?!\w)"
                        # tt = r"(" + each + ")\s+\w+"
                        pattern = re.compile(tp)
                        match = pattern.search(eachStr)
                        # logging.debug(match)
                        if match:
                            #logging.debug(match)
                            '''
                            
                            有个bug
                            
                            
                            
                            '''
                            print(fileDict["module"])
                            if not fileDict["module"][index - 1]["moduleName"] == each:
                                #得到例化模块名
                                #逆推到该module文件
                                d = {}
                                for eachDict in verilogList:
                                    moduleD = eachDict.get("module",[])
                                    for e in moduleD:
                                        if e.get("moduleName","") == each:
                                            d = eachDict

                                moduleDict = {"name":each,"submoduleFileDict":d}
                                fileDict["module"][index - 1]["submoduleName"].append(moduleDict)
                                fileDict["submodule"].append(each)

                # logging.debug(self.modules)

        #logging.debug(fileDict)
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
        # logging.debug(fileList)


if __name__ == '__main__':
    # initDark()

    c = SimulatorFileManager("C:\\Users\\User\\Documents\\GitHub\\PRV464PRO\\RTL")

