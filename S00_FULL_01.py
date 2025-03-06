import bpy

S01_RAWDATA  = bpy.data.texts["S01_RAWDATA"].as_module()
S02_TEXTURES = bpy.data.texts["S02_TEXTURES"].as_module()
S03_PREPARE  = bpy.data.texts["S03_PREPARE"].as_module()
S04_SELECT   = bpy.data.texts["S04_SELECT"].as_module()
S05_BAKE     = bpy.data.texts["S05_BAKE"].as_module()
S06_EXPORT   = bpy.data.texts["S06_EXPORT"].as_module()

S01_RAWDATA.IMPORT()

size_02k = 2048, 2048,"02K" 
size_04k = 4096, 4096,"04K"
size_08k = 8192, 8192,"08K"
size_16k = 16384, 16384,"16K"
size_param = size_02k

S02_TEXTURES.CREATE("T_",True,"RAW",size_param)

S03_PREPARE.SMARTPROJECT("rtp")
S03_PREPARE.SETMATERIALS("rtp","RAW")
S04_SELECT.ALL("raw","rtp")
S05_BAKE.DEFFUCE("T_")
S03_PREPARE.REFRAME()

