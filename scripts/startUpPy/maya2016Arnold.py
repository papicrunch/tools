import os
import subprocess
from os.path import expanduser

home = expanduser("~")

arnoldPath = "F:\_arnold\mtoa"
os.environ["MAYA_MODULE_PATH"] = arnoldPath

mayaExe = os.environ["ProgramFiles"]+"/autodesk/maya2016/bin/maya.exe"
subprocess.call([mayaExe])

