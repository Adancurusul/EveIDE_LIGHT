import time
import os
print(int(time.time()))

print(int(os.stat("D:\\codes\\EveIDE_Plus\\EveIDE_Plus\\source\\t_workspace\\cfgPorjectList.evecfg").st_mtime))