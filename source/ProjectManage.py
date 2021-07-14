import os
import sys

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
            #print(treeDict)


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
        print(rootTreeList)
        print(rootTreeList[0])
        print(len(rootTreeList))
    #@property
    def relative_path(self,pathNow):
        return os.path.relpath(pathNow)
    def absolute_path(self,pathNow):
        return os.path.abspath(pathNow)
    def file_suffix(self,fileName):
        return fileName.split(".")[-1]
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
            # print(treeDict)

        for eachDict in reversed(rootTreeList):
            nodeNow = eachDict.get("node", "")
            for searchDict in rootTreeList:
                searchNodeList = searchDict.get("dirs", [])
                for searchNode in searchNodeList:
                    childName = searchNode.get("name", "")
                    if nodeNow == childName:
                        searchNode["child"] = eachDict
                        del rootTreeList[-1]
        return rootTreeList[0]


def classT():
    c = ProjectManage(path)
    d = c.porject_dict
    print(d)

def get_filelist(dir):
    Filelist = []
    dirList = []
    a = os.walk(path)
    print(a)
    print("*"*20)
    for home, dirs, files in os.walk(path):
        print("home"+home)
        print("dirs" + str(dirs))
        print("files" + str(files))

        '''for filename in files:
            # 文件名列表，包含完整路径

            Filelist.append(os.path.join(home, filename))

            # # 文件名列表，只包含文件名

            # Filelist.append( filename)
        for dirs in files:
            print(dirs)
            dirList.append(os.path.join(home, dirs))'''


    #return Filelist,dirList

def get_suffix(dir):
    d = "C:\\Users\\User\\Documents\\GitHub\\EveIDE_Plus\\source\\t_exCpro"
    a = os.path.splitext(d)
    b = os.path.basename(d)
    c = b.split(".")
    c = os.listdir(d)

    print(a)
if __name__ == "__main__":
    #Filelist = get_suffix(dir)
    classT()
    #print(Filelist)
'''    print(len(Filelist))

    for file in Filelist:
        print(file)'''
