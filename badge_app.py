# Import required libraries and modules

from io import BytesIO
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from flask import Flask, render_template, request, send_file

app = Flask(__name__)

# Function to create the badge

@app.route('/', methods=['GET', 'POST'])
def create_badge():
    if request.method == 'POST':
        # Get parameters from HTML form
        text = request.form.get('text', 'SAMPLE TEXT')
        font_style = request.form.get('font-style', 'OpenSans-Bold.ttf')
        font_size = int(request.form.get('font-size', 65))
        emboss = request.form.get('emboss', False) == 'on'
        circle_color = request.form.get('circle-color', 'orange')
        size = int(request.form.get('size', 200))

        # Set font and text dimensions
        font = ImageFont.truetype(font_style, font_size)
        char_width, char_height = font.getsize('A')
        chars_per_line = int(1.8 * size / char_width)
        max_lines = int(1.8 * size / char_height)

        # Add input validation to ensure user inputs are valid
        if size > 500:
            size = 500
        if font_size > 150 or font_size < 10:
            font_size = 65
        if not text:
            text = 'SAMPLE TEXT'

        # Create badge image
        bg_color = (255, 255, 255)
        img = Image.new('RGBA', (size, size), bg_color)
        draw = ImageDraw.Draw(img)
        text_color = (0, 0, 0)
        circle_coords = [(10, 10), (size-10, size-10)]
        draw.ellipse(circle_coords, fill=circle_color)

        # Add text to badge image
        words = text.split()
        line = ''
        lines = []
        for word in words:
            if len(line + word) <= chars_per_line:
                line += word + ' '
            else:
                lines.append(line)
                line = ''
        if line:
            lines.append(line)
        num_lines = len(lines)
        if num_lines <= max_lines:
            y_pos = (size - num_lines * char_height) // 2
            for line in lines:
                line_width, line_height = font.getsize(line)
                x_pos = (size - line_width) // 2
                draw.text((x_pos, y_pos), line, font=font, fill=text_color)
                y_pos += char_height

        # Add emboss effect if selected
        if emboss:
            img = img.filter(ImageFilter.EMBOSS)

        # Add error handling for image creation and file serving
        try:
            # Return badge image as PNG file
            return serve_pil_image(img)
        except Exception as e:
            print(e)

# Helper function to output badge as PNG file

@app.route('/badge')
def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)
