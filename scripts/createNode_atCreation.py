
import hou

###### create node a start
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
else:
	print "OK"
##nNodeCreate[0].setColor(hou.Color((0.450,1,0)))