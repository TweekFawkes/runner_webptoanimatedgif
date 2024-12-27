from PIL import Image
import webp
from typing import Tuple, List
import io

class WebPConverter:
    def __init__(self):
        self.frames = []
        self.durations = []

    def validate_webp(self, file_path: str) -> bool:
        """Validate if file is animated WebP"""
        try:
            with Image.open(file_path) as img:
                return img.format == "WEBP" and hasattr(img, "is_animated") and img.is_animated
        except Exception:
            return False

    def extract_frames(self, file_path: str) -> Tuple[List[Image.Image], List[int]]:
        """Extract frames and timing data from WebP"""
        webp_data = webp.WebPData.from_file(file_path)
        anim = webp_data.get_info().has_animation

        if not anim:
            raise ValueError("Not an animated WebP file")

        # Extract frames and durations
        frames = []
        durations = []
        
        for frame in webp_data.frames:
            img = Image.open(io.BytesIO(frame.image_data))
            frames.append(img)
            durations.append(frame.duration)

        return frames, durations

    def convert(self, input_path: str, output_path: str, optimize: bool = True) -> None:
        """Convert WebP to GIF"""
        if not self.validate_webp(input_path):
            raise ValueError("Invalid WebP file")

        # Extract frames and timing
        frames, durations = self.extract_frames(input_path)

        # Save as GIF
        frames[0].save(
            output_path,
            save_all=True,
            append_images=frames[1:],
            optimize=optimize,
            duration=durations,
            loop=0
        )
