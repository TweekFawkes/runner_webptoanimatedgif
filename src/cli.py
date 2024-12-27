import argparse
from pathlib import Path
from .converter import WebPConverter

def main():
    """Command line interface for WebP to GIF converter"""
    parser = argparse.ArgumentParser(description="Convert animated WebP to GIF")
    parser.add_argument("input", type=str, help="Input WebP file")
    parser.add_argument("output", type=str, help="Output GIF file")
    parser.add_argument("--no-optimize", action="store_true", help="Disable GIF optimization")
    
    args = parser.parse_args()
    
    # Validate paths
    input_path = Path(args.input)
    output_path = Path(args.output)
    
    if not input_path.exists():
        print(f"Error: Input file {input_path} does not exist")
        return 1
        
    # Convert file
    converter = WebPConverter()
    try:
        converter.convert(str(input_path), str(output_path), not args.no_optimize)
        print(f"Successfully converted {input_path} to {output_path}")
        return 0
    except Exception as e:
        print(f"Error during conversion: {e}")
        return 1

if __name__ == "__main__":
    main()
