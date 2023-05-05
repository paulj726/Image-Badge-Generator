
from PIL import Image, ImageDraw, ImageFont
import random
# Define font style, color, and size constants
color = (255, 255, 255)
font_style = 'fonts/Roboto-Regular.ttf'
font_size = 80

def generate_circle_badge(text, font_style, font_size):
    # Set up image
    size = (500, 500)
    img = Image.new('RGB', size, (0, 0, 0))
    bg_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    # Generate image
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_style, font_size)
    text_width, text_height = draw.textsize(text, font=font)
    x = (size[0] - text_width) / 2
    y = (size[1] - text_height) / 2
    draw.ellipse((x - 30, y - 30, x + text_width + 30, y + text_height + 30), fill=bg_color)
    draw.ellipse((x, y, x + text_width, y + text_height), fill=(255, 255, 255), outline=bg_color)
    draw.text((x, y), text, font=font, fill=color)
    # Save image as PNG file
    img.save(text+'.png')