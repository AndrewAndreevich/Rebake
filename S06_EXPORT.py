import bpy
import os

def FBX():
    bpy.ops.object.select_all(action='DESELECT') 
    S04_SELECT  = bpy.data.texts["S04_SELECT"].as_module()
    S04_SELECT.TYPE("obj")
    cwd =  os.getcwd()
    names = bpy.path.basename(bpy.context.blend_data.filepath).split('.')
    name = names[0]
    directory_im = cwd + "\\ITERATIONS\\S_02_SCAN_OBJ\\"+name+".fbx"
    kwargs = {}
    kwargs["filepath"] = directory_im
    kwargs["use_selection"] = True
    kwargs["path_mode"] = 'COPY'
    #kwargs["tangent_space"] = True
    
    bpy.ops.export_scene.fbx(**kwargs)
    
def BLENDER():
    bpy.ops.object.select_all(action='DESELECT') 
    #S04_SELECT  = bpy.data.texts["S04_SELECT"].as_module()
    #S04_SELECT.TYPE("obj")
    cwd =  os.getcwd()
    names = bpy.path.basename(bpy.context.blend_data.filepath).split('.')
    name = names[0]
    directory_im = cwd + "\\ITERATIONS\\S_02_SCAN_OBJ\\"+name+".blend"
    bpy.ops.wm.save_as_mainfile(filepath=directory_im)

def BLENDER_SAVE_TO_ASSETS(dir):
    bpy.ops.object.select_all(action='DESELECT') 
    #S04_SELECT  = bpy.data.texts["S04_SELECT"].as_module()
    #S04_SELECT.TYPE("obj")
    cwd =  os.getcwd()
    names = bpy.path.basename(bpy.context.blend_data.filepath).split('.')
    name = names[0]
    directory_im = dir+name+".blend"
    bpy.ops.wm.save_as_mainfile(filepath=directory_im)


#FBX()
#BLENDER()

