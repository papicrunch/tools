import hou

print " hello Houdini Power User\n ----------------\n current Houdini Build must be\n 15.5.607\n"


hou.node("/obj").createNode("setupShot", "setup_Shot")
mantra = hou.node("/out").createNode("paMantra", "default")



###################




nNode = hou.node("/obj").children()
sType = ""
iSetupShot = 0
nNodeCreate = []

#### loop /obj to find node Type name match
for object in hou.node("/obj").children():
    sType = object.type().name()
    print sType
    if sType == "papicrunch::setupShot::0.1":
        iSetupShot = 1
if iSetupShot == 0:
    nodeCreate = hou.node("/obj").createNode("setupShot", "setupShot")
    nNodeCreate.append(nodeCreate) 
    
nNodeCreate[0].setColor(hou.Color((0.450,1,0)))