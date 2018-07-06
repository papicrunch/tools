def setTakeDriver(node):

	n = node
	sNoTake = """$IMAGES/fx/render/`chs("asset")`/`chs("version")`/`chs("asset")`_`chs("version")`"""
	sTake = """$IMAGES/fx/render/`chs("asset")`/`chs("version")`/`chs("asset")`_`chs("take")`_`chs("version")`"""
	sNoTakeIfds = """$JOB/ifds/`chs("asset")`/`chs("version")`/`chs("asset")`_`chs("version")`"""
	sTakeIfds = """$JOB/ifds/`chs("asset")`/`chs("version")`/`chs("asset")`_`chs("take")`_`chs("version")`"""
	

	if(n.parm('useTake').eval()):
		n.parm("outImages").set(sTake)
		n.parm("outIfds").set(sTakeIfds)

	else:
		n.parm("outImages").set(sNoTake)
		n.parm("outIfds").set(sNoTakeIfds)

def setTakeArnold(node):

	n = node
	sNoTake = """$IMAGES/fx/render/`chs("asset")`/`chs("version")`/`chs("asset")`_`chs("version")`"""
	sTake = """$IMAGES/fx/render/`chs("asset")`/`chs("version")`/`chs("asset")`_`chs("take")`_`chs("version")`"""
	sNoTakeIfds = """$JOB/ass/`chs("asset")`/`chs("version")`/`chs("asset")`_`chs("version")`"""
	sTakeIfds = """$JOB/ass/`chs("asset")`/`chs("version")`/`chs("asset")`_`chs("take")`_`chs("version")`"""
	

	if(n.parm('useTake').eval()):
		n.parm("outImages").set(sTake)
		n.parm("outAss").set(sTakeIfds)

	else:
		n.parm("outImages").set(sNoTake)
		n.parm("outAss").set(sNoTakeIfds)