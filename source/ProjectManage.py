import os
import sys
import logging
#t_dir = "C:\Users\User\Documents\GitHub\EveIDE_Plus\source\\t_exCpro"
languageFileSuportList = [".c",".v",".sv",".S"]
outputFileSupportList = [".bin",".mif",".coe",".out"]
t_dirFilesDict = {}
t_fileDict = {"fullPath":"","name":"","type":"","fileSuffix":"","homePath":"","fatherName":""}
t_dirDict = {"fullPath":"","name":"","type":"","files":[],"homePath":"","fatherName":""}

import os

path = "C:\\Users\\User\\Documents\\GitHub\\EveIDE_Plus\\source\\t_exCpro"

class ProjectManage():
    def __init__(self,projectPath):
        self.projectPath = projectPath
    def get_project_tree_dict(self):
        files = os.listdir(path)
    def get_project_dict(self):
        rootName = os.path.basename(self.projectPath)

        rootTreeList = []
        for home,dirs,files in os.walk(self.projectPath) :
            treeDict = {"node":os.path.basename(home),"dirs":[],"files":[],"ifOpen":0}
            for eachDir in dirs:
                dirDictNow = {}
                dirDictNow["fullPath"] = self.relative_path(os.path.join(home,eachDir))
                dirDictNow["name"] = eachDir
                #dirDictNow["homePath"] = self.relative_path(home)
                #dirDictNow["fatherName"] = os.path.basename(home)
                treeDict["dirs"].append(dirDictNow)
                dirDictNow["child"] = []
            for eachFile in files :
                fileDictNow = {}
                fileDictNow["fullPath"] = self.relative_path(os.path.join(home,eachFile))
                fileDictNow["name"] = eachFile
                fileDictNow["type"] = "file"
                fileDictNow["fileSuffix"] = self.file_suffix(eachFile)
                treeDict["files"].append(fileDictNow)
                #fileDictNow["fatherName"] = os.path.basename(home)
                #fileDictNow["homePath"] = self.relative_path(home)
            rootTreeList.append(treeDict)
            #logging.debug(treeDict)


        for eachDict in reversed(rootTreeList):
            nodeNow = eachDict.get("node","")
            for searchDict in rootTreeList :
                searchNodeList = searchDict.get("dirs",[])
                for searchNode in searchNodeList :
                    childName = searchNode.get("name","")
                    if nodeNow == childName :
                        searchNode["child"].append(eachDict)
                        del rootTreeList[-1]
                        #break
        logging.debug(rootTreeList)
        logging.debug(rootTreeList[0])
        logging.debug(len(rootTreeList))
    #@property
    def relative_path(self,pathNow):
        return os.path.relpath(pathNow)
    def absolute_path(self,pathNow):
        return os.path.abspath(pathNow)
    def file_suffix(self,fileName):
        return fileName.split(".")[-1]
    @property
    def file_list(self):
        fileList = []
        for home,dirs,files in os.walk(self.projectPath):
            for eachFile in files:
                fileDictNow = {}
                fileDictNow["fullPath"] = self.relative_path(os.path.join(home, eachFile))
                fileDictNow["name"] = eachFile
                fileDictNow["type"] = "file"
                fileDictNow["fileSuffix"] = self.file_suffix(eachFile)
                #treeDict["files"].append(fileDictNow)
                fileList.append(fileDictNow)

        return fileList
    @property
    def porject_dict(self) :
        rootName = os.path.basename(self.projectPath)

        rootTreeList = []
        for home, dirs, files in os.walk(self.projectPath):

            treeDict = {"node": os.path.basename(home), "dirs": [], "files": [], "ifOpen": 0}
            for eachDir in dirs:
                dirDictNow = {}
                dirDictNow["fullPath"] = self.relative_path(os.path.join(home, eachDir))
                dirDictNow["name"] = eachDir
                # dirDictNow["homePath"] = self.relative_path(home)
                # dirDictNow["fatherName"] = os.path.basename(home)
                treeDict["dirs"].append(dirDictNow)
                dirDictNow["child"] = []
            for eachFile in files:
                fileDictNow = {}
                fileDictNow["fullPath"] = self.relative_path(os.path.join(home, eachFile))
                fileDictNow["name"] = eachFile
                fileDictNow["type"] = "file"
                fileDictNow["fileSuffix"] = self.file_suffix(eachFile)
                treeDict["files"].append(fileDictNow)

                # fileDictNow["fatherName"] = os.path.basename(home)
                # fileDictNow["homePath"] = self.relative_path(home)
            rootTreeList.append(treeDict)

            # logging.debug(treeDict)
        #rootTreeList.reverse()
        print(rootTreeList)
        for eachDict in reversed(rootTreeList):
            nodeNow = eachDict.get("node", "")
            for searchDictIndex in range(len(rootTreeList)):
                searchNodeList = rootTreeList[searchDictIndex].get("dirs", None)
                #print(searchNodeList)
                if searchNodeList:
                    for searchNodeIndex in range(len(rootTreeList[searchDictIndex]["dirs"])):
                        #print(rootTreeList[searchDictIndex]["dirs"][searchNodeIndex])
                        print(searchNodeIndex)
                        childName = rootTreeList[searchDictIndex]["dirs"][searchNodeIndex].get("name", None)
                        if childName:
                            if childName == nodeNow:
                                rootTreeList[searchDictIndex]["dirs"][searchNodeIndex]["child"] = eachDict

                                #del rootTreeList[-1]




        '''for eachDict in reversed(rootTreeList):
            nodeNow = eachDict.get("node", "")
            for searchDict in rootTreeList:
                searchNodeList = searchDict.get("dirs", [])
                for searchNode in searchNodeList:
                    childName = searchNode.get("name", "")
                    if nodeNow == childName:
                        print(eachDict)
                        searchNode["child"] = eachDict
                        del rootTreeList[-1]'''
        logging.debug("*"*30)
        logging.debug(self.projectPath)
        logging.debug(rootTreeList)
        logging.debug("*"*30)
        if not len(rootTreeList)  == 0:
            logging.debug("*" * 80)
            return rootTreeList[0]
        else:
            return {}


def classT():
    c = ProjectManage(path)
    d = c.porject_dict
    logging.debug(d)

def get_filelist(dir):
    Filelist = []
    dirList = []
    a = os.walk(path)
    logging.debug(a)
    logging.debug("*"*20)
    for home, dirs, files in os.walk(path):
        logging.debug("home"+home)
        logging.debug("dirs" + str(dirs))
        logging.debug("files" + str(files))

        '''for filename in files:
            # 文件名列表，包含完整路径

            Filelist.append(os.path.join(home, filename))

            # # 文件名列表，只包含文件名

            # Filelist.append( filename)
        for dirs in files:
            logging.debug(dirs)
            dirList.append(os.path.join(home, dirs))'''


    #return Filelist,dirList

def get_suffix():
    d = "C:\\Users\\User\\Documents\\GitHub\\EveIDE_Plus\\source\\t_exCpro"
    #"C:\\Users\\User\\Documents\\GitHub\\EveIDE_Plus\\source\\t_workspace\\UR408_Core-master"
    a = os.path.split(d)
    b = os.path.basename(d)
    c = b.split(".")
    #c = os.listdir(d)

    logging.debug(a)
if __name__ == "__main__":
    #Filelist = get_suffix(dir)
    #classT()
    logging.getLogger().setLevel(logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S', )
    q = "C:\\Users\\User\\Documents\\GitHub\\EveIDE_Plus\\source\\t_workspace\\UR408_Core-master"
    a ="C:\\Users\\User\\Documents\\GitHub\\KC_LS1u_SoC"
    k = ProjectManage(a)
    print(k.porject_dict)
    #logging.debug(Filelist)
'''    logging.debug(len(Filelist))

    for file in Filelist:
        logging.debug(file)'''
