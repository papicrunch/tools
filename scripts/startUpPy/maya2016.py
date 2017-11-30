import os
import subprocess
from os.path import expanduser

home = expanduser("~")

# arnoldPath = "E:\mayaConfig\ARNOLD"
# presenZPath = "E:\mayaConfig\PRESENZ\Arnold\PresenZ-0.3.2"
# os.environ["MAYA_MODULE_PATH"] = presenZPath + ";" + arnoldPath
scriptPath = "X:\_MTC_CONFIG\_CONFIG_MAYA_DEV\MEL"
modulePath = "X:\_MTC_CONFIG\_CONFIG_MAYA_DEV\MODULES\_MOD_FILES"
configPath = "X:\_MTC_CONFIG\_CONFIG_MAYA_DEV"
os.environ["MAYA_MODULE_PATH"] = modulePath
os.environ["MAYA_SCRIPT_PATH"] = scriptPath
os.environ["MAYA_CONFIG_PATH"] = configPath

userName = os.environ['USERNAME']
allEnv  = os.environ
userProfile = os.environ['USERPROFILE']
homePath = os.environ['HOMEPATH']

print "loading maya2016"
#print allEnv

mayaExe = os.environ["ProgramFiles"]+"/autodesk/maya2016/bin/maya.exe"
subprocess.call([mayaExe])
