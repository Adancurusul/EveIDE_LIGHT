"""
    	*************************** 
    	--------EveIDE_LIGHT-------- 
 	 Author: Adancurusul
 	 Date: 2021-07-30 08:45:47
 	 LastEditors: Adancurusul
 	 LastEditTime: 2021-07-31 14:09:42
 	 Github: https://github.com/Adancurusul
 	 Email: adancurusul@gmail.com

    	***************************
    """
import json
import logging
import os
class cfgRead():
    def __init__(self,cfgPath): 
        self.cfgPath = cfgPath

    def check_path(self):
        if os.path.exists(self.cfgPath):
            return 1
        else:
            logging.debug("Path is not exists:"+self.cfgPath)
            return 0

    def get_dict(self):
        with open(self.cfgPath,"r",encoding="utf-8") as readFile:
            strNow = readFile.read()
            logging.debug("loading json:"+strNow+"from file :"+self.cfgPath)
            dictNow = json.loads(strNow)
            logging.debug("Successfully read Dict: "+str(dictNow)+"from :"+ self.cfgPath)
            return dictNow
    def write_dict(self,dictNow):
        with open(self.cfgPath,"w",encoding="utf-8") as writeFile:
            json.dump(dictNow,writeFile,indent=4)#format
            logging.debug("Successfully store Dict: "+str(dictNow)+"into :"+ self.cfgPath)


