import os
import subprocess
from os.path import expanduser

home = expanduser("~")

## PATH = "$PATH;C:/path/to/htoa/htoa-1.0.0_r990_houdini-13.0.509_windows_vc-11/scripts/bin"
## HOUDINI_PATH = "C:/path/to/htoa/htoa-1.0.0_r990_houdini-13.0.509_windows_vc-11;&"
mtcPath = r"\\config.int.mtc.fr\CONFIG\_MTC_CONFIG\_CONFIG_HOUDINIaaaaa_\HMTCConfig%s" %("\\")
arnoldPath = r"F:\_arnold\htoa\htoa-2.2.0_r9912855_houdini-16.0.705%s" %("\\")
localPath = r"$PATH;"+ arnoldPath + "\\scripts\\bin"
houdiniPath = arnoldPath + ";&"


os.environ["PATH"] = localPath
os.environ["HOUDINI_PATH"] = houdiniPath + ""

print "loading Houdini with Arnold"
print houdiniPath
#print arnoldPath
print localPath

HoudiniExe = os.environ["ProgramFiles"]+"/Side Effects Software/Houdini 16.0.705/bin/hmaster.exe"
subprocess.call([HoudiniExe])
