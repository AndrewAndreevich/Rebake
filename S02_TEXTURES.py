import bpy
import os
from pathlib import Path


#,SIZE,SETIMAGE,TYPE
def CREATE(PREFIX,SETIMAGE,MATERIAL,SIZE_P):
    """Create new Texture's

    Parameters
    ----------
    TYPE : str
        Texture type, like T_("texture) or "N_"(normal)
    SETIMAGE : bool, optional
        A flag used to set texture to MAIN material or not (default is
        False)
    """
    
    #folder,
    #preset_rtp = "S_01_SCAN_RTP",
    #if "rtp" in TYPE:
        

    
    size= SIZE_P
    

    name_path = Path(bpy.path.basename(bpy.context.blend_data.filepath)).stem
    name_full = PREFIX+size[2]+"_"+name_path
    
    # blank image
    image = bpy.data.images.new(name_full, width=size[0], height=size[1])

    cwd =  os.getcwd()
    cwd =  bpy.data.filepath
    
    directory_im = "//ITERATIONS/S_01_SCAN_RTP"
    #print (directory_im)
    
    # write image
    image.filepath_raw = directory_im+"/"+name_full+".jpeg"
    #print (image.filepath_raw)
    image.file_format = 'JPEG'
    image.save()
    
    if(SETIMAGE):
        mat = bpy.data.materials.get(MATERIAL)
        
        #print("---------")   
        for obj in mat.node_tree.nodes:
            #print(obj.name)
            if "Texture" in obj.name:
                obj.image = image
    #print("---------")

        for area in bpy.context.screen.areas:
            #print(area.type)
            if area.type == 'IMAGE_EDITOR':
                #print("THERE IS IT!")
                area.spaces.active.image = image



#TEXTURE RAW
#CREATE("TR_",True,"MAIN")
#TEXTURE DONE
#S02_TEXTURES("T_")

