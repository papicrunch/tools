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


# HOUDINI_PATH     &;\\config.int.mtc.fr\CONFIG\_MTC_CONFIG\_CONFIG_HOUDINI_\HMTCConfig\
houdiniPath = r"&;\\config.int.mtc.fr\CONFIG\_MTC_CONFIG\_CONFIG_HOUDINIaaaaa_\HMTCConfig%s" %("\\")
##houdiniPath =""
arnoldPath = r"\\config.int.mtc.fr\CONFIG\_MTC_CONFIG\_CONFIG_HOUDINI_\htoa\Htoa_2.2.0\htoa-2.2.0_r9912855_houdini-16.0.705%s" %("\\")
userName = os.environ['USERNAME']
allEnv  = os.environ
userProfile = os.environ['USERPROFILE']
homePath = os.environ['HOMEPATH']

os.environ["HOUDINI_PATH"] = houdiniPath

print "loading Houdini with Arnold"
print houdiniPath
print arnoldPath

HoudiniExe = os.environ["ProgramFiles"]+"/Side Effects Software/Houdini 16.0.705/bin/hmaster.exe"
subprocess.call([HoudiniExe])
