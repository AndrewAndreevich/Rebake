import bpy
import os


def ALL(T1,T2):
    TYPE(T1)
    TYPE(T2)
        
def TYPE_GET(T):  
    for obj in bpy.data.objects:
        if T in obj.name:
            return obj    
         
#def TYPE_DELETE(T):
#    for obj in bpy.data.objects:
#        if T in obj.name:
#            bpy.data.objects.remove(obj, do_unlink=True)
#            bpy.ops.object.delete()

def TYPE_DELETE(T):
    obj = TYPE_GET(T)
    if(T in obj.name):
            bpy.data.meshes.remove( obj.data )
    #TYPE(T)
    #bpy.ops.object.delete()
    
    #collection_name = "SCAN_PROCESS"
    #collection = bpy.data.collections[collection_name]
    #for obj in [o for o in collection.objects if o.type == 'MESH']:
    #    if(T in obj.name):
    #        bpy.data.meshes.remove( obj.data )
    #TYPE(T)
    #bpy.ops.object.delete()

def TYPE_HIDE(T):
    obj = TYPE_GET(T)
    obj.hide_set(True)
    
def TYPE_COPY(T,name):
    TYPE(T)
    bpy.ops.object.duplicate(linked=False)
    obj = TYPE_FIND("001")
    TYPE_RENAME(obj,name)
    return obj
    
def TYPE_FIND(NAME):
    for obj in bpy.data.objects:
        if NAME in obj.name:
            return obj
        
def TYPE_RENAME(obj,type):
    start=obj.name.find("_")
    end=obj.name.find(".")
    #end=len(obj.name)
    start+=1
    newName=obj.name[start:end:1]
    print(newName)  
    obj.name =type+"_"+newName
    bpy.data.objects[obj.name].data.name = obj.name

    
def TYPE(T):
    
    #bpy.ops.object.mode_set(mode='OBJECT')
        
    for obj in bpy.data.objects:
        if T in obj.name:
            print("---")
            print("select object :")
            print(obj.name)
            print("---")
            obj.select_set(True)
            material = obj.active_material
            #print(material)   
            for node in material.node_tree.nodes:
                #print(node.name)
                #print("---------")
                if "Texture" in node.name:
                    #node.image = image
                    node.select = True
            #print("---------")
    
def CLEAR_TEXTURES():
    print("s raw_..")
    for image in bpy.data.images:
        print(image.name)
        if("raw" in image.name):
            bpy.data.images.remove(image)
    print("s T_..")        
    for image in bpy.data.images:
        print(image.name)
        if("T_" in image.name):
            bpy.data.images.remove(image)

def CLEAR_TEXTURE_TR():
    print("s tr_..")
    for image in bpy.data.images:
        print(image.name)
        if("TR" in image.name):
            bpy.data.images.remove(image)   
            
            
def MARK_ASSET():
    obj = TYPE_GET("obj")
    bpy.data.objects[obj.name].asset_mark()
    bpy.ops.ed.lib_id_generate_preview({"id": obj})
        
    #collection_name = "SCAN_PROCESS"
    #collection = bpy.data.collections[collection_name]
    #for obj in [o for o in collection.objects if o.type == 'MESH']:
    #    if(T in obj.name):
    #        bpy.data.meshes.remove( obj.data )
    #TYPE(T)
    #bpy.ops.object.delete()
    
def CLEAR_COLLECTION():
    name_coll_c = "Cutters"
    name_coll = "Cutter"
    coll_cutters = bpy.data.collections.get(name_coll)
    if coll_cutters:
        obs = [o for o in coll_cutters.objects]
        while obs:
            obj=obs.pop()
            bpy.data.objects.remove(obj)  
        bpy.data.collections.remove(name_coll_c)

def SET_COLLECTION_ASSET():
    act = bpy.context.selected_objects[0]
    name_coll = "Collection"
    coll_cutters = bpy.data.collections.get(name_coll)
    coll_cutters.name = "C_"+act.name.upper()
    
    coll_cutters.asset_mark()
    #if coll_cutters:
    #    obs = [o for o in coll_cutters.objects]
    #    while obs:
    #        obj=obs.pop()
    #        bpy.data.objects.remove(obj)  
    #    bpy.data.collections.remove(name_coll_c)  


def CLEAR():
    name_coll = "Cutter"
    for mesh in bpy.data.meshes:
        if(name_coll in mesh.name):
            bpy.data.meshes.remove(mesh)
           


def SET_UPPER_NAME_TO_SELECTED():
    act = bpy.context.selected_objects[0]
    act.name = act.name.upper()
    
    
  
     
#TYPE_DELETE("rtp")     
        
#CLEAR_COLLECTION()        
        
        
#CLEAR_TEXTURES()
    
    
#ALL()
#TYPE("raw")
#TYPE("rtp")

#obj = TYPE_GET("rtp")
#print(obj.name)

#TYPE_GET("rtp")

#TYPE("rtp")

#obj_copy = bpy.context.active_object.copy()
#obj = TYPE_COPY("rtp")
#print(obj.name)

#obj =TYPE_COPY("rtp")
#TYPE("dne")



#print(obj.name)

#TYPE_DELETE("rtp")


