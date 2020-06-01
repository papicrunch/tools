import hou

def get():
    n = hou.pwd()
    entity = hou.getenv("ENTITY")
    project = hou.getenv("PROJECT")
    task = hou.getenv("TASK")
    category = hou.getenv("JOB")
    category = category.split("/")[-2]
    
    n.parm('entity').set(entity)   
    n.parm('project').set(project)
    n.parm('task').set(task)
    n.parm('category').set(category)
    
def setnet():
    n = hou.pwd()
    path = n.evalParm('network')

    project = n.evalParm('project')
    category = n.evalParm('category')
    entity = n.evalParm('entity')
    task = n.evalParm('task')
    hipname = hou.getenv("HIPNAME")
    
    assets = path + project + "/work/assets"
    job =  path + project + "/work/" + category + "/" + entity
    cache = job + "/caches"
    images = job + "/images"
    images_writes = images + "/" + task + "/" + hipname
    
    hou.putenv('ASSETS', assets)
    hou.putenv('JOB', job)
    hou.putenv('CACHE', cache)
    hou.putenv('IMAGES', images)
    hou.putenv('IMAGES_WRITES', images_writes)
    
    print "---- NETWORK ----\n"
    print "ASSETS : " + hou.getenv("ASSETS") + "\n"
    print "JOB : " + hou.getenv("JOB") + "\n"
    print "CACHE : " + hou.getenv("CACHE") + "\n"
    print "IMAGES : " + hou.getenv("IMAGES") + "\n"
    print "IMAGES_WRITE : " + hou.getenv("IMAGES_WRITES") + "\n"
    print "---- NETWORK ----\n"
    
    
def setlocal():
    n = hou.pwd()
    path = n.evalParm('local')

    project = n.evalParm('project')
    category = n.evalParm('category')
    entity = n.evalParm('entity')
    task = n.evalParm('task')
    hipname = hou.getenv("HIPNAME")
    
    assets = path + project + "/work/assets"
    job = path + project + "/work/" + category + "/" + entity
    cache = job + "/caches"
    images = job + "/images"
    images_writes = images + "/" + task + "/" + hipname
    
    hou.putenv('ASSETS', assets)
    hou.putenv('JOB', job)
    hou.putenv('CACHE', cache)
    hou.putenv('IMAGES', images)
    hou.putenv('IMAGES_WRITES', images_writes)
    
    print "---- LOCAL ----\n"
    print "ASSETS : " + hou.getenv("ASSETS") + "\n"
    print "JOB : " + hou.getenv("JOB") + "\n"
    print "CACHE : " + hou.getenv("CACHE") + "\n"
    print "IMAGES : " + hou.getenv("IMAGES") + "\n"
    print "IMAGES_WRITE : " + hou.getenv("IMAGES_WRITES") + "\n"
    print "---- LOCAL ----\n"