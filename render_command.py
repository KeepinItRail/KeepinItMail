#################################
####### SET UP FILES HERE #######
#################################

# Vehicle Name - this will also be the name of the folder the sprites will appear in the NewGRF's folder
vehicle_name = "transit"

# Manifests to use - I use several to get the size I want
vehicle_manifest = "manifest_transit"
manifest_size = "100_46_63"

# select zoom levels desired, options are 1,2,4
zoom_levels = "1,2"

# File and Folder locations

# Source folder (i.e. the MagicaVoxel folder) - much easier to store with MagicaVoxel to work on and then run this script when sprites are wanted
src_folder = r"/home/john/Applications/MagicaVoxel/vox/KeepinItMail/"
# Destination folder - i.e. in the NewGRF folder which the sprites are for. This will also copy the voxels beforehand to allow production of the sprites
dst_folder = r"/home/john/Projects/KeepinItMail/voxel/" 

#################################
# NO NEED TO CHANGE STUFF BELOW #
#################################

import subprocess
import shutil
import os

# Copy voxel from MagicaVoxel folder to NewGRF folder
src_path = src_folder + vehicle_name + ".vox"
dst_path = dst_folder + vehicle_name + ".vox"
shutil.copy(src_path, dst_path)
print("'" + vehicle_name + ".vox' voxel transferred from MagicaVoxel to NewGRF voxel folder")

input_voxel = "voxel/" + vehicle_name + ".vox"                          # Which voxel is to be used by GoRender
manifest_path = "voxel/manifest/" + vehicle_manifest + ".json"          # Which manifest is to be used by GoRender
output_sprite = "src/gfx/" + vehicle_name + "/" + manifest_size         # Where the produced sprites will be sent       

output_sprite_path = output_sprite + ".png"                             # What the produced sprites will be called

if os.path.exists(output_sprite_path):
    os.remove(output_sprite_path)

gorender = subprocess.run(["./renderobject", "-input", input_voxel, "-m", manifest_path, "-output", output_sprite, "-8", "-palette", "/home/john/Applications/gorender/files/ttd_palette.json", "-scale", zoom_levels], stdout = subprocess.PIPE, text=True)
print(gorender.stdout)
print("'" + vehicle_name + ".png' sprites produced from '" + vehicle_name + ".vox'")
