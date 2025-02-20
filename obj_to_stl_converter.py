import trimesh
import os

def convert_obj_to_stl(input_file, output_file):
    try:
        # Load the OBJ file
        mesh = trimesh.load(input_file)
        
        # Export as STL
        mesh.export(output_file)
        print(f"Successfully converted {input_file} to {output_file}")
    except Exception as e:
        print(f"Error converting file: {str(e)}")

if __name__ == "__main__":
    # Input and output file paths
    input_obj = "test.obj"
    output_stl = "test.stl"
    
    # Check if input file exists
    if not os.path.exists(input_obj):
        print(f"Error: Input file {input_obj} not found")
    else:
        convert_obj_to_stl(input_obj, output_stl) 