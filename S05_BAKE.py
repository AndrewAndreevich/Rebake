import bpy
import time
import os
import glob
import math



def DEFFUCE(TYPE):        
    #startTime = time.strftime("%Y-%m-%d %H:%M:%S")
    bpy.ops.object.bake(type='DIFFUSE')
    for image in bpy.data.images:
        print(image.name)
        if TYPE in image.name:
            image.save()
    #timeToBake = time.process_time() - startTime
    #endTime = time.strftime("%Y-%m-%d %H:%M:%S")

    #print("Time to bake the fluid sim was",timeToBake,"seconds")
    #print("Start - ", startTime)
    #print("End   - ", endTime)



#DEFFUCE()