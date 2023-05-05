from flask import Flask, request, render_template, send_file
from PIL import Image, ImageDraw, ImageFont
import os

app = Flask(__name__)

app.config["CUSTOM_FONTS_DIR"] = os.path.join(app.root_path, "fonts")

@app.route("/")
def index():
    return render_template("index.html")


def generate_badge(color, size, font, text, style, emboss):
    # Define Circle Size and Position
    circle_x, circle_y = size/2, size/2
    circle_r = size/2
    im_size = (size, size)

    # Define Font and Text Settings
    font_size = 70
    font_color = color
    text_position = (circle_x - font_size*len(text)/4, circle_y - font_size/2)
    font_file = os.path.join(app.config["CUSTOM_FONTS_DIR"], font)
    font_type = ImageFont.truetype(font_file, font_size)

    # Create Circle and Text on Image Based on Style
    im = Image.new("RGBA", im_size, color)
    draw = ImageDraw.Draw(im)
    if style == 'embossed':
        emboss_positions = {'top': (0,-1), 'bottom': (0,1), 'left': (-1,0), 'right': (1,0)}
        for emboss_pos in emboss_positions:
            emboss_x, emboss_y = emboss_positions[emboss_pos]
            draw.ellipse([circle_x-circle_r+emboss_x, circle_y-circle_r+emboss_y, circle_x+circle_r+emboss_x, circle_y+circle_r+emboss_y], fill=None, outline=(0,0,0,255))
            draw.text((text_position[0]+emboss_x, text_position[1]+emboss_y), text, font_type, fill=(0,0,0,255))
    else:
        draw.ellipse([0, 0, size, size], fill=color, outline=color)
        draw.text(text_position, text, font_type, fill=font_color)

    # Save Image and Return File Name
    filename = "badge.png"
    im.save(filename)
    return filename

    
@app.route("/badge")
def badge():
    color = request.args.get('color', '#000000')
    size = int(request.args.get('size', '100'))
    font = request.args.get('font', 'Arial.ttf')
    text = request.args.get('text', '')
    style = request.args.get('style', 'flat')
    emboss = request.args.get('emboss', '')
    filename = generate_badge(color, size, font, text, style, emboss)
    return send_file(filename)

@app.route("/image")
def image():
    return send_file("badge.png")
from flask import Flask, render_template, request, send_file
from generate_badge import generate_circle_badge
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def create_badge():
    text = request.form['text']
    font_style = request.form['font_style']
    font_size = request.form['font_size']
    color = request.form['color']
    style = request.form['style']
    if style == 'embossed':
        # Create embossed effect
        generate_circle_badge(text, font_style, int(font_size)/2)
        filename = text + '.png'
    else:
        # Create regular badge
        generate_circle_badge(text, font_style, int(font_size))
        filename = text + '_{}.png'.format(color)
    # Send file to user for download
    return send_file(filename, as_attachment=True)