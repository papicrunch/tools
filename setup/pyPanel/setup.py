import os
import sys

from PySide2 import QtCore, QtWidgets, QtUiTools

def setupButtonAction():
    nSelf = hou.pwd()
    sHipFile = hou.expandString('$HIPFILE')
    sHipFolderSplit = sHipFile.rsplit("/",1)
    iNumFolder = len(sHipFile.split("/"))
    count = 2
    
    while (count < iNumFolder):
        sHipFolderSplit = sHipFolderSplit[0].rsplit("/",1)
        
        if (sHipFolderSplit[1] == "scenes"):
            count = iNumFolder
            hou.putenv("JOB",sHipFolderSplit[0])
            
            # lImage
            lImages = sHipFolderSplit[0].split("/")
            del lImages[2:4]
            lImages[0] = "W:"
            lImages[1] = lImages[1] + "_I"
            sImages = '/'.join(lImages) + "/images"
            
            
            # lCache
            lCache = sHipFolderSplit[0].split("/")
            del lCache[2:4]
            lCache[0] = "U:"
            lCache[1] = lCache[1] + "_K"
            sCache = '/'.join(lCache) + "/cache"              
                
            #set env
            #hou.putenv("IMAGES",sImages)
            #hou.putenv("CACHE",sCache)
            hou.hscript('setenv IMAGES=' + sImages)
            hou.hscript('setenv CACHE=' + sCache)
        
        count += 1
    


def createInterface():
    global MainWidget
    
    ui_file_path = "P:/Alex/test.ui"
    loader = QtUiTools.QUiLoader()
    ui_file = QtCore.QFile(ui_file_path)
    ui_file.open(QtCore.QFile.ReadOnly)
    MainWidget = loader.load(ui_file)
    
    layout = MainWidget.layout()
    
    setupBtn = MainWidget.findChild(QtWidgets.QPushButton,"setupButton")
    setupBtn.clicked.connect(setupButtonAction)
    
    jobLbl = MainWidget.findChild(QtWidgets.QLabel,"jobPath")
    jobLbl.setText(hou.getenv("JOB"))
    
    imagesLbl = MainWidget.findChild(QtWidgets.QLabel,"imagesPath")
    imagesLbl.setText(hou.getenv("IMAGES"))
    
    cacheLbl = MainWidget.findChild(QtWidgets.QLabel,"cachePath")
    cacheLbl.setText(hou.getenv("CACHE"))

    return MainWidget

