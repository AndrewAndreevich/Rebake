import bpy
import math 
from mathutils import Euler
#bpy.data.objects["Cube"].select_set(True)
#bpy.ops.object.editmode_toggle()
#bpy.ops.mesh.select_all(action='SELECT')
#bpy.ops.uv.smart_project()

 
# to select the object in the 3D viewport,


def SMARTPROJECT(T):
    
    bpy.ops.object.select_all(action='DESELECT') 
    for obj in bpy.data.objects:
        if T in obj.name:
            #print ("OBJECT TO UNWRAP : "+obj.name)
            bpy.context.view_layer.objects.active = obj
            obj.select_set(True)
            #current_state = obj.select_get()
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.uv.smart_project()
            #print ("UNWRAP DONE: "+obj.name)
            #print ("DELETE MATERIALS : "+obj.name)
            bpy.ops.object.mode_set(mode='OBJECT')

def SETMATERIALS(T,MAT):

    #bpy.ops.object.select_all(action='DESELECT') 
        
    for obj in bpy.data.objects:
        if T in obj.name:           
            bpy.context.view_layer.objects.active = obj
            obj.select_set(True)
            
            for ms in obj.material_slots:
                ms.material = None 
                   
            mat = bpy.data.materials.get(MAT)
            obj.data.materials[0] = mat
            
            
def SETMATERIALNAME(T,MAT):

    #bpy.ops.object.select_all(action='DESELECT') 
        
    for obj in bpy.data.objects:
        if T in obj.name:           
            bpy.context.view_layer.objects.active = obj
            obj.select_set(True)
            
            for ms in obj.data.materials:
                if MAT in ms.name: 
                    ms.name = "M_"+obj.name
                    ms.name =  ms.name.upper()
                                
def REFRAME():
    bpy.ops.object.select_all(action='DESELECT') 
    S04_SELECT  = bpy.data.texts["S04_SELECT"].as_module()
    ob1 = S04_SELECT.TYPE_GET("raw")
    ob1.rotation_euler = Euler((0, 0, 0), 'XYZ')
    #S04_SELECT.TYPE_HIDE("raw")
    #or
    S04_SELECT.TYPE_DELETE("raw")

    ob2 = S04_SELECT.TYPE_GET("rtp")
    ob2.rotation_euler = Euler((0, 0, 0), 'XYZ')
    S04_SELECT.TYPE("rtp")
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
    bpy.data.objects[ob2.name].location = (0.0,0.0,0.0)

            

def ADD_MODIF_DECIMATE(val):
    act = bpy.context.selected_objects[0]
    print(act)
    bpy.context.view_layer.objects.active = act #sets the obj accessible to bpy.ops
    bpy.ops.object.modifier_add(type='DECIMATE')
    bpy.context.object.modifiers["Decimate"].ratio = val
    bpy.ops.object.modifier_apply(modifier="Decimate")
    bpy.context.view_layer.objects.active = act

            

def APPLY_MODIFIERS():
    obj = bpy.context.selected_objects[0]
    ctx = bpy.context.copy()
    ctx['object'] = obj
    for _, m in enumerate(obj.modifiers):
        try:
            ctx['modifier'] = m
            bpy.ops.object.modifier_apply(ctx, modifier=m.name)
        except RuntimeError:
            print(f"Error applying {m.name} to {obj.name}, removing it instead.")
            obj.modifiers.remove(m)

    for m in obj.modifiers:
        obj.modifiers.remove(m)

def APPLY_SMOOTH():
    bpy.context.selected_objects[0].data.polygons.foreach_set('use_smooth',[True] * len(bpy.context.selected_objects[0].data.polygons))
    bpy.context.selected_objects[0].data.update()