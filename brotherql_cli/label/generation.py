from PIL import Image, ImageDraw, ImageFont
import string
import math
import sys

def generate_image(label_lines:list[str]) -> Image.Image:
    """
    Generate label image to print
    """
    # IMAGE WIDTH {62mm} * DPI {300} / 25.4 to nearest px
    image_width_px = 696
    # SPACING {2mm} * DPI {300} / 25.4 to nearest px
    spacing_px = 47
    
    # For construction of label image
    temp_image = Image.new("RGB", (image_width_px, 1))
    draw = ImageDraw.Draw(temp_image)

    # Get font path
    # Mac
    if sys.platform == "darwin":
        font_path = "/Library/Fonts/Arial Unicode.ttf"
    # Windows
    elif sys.platform == "win32":
        font_path = "C:\\Windows\\Fonts\\arial.tff"

    # Simulate rendering longest line to find font size
    longline = max(label_lines, key=len)
    font: ImageFont.FreeTypeFont

    sim_text_width = 0
    font_size = 0
    # Font size can never be larger than 64px
    while sim_text_width < image_width_px and font_size < 64:
        font_size += 1
        font = ImageFont.truetype(font_path, font_size)
        # Get simulated text bounding box
        sim_text_bbox = draw.textbbox((0, 0), longline, font=font)
        # Get width of bounding box
        sim_text_width = sim_text_bbox[2] - sim_text_bbox[0]

    # Simulate text to calc image height
    # Get simulated text bounding box
    sim_text_bbox = draw.textbbox((0, 0), string.ascii_letters + string.digits, font=font)
    # Get height of bounding box (rounded up to nearest int)
    text_height = math.ceil(sim_text_bbox[3] - sim_text_bbox[1])

    # Multiply simulated height + spacing {2px} by number of lines
    # And round up to nearest integer
    image_height_px = (text_height + spacing_px) * len(label_lines)
    
    # Includes 6 pixels of height padding for descenders
    image = Image.new("RGB", (image_width_px, image_height_px + 6), color="white")
    draw = ImageDraw.Draw(image)

    # Generate image
    # Base height
    current_height_px = 0
    for line in label_lines:
        draw.text((5, current_height_px), line, font=font, fill="black", align='left')
        current_height_px += text_height + spacing_px

    # Convert to black and white and flip
    # image = ImageOps.invert(image)
    # image = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    
    return image

__all__ = [
    "generate_image"
]