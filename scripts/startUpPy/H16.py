import os
import subprocess
from os.path import expanduser

home = expanduser("~")

rawPath = r"X:\\_MTC_CONFIG\\_CONFIG_HOUDINI_"
absPath = r"\\config.int.mtc.fr\CONFIG\_MTC_CONFIG\_CONFIG_HOUDINI"

mtcPath = rawPath + r"\\HMTCConfig%s" %("\\")
houdiniPath = ";&;" + mtcPath

os.environ["HOUDINI_PATH"] = houdiniPath 


HoudiniExe = "C:\Program Files/Side Effects Software/Houdini 16.0.736/bin/hmaster.exe"
print HoudiniExe
subprocess.call([HoudiniExe])
