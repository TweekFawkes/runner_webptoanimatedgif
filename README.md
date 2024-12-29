# WebP to GIF Converter

Convert animated WebP files to GIF format while preserving animation timing and quality.

## Installation

```bash
pip install -r requirements.txt
```

If you encounter any issues, you might need to install system-level WebP dependencies:

### Ubuntu/Debian
```bash
sudo apt-get install webp libwebp-dev
```

### macOS
```bash
brew install webp
```

## Usage

1. Place your WebP file in the `inputs` directory
2. Run the converter:
```bash
python3 app.py inputs/input.webp outputs/output.gif
```

Example:
```bash
# Place 20241227-001-giphy.webp in the inputs directory
python3 app.py inputs/20241227-001-giphy.webp outputs/20241227-001-giphy.gif
```

## Features
- Preserves animation timing
- Maintains image quality
- Progress tracking
- Command-line interface
- Organized input/output directories

## Requirements
- Python 3.8+
- Pillow (with WebP support)

## Project Structure
```
.
├── inputs/         # Place WebP files here
├── outputs/        # Converted GIFs will be saved here
├── app.py         # Main application file
├── requirements.txt
└── README.md
```
