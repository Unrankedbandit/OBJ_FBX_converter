import sys
import os
import subprocess
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                            QTextEdit, QFileDialog, QFrame)
from PyQt6.QtCore import Qt
from obj_to_stl_converter import convert_obj_to_stl

class ModelConverterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("3D Model Converter")
        self.setMinimumSize(800, 600)
        
        # Create main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        
        # Title
        title_label = QLabel("3D Model Converter")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; margin: 20px;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)
        
        # Input file section
        input_frame = QFrame()
        input_frame.setFrameStyle(QFrame.Shape.StyledPanel)
        input_layout = QHBoxLayout(input_frame)
        
        input_label = QLabel("Input File:")
        self.input_path = QLineEdit()
        self.input_path.setReadOnly(True)
        browse_input_btn = QPushButton("Browse")
        browse_input_btn.clicked.connect(self.browse_input)
        
        input_layout.addWidget(input_label)
        input_layout.addWidget(self.input_path)
        input_layout.addWidget(browse_input_btn)
        layout.addWidget(input_frame)
        
        # Output directory section
        output_frame = QFrame()
        output_frame.setFrameStyle(QFrame.Shape.StyledPanel)
        output_layout = QHBoxLayout(output_frame)
        
        output_label = QLabel("Output Directory:")
        self.output_path = QLineEdit()
        self.output_path.setReadOnly(True)
        browse_output_btn = QPushButton("Browse")
        browse_output_btn.clicked.connect(self.browse_output)
        
        output_layout.addWidget(output_label)
        output_layout.addWidget(self.output_path)
        output_layout.addWidget(browse_output_btn)
        layout.addWidget(output_frame)
        
        # Status section
        status_frame = QFrame()
        status_frame.setFrameStyle(QFrame.Shape.StyledPanel)
        status_layout = QVBoxLayout(status_frame)
        
        status_label = QLabel("Status:")
        self.status_text = QTextEdit()
        self.status_text.setReadOnly(True)
        
        status_layout.addWidget(status_label)
        status_layout.addWidget(self.status_text)
        layout.addWidget(status_frame)
        
        # Buttons
        button_frame = QFrame()
        button_layout = QHBoxLayout(button_frame)
        
        convert_btn = QPushButton("Convert")
        convert_btn.clicked.connect(self.convert)
        clear_btn = QPushButton("Clear")
        clear_btn.clicked.connect(self.clear)
        exit_btn = QPushButton("Exit")
        exit_btn.clicked.connect(self.close)
        
        button_layout.addWidget(convert_btn)
        button_layout.addWidget(clear_btn)
        button_layout.addWidget(exit_btn)
        layout.addWidget(button_frame)
        
        # Style buttons
        for btn in [browse_input_btn, browse_output_btn, convert_btn, clear_btn, exit_btn]:
            btn.setMinimumWidth(100)
            btn.setStyleSheet("""
                QPushButton {
                    padding: 8px;
                    background-color: #f0f0f0;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                }
                QPushButton:hover {
                    background-color: #e0e0e0;
                }
                QPushButton:pressed {
                    background-color: #d0d0d0;
                }
            """)

    def browse_input(self):
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Select Input File",
            "",
            "3D Models (*.obj *.fbx);;OBJ Files (*.obj);;FBX Files (*.fbx);;All Files (*.*)"
        )
        if filename:
            self.input_path.setText(filename)
            # Auto-set output directory to same as input
            if not self.output_path.text():
                self.output_path.setText(os.path.dirname(filename))

    def browse_output(self):
        directory = QFileDialog.getExistingDirectory(
            self,
            "Select Output Directory",
            ""
        )
        if directory:
            self.output_path.setText(directory)

    def update_status(self, message):
        self.status_text.append(message)

    def clear(self):
        self.input_path.clear()
        self.output_path.clear()
        self.status_text.clear()

    def convert(self):
        input_file = self.input_path.text()
        output_dir = self.output_path.text()
        
        if not input_file:
            self.update_status("Error: Please select an input file")
            return
            
        if not os.path.exists(input_file):
            self.update_status("Error: Input file does not exist")
            return
            
        # Create output file path
        output_file = os.path.join(
            output_dir if output_dir else os.path.dirname(input_file),
            os.path.splitext(os.path.basename(input_file))[0] + '.stl'
        )
        
        self.update_status(f"Converting {os.path.basename(input_file)} to {os.path.basename(output_file)}...")
        
        try:
            file_ext = os.path.splitext(input_file)[1].lower()
            
            if file_ext == '.obj':
                convert_obj_to_stl(input_file, output_file)
                
            elif file_ext == '.fbx':
                # Create temporary Python script for Blender
                script_content = f'''
import sys
sys.path.append("{os.getcwd()}")
from fbx_to_stl_converter import convert_fbx_to_stl
convert_fbx_to_stl("{input_file.replace('\\', '/')}", "{output_file.replace('\\', '/')}")
'''
                with open("temp_convert.py", "w") as f:
                    f.write(script_content)
                
                # Run Blender in background mode
                blender_path = "C:\\Program Files\\Blender Foundation\\Blender 4.0\\blender.exe" if sys.platform == "win32" else "blender"
                subprocess.run([blender_path, "--background", "--python", "temp_convert.py"])
                os.remove("temp_convert.py")
                
            self.update_status("Conversion completed successfully!")
            
        except Exception as e:
            self.update_status(f"Error converting file: {str(e)}")

def main():
    app = QApplication(sys.argv)
    window = ModelConverterApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 