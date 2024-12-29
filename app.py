import argparse
from pathlib import Path
from PIL import Image
from typing import Tuple, List

class WebPConverter:
    def __init__(self):
        self.frames = []
        self.durations = []

    def validate_webp(self, file_path: str) -> bool:
        """Validate if file is animated WebP"""
        try:
            with Image.open(file_path) as img:
                return img.format == "WEBP" and getattr(img, "is_animated", False)
        except Exception:
            return False

    def extract_frames(self, file_path: str) -> Tuple[List[Image.Image], List[int]]:
        """Extract frames and timing data from WebP"""
        frames = []
        durations = []
        
        with Image.open(file_path) as img:
            if not getattr(img, "is_animated", False):
                raise ValueError("Not an animated WebP file")
            
            try:
                while True:
                    # Get current frame duration in milliseconds
                    duration = img.info.get('duration', 100)  # default to 100ms if not specified
                    
                    # Convert frame to RGB mode
                    current_frame = img.convert('RGB')
                    
                    frames.append(current_frame)
                    durations.append(duration)
                    
                    img.seek(img.tell() + 1)
            except EOFError:
                pass  # We've hit the last frame

        return frames, durations

    def convert(self, input_path: str, output_path: str, optimize: bool = True) -> None:
        """Convert WebP to GIF"""
        if not self.validate_webp(input_path):
            raise ValueError("Invalid or non-animated WebP file")

        # Extract frames and timing
        frames, durations = self.extract_frames(input_path)

        # Save as GIF
        frames[0].save(
            output_path,
            format='GIF',
            save_all=True,
            append_images=frames[1:],
            optimize=optimize,
            duration=durations,
            loop=0,
            disposal=2,  # Clear the frame before rendering the next one
            quality=95,  # Higher quality
            dither=Image.Dither.FLOYDSTEINBERG  # Use dithering for better color representation
        )

def main():
    """Command line interface for WebP to GIF converter"""
    parser = argparse.ArgumentParser(description="Convert animated WebP to GIF")
    parser.add_argument("input", type=str, help="Input WebP file name (from inputs directory)")
    parser.add_argument("--no-optimize", action="store_true", help="Disable GIF optimization")
    
    args = parser.parse_args()
    
    # Ensure input is from inputs directory
    input_path = Path("inputs") / args.input
    
    # Create output path with same name but .gif extension
    output_path = Path("outputs") / input_path.with_suffix('.gif').name
    
    # Create outputs directory if it doesn't exist
    Path("outputs").mkdir(exist_ok=True)
    
    if not input_path.exists():
        print(f"Error: Input file {input_path} does not exist")
        print("Please place your WebP file in the 'inputs' directory")
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