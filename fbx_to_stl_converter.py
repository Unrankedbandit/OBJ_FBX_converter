import sys
import os

def convert_fbx_to_stl(input_file, output_file):
    try:
        import bpy
        
        # Clear existing objects
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete()
        
        # Import FBX
        bpy.ops.import_scene.fbx(filepath=input_file)
        
        # Select all objects
        bpy.ops.object.select_all(action='SELECT')
        
        # Export as STL
        bpy.ops.export_mesh.stl(filepath=output_file)
        print(f"Successfully converted {input_file} to {output_file}")
    except Exception as e:
        print(f"Error converting file: {str(e)}")

if __name__ == "__main__":
    # Input and output file paths
    input_fbx = "SelfWateringPlantpot.fbx"
    output_stl = "SelfWateringPlantpot.stl"
    
    # Check if input file exists
    if not os.path.exists(input_fbx):
        print(f"Error: Input file {input_fbx} not found")
    else:
        convert_fbx_to_stl(input_fbx, output_stl) 