import bpy
import os
import glob
import math

def IMPORT():
    print("0000000")
   # cwd =  bpy.data.filepath
    #cwd =  os.getcwd()
    filepath =  bpy.data.filepath
    cwd =  os.path.dirname(filepath)
    print ("rootpath "+cwd)
    #print (cwd)
    directory_raw = cwd+"/ITERATIONS/S_00_SCAN_RAW/"
    directory_rtp = cwd+"/ITERATIONS/S_01_SCAN_RTP/"


    files_raw = glob.glob(directory_raw + "*.obj")

    #print (files_raw)
    old_objs = set(bpy.context.scene.objects)
    for f in files_raw:
        head, tail = os.path.split(f)
        collection_name = tail.replace('.obj', '')
        bpy.ops.import_scene.obj(filepath=f)


    files_rtp  = glob.glob(directory_rtp  + "*.obj")

    #print (files_rtp)
    old_objs = set(bpy.context.scene.objects)
    for f in files_rtp:
        head, tail = os.path.split(f)
        collection_name = tail.replace('.obj', '')
        bpy.ops.import_scene.obj(filepath=f)
    bpy.ops.wm.save_mainfile()
    #print("0000000") 
    
    
    
    

