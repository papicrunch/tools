node = hou.pwd()
geo = node.geometry()
geo.addAttrib(hou.attribType.Global, "allInstance2", "")
from cStringIO import StringIO
file_str = StringIO()

for point in geo.points():
    tmp_list = point.attribValue("declareProc")
    file_str.write(tmp_list)
    
value = file_str.getvalue()
geo.setGlobalAttribValue("allInstance2", value)
file_str.close()