def HMTC_createSceneBtn():
    import datetime
    import os
    n = hou.pwd()
    nConnect = n.inputs()
    count = 0
    sNukeFile = ""
    sPath = hou.expandString('$JOB')
    sHipName = hou.expandString('$HIPNAME')
    sSceneName = datetime.datetime.now().strftime("%Y_%m_%d_at_%Hh%M") + ".nk"
    sPathNukeFile = sPath + "/scenes/compo/precomp/fx_render/"


    ################ loop children
    for i in nConnect:
        sStartFrame = str(int(nConnect[count].evalParm('f1')))
        sEndFrame = str(int(nConnect[count].evalParm('f2')))
        sAsset = nConnect[count].evalParm('asset')
        sVersion = nConnect[count].evalParm('version')
        sOutPic = nConnect[count].evalParm('vm_picture')
        sTemplateRead = ""
        sYpos = "0"
        sXpos = str(count*150)
        ########################## useTake parm ######################
        try :
            iTake = nConnect[count].evalParm('useTake')
            if (iTake == True):
                    sTake = nConnect[count].evalParm('take') + "_"
            else:
                    sTake = ""
        except:
            sTake = ""

        sOutPic = HMTC_houPath2NukePath(sOutPic)
        sTake = nConnect[count].evalParm('take') + "_" ########### TAKE OVER FOR THE MOMENT
        sName = sAsset + "_"+ sTake + sVersion
        sTemplateRead += HMTC_nukeReadTemplate(sOutPic,sStartFrame,sEndFrame,sName,sXpos,sYpos)
        sNukeFile += sTemplateRead

        count += 1

    if not os.path.exists(sPathNukeFile):
        os.makedirs(sPathNukeFile)
        
    n.parm("path").set(sPathNukeFile)
    sPathNukeFile += sSceneName
    f = open(sPathNukeFile ,"w")
    f.write(sNukeFile)
    f.close()





def HMTC_houPath2NukePath(sHouPath):
        aOutPic = sHouPath.rsplit('.',2)
        sHoudiniPad = aOutPic[-2]
        sNukePad = ""

        for i in sHoudiniPad:
                sNukePad += "#"

        aOutPic[-2] = sNukePad
        sOutPic = ".".join(aOutPic)
        return sOutPic

def HMTC_nukeReadTemplate(imagePath,firstFrame,lastFrame,name,xpos,ypos):
    sTemplateRead = "Read {\n" + " inputs 0" + "\n"
    sTemplateRead += " file " + imagePath + "\n"
    sTemplateRead += " first " + firstFrame + "\n"
    sTemplateRead += " last " + lastFrame + "\n"
    sTemplateRead += " origfirst " + firstFrame + "\n"
    sTemplateRead += " origlast " + lastFrame + "\n"
    sTemplateRead += " origset true" + "\n"
    sTemplateRead += " name " + name + "\n"
    sTemplateRead += " xpos " + xpos + "\n"
    sTemplateRead += " ypos " + ypos + "\n" + "}" + "\n"
    return sTemplateRead