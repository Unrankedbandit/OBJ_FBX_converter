# OBJ/FBX Converter

A tool for converting between OBJ and FBX 3D model file formats.

## Features

- Convert OBJ files to FBX format
- Convert FBX files to OBJ format
- Preserve mesh data during conversion
- Support for materials and textures
- Command-line interface for easy automation

## Installation

basj 

## clone the repository

```bash
git clone https://github.com/username/obj_fbx_converter.git
```

## navigate to the project directory

```bash
cd obj_fbx_converter
```

## Usage

### Command Line Interface

```bash
# Convert OBJ to FBX
python converter.py --input model.obj --output model.fbx

# Convert FBX to OBJ
python converter.py --input model.fbx --output model.obj
```

### Options

- `--input`: Path to input file (required)
- `--output`: Path to output file (required)
- `--preserve-materials`: Keep original material settings (optional)
- `--scale`: Apply scaling factor during conversion (optional)

## Requirements

- Python 3.7 or higher
- FBX SDK
- Additional dependencies listed in requirements.txt

## Known Limitations

- Some complex materials may not convert perfectly
- Animation data is not currently supported
- Vertex colors may not be preserved in all cases

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- FBX SDK by Autodesk
- OBJ file format specification
- Contributors and maintainers

## Support

If you encounter any issues or have questions, please:
1. Check the [Issues](https://github.com/unrankedbandit/obj_fbx_converter/issues) page
2. Create a new issue with detailed information about your problem


