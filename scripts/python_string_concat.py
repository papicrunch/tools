node = hou.pwd()
geo = node.geometry()

from cStringIO import StringIO
file_str = StringIO()

##geo.addAttrib(hou.attribType.Global, "allInstance2", "")
loc = "F:/test.ass"

for point in geo.points():
    tmp_list = point.attribValue("declareInstance")
    file_str.write(tmp_list)

f=open(loc, "w")
f.write(file_str.getvalue())
f.close()

## value = file_str.getvalue()
##geo.setGlobalAttribValue("allInstance2", value)


file_str.close()