# runner_webptoanimatedgif // WebP to GIF Converter

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

```bash
python -m src.cli input.webp output.gif
python -m src.cli 20241227-001-giphy.webp 20241227-001-giphy.gif
```

## Features
- Preserves animation timing
- Maintains image quality
- Progress tracking
- Command-line interface

## Requirements
- Python 3.8+
- Pillow (with WebP support)
