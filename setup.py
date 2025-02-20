import subprocess
import sys
import os
import venv
from pathlib import Path

def create_venv():
    print("Creating virtual environment...")
    venv_path = Path("venv")
    
    if venv_path.exists():
        print("Virtual environment already exists")
        return str(venv_path)
    
    venv.create(venv_path, with_pip=True)
    print("Virtual environment created successfully")
    return str(venv_path)

def get_venv_python():
    # Get the path to the virtual environment's Python executable
    if sys.platform == "win32":
        python_path = Path("venv/Scripts/python.exe")
    else:
        python_path = Path("venv/bin/python")
    return str(python_path)

def install_requirements(python_path):
    try:
        # Upgrade pip first
        print("Upgrading pip...")
        subprocess.check_call([python_path, "-m", "pip", "install", "--upgrade", "pip"])
        
        print("Installing required packages...")
        subprocess.check_call([python_path, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Successfully installed all required packages")
    except subprocess.CalledProcessError as e:
        print(f"Error installing packages: {str(e)}")
        print("\nTrying to install packages individually...")
        
        # Read requirements and try to install one by one
        with open("requirements.txt", "r") as f:
            requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]
        
        for req in requirements:
            try:
                print(f"Installing {req}...")
                subprocess.check_call([python_path, "-m", "pip", "install", req])
            except subprocess.CalledProcessError as e:
                print(f"Warning: Failed to install {req}: {str(e)}")
                print("Continuing with remaining packages...")
                continue

def main():
    print("Setting up 3D model converter environment...")
    
    # Create virtual environment
    venv_path = create_venv()
    python_path = get_venv_python()
    
    # Install all requirements
    install_requirements(python_path)
    
    # Create launcher script
    if sys.platform == "win32":
        with open("run_converter.bat", "w") as f:
            f.write(f"@echo off\n")
            f.write(f"call {venv_path}\\Scripts\\activate.bat\n")
            f.write(f"python model_converter.py\n")
            f.write("pause\n")
    else:
        with open("run_converter.sh", "w") as f:
            f.write("#!/bin/bash\n")
            f.write(f"source {venv_path}/bin/activate\n")
            f.write("python model_converter.py\n")
        # Make the shell script executable
        os.chmod("run_converter.sh", 0o755)
    
    print("\nSetup complete!")
    print("\nTo run the 3D Model Converter:")
    if sys.platform == "win32":
        print("Run run_converter.bat")
    else:
        print("Run ./run_converter.sh")

if __name__ == "__main__":
    main() 