##################################
##################################
# si plusieurs asset dans un vrscene
# faire un dict entre geo et shader
#
# dicto pour link unique assetName et geometry
#
# attention le frame offset doit etre un int 
# il est donc multiplié par 100
##################################
##################################

def materialNode(vrmeshFullPathPrim, assetNamePrim, ptId):
        ##########################
        # find node material on matrials.vrscene
        # but we can also search in node.vrscene
        ##########################
        materialPath = os.path.dirname(vrmeshFullPathPrim)
        materialFullPath = "%s/%s_materials.vrscene" %(materialPath, assetNamePrim)
        if(os.path.isfile(materialFullPath)):
                fMaterial = open(materialFullPath,"r")
                first = fMaterial.readline()
                fMaterial.close()
                material = first.split(" ")[1]
                
        else :
                print "PRIM : %s ---> NO MATERIAL FILE FOUND" %(ptId)
                material = "none"

        return material       

        


def nodeTemplate(scatterPath, ptId, scatterSopName, nodeTransform, geoNamePrimNode, nodeMaterial, nodeVisibility, nodeUserAttributes):  
        sNodeDef = "Node Node%s@%s {" %(ptId,scatterSopName)
        sTransform = "  transform=Transform(Matrix(Vector(%s, %s, %s), Vector(%s, %s, %s), Vector(%s, %s, %s)), Vector(%s, %s, %s));"\
                %(nodeTransform[0],nodeTransform[1],nodeTransform[2],nodeTransform[4],nodeTransform[5],nodeTransform[6],\
                nodeTransform[8],nodeTransform[9],nodeTransform[10],nodeTransform[12],nodeTransform[13],nodeTransform[14])
        sGeometry = "  geometry=%s;" %(geoNamePrimNode)
        sMaterial = "  material=%s;" %(nodeMaterial)
        sNsamples = "  nsamples=%s;" %(1)
        sVisibility = "  visible=%s;" %(nodeVisibility)
        sUserAttributes = '  user_attributes="%s=%s";' %(nodeUserAttributes.items()[0][0],nodeUserAttributes.items()[0][1])
        sFullPathNode = scatterPath + scatterSopName+ "_node.vrscene"
        sNode = sNodeDef+ "\n"+ sTransform+ "\n"+ sGeometry+ "\n"+ sMaterial+ "\n"+ sNsamples+ "\n"+sVisibility+ "\n"+ sUserAttributes+ "\n" + "}" + "\n"
        return sNode
        
def geometryTemplate(geoName, vrmeshFullPath, scatterPath, scatterSopName, frameOffsetGeo, uniqueGeoCount):
        sGeomDef = "GeomMeshFile VRayProxyRef_%s {" %( geoName)
        sFile = '  file="%s";' %(vrmeshFullPath)
        sAnimSpeed = "  anim_speed=%s;" %(0)
        sAnimOffset = "  anim_offset=%s;" %(frameOffsetGeo)
        sInstancing = "  instancing=%s;" %(1)
        sFullPathGeometry = scatterPath+ "/" + scatterSopName + "_geometry.vrscene"
        sGeometry = sGeomDef+ "\n"+ sFile+ "\n"+ sAnimSpeed+ "\n"+ sAnimOffset+ "\n"+ sInstancing+ "\n"+ "}"+ "\n"
        return sGeometry

def sceneTemplate(instancePath, asset):
        # only reference existing include for all asset
        sMaterials = '#include "%s/%s_materials.vrscene"\n' %(instancePath,asset)
        sTextures = '#include "%s/%s_textures.vrscene"\n' %(instancePath,asset)
        sBitmaps = '#include "%s/%s_bitmaps.vrscene"\n' %(instancePath,asset)
        sScene = sMaterials+ sTextures+ sBitmaps
        return sScene


import os
import time

def run():
        start_time = time.time()
        node = hou.pwd()
        geo = node.geometry()
        nbPrims = len(geo.prims())
        ptId = 0
        frameOffset = 0
        frameOffsetName = 0.0
        frameOffsetGeo = []
        assetName = []
        vrmeshFullPath = []
        instancePath = []
        geoName = []
        nodeMaterial = []
        nodeTransform = [] # matrix
        sScene = []
        geoVrmesh = {}
        scatterPath = node.evalParm("path")  # need $JOB control
        scatterSopName = "scatterA"      
        nodeVisibility = 1
        nodeUserAttributes = {"customCube":(0,1,2)} # dico
        
        # clear FILE
        sFullPathNode = scatterPath+ "/"+scatterSopName+ "_nodes.vrscene"
        sFullPathGeometry = scatterPath+ "/"+scatterSopName+ "_geometry.vrscene"
        sFullPathScene = scatterPath+ "/" + scatterSopName + ".vrscene"
        fNode = open(sFullPathNode, "w")
        fNode.close()
        fGeometry = open(sFullPathGeometry, "w")
        fGeometry.close()
        fTemplate = open(sFullPathScene, "w")
        fTemplate.close()

        fNode = open(sFullPathNode, "a")

        for prim in geo.prims():

                vrmeshFullPathPrim = prim.intrinsicValue("file")
                frameOffset = prim.intrinsicValue("anim_offset")
                frameOffsetName = int(frameOffset *100)
                # unique assetName link to instancePath
                assetNamePrim = vrmeshFullPathPrim.split("/")[-1].split(".")[0]
                instancePathPrim = os.path.dirname(vrmeshFullPathPrim)
                if assetNamePrim not in assetName: 
                        assetName.append(assetNamePrim)
                        instancePath.append(instancePathPrim)
                
                # unique geometryName link to vrmeshFullPath
                geoNamePrim = "%s@%s_f%s" %(assetNamePrim, scatterSopName,frameOffsetName)
                if geoNamePrim not in geoName:
                        geoName.append(geoNamePrim)
                        vrmeshFullPath.append(vrmeshFullPathPrim)
                        frameOffsetGeo.append(frameOffset)
                geoNamePrimNode = "VRayProxyRef_%s" %(geoNamePrim)


                nodeMaterialPrim = materialNode(vrmeshFullPathPrim,assetNamePrim, ptId)
                # unique node material list
                if nodeMaterialPrim not in nodeMaterial:
                        nodeMaterial.append(nodeMaterialPrim)


                ##########################################################
                # write append Node file
                ##########################################################
                nodeUserAttributes["customCube"] = prim.attribValue("Cd")
                nodeTransform = prim.intrinsicValue("packedfulltransform")
                sNode = nodeTemplate(scatterPath, ptId, scatterSopName, nodeTransform, geoNamePrimNode, nodeMaterialPrim, nodeVisibility, nodeUserAttributes)
                fNode.write(sNode + "\n")

                ptId += 1
                
        fNode.close()

        uniqueGeoCount = 0
        fGeometry = open(sFullPathGeometry, "a")
        for uniqueGeo in geoName:

                ##########################################################
                # write Geo file
                ##########################################################
                sGeometry = geometryTemplate(uniqueGeo, vrmeshFullPath[uniqueGeoCount], scatterPath, scatterSopName, frameOffsetGeo[uniqueGeoCount], uniqueGeoCount)
                # fGeometry = open(sFullPathGeometry, "a")
                fGeometry.write(sGeometry + "\n")

                uniqueGeoCount +=1
        fGeometry.close()

        ##########################################################
        # write Vrscene file
        ##########################################################
        countAsset = 0
        fTemplate = open(sFullPathScene, "a")
        sNodeInclude = '#include "%s/%s_nodes.vrscene"\n' %(scatterPath,scatterSopName)
        sGeometryInclude = '#include "%s/%s_geometry.vrscene"\n' %(scatterPath,scatterSopName)
        for asset in assetName:
                sSceneAsset = sceneTemplate(instancePath[countAsset], asset)
                fTemplate.write(sSceneAsset)
                countAsset += 1

        fTemplate.write(sNodeInclude)
        fTemplate.write(sGeometryInclude)
        fTemplate.close()


        elapsed_time = time.time() - start_time  

        ##################################
        print "-----------> Nodes : %s" %(ptId)
        print "-----------> Geometry : %s" %(uniqueGeoCount)
        print "-----------> Vrmesh : %s" %( len(assetName))
        print "-----------> Material : %s" %( len(nodeMaterial))
        print "-----------> compute Time : %s \n" %( elapsed_time)
        ##################################
        ##################################
        print "------------------------------"
        print "-----------> DONE <-----------"
        print "------------------------------", "\n"
        ##################################        


