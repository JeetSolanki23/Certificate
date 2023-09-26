from flask import Flask, render_template, request, send_file
from PIL import Image, ImageDraw, ImageFont
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_certificate():
    name = request.form['name']
    template_path = 'static/certificate_template.png'
    #font_path = 'fonts/arial.ttf'
    output_path = f'static/generated_certificates/{name}_certificate.png'

    # Load the certificate template image
    template = Image.open(template_path)

    # Create a drawing context
    draw = ImageDraw.Draw(template)

    # Load the font
    font = ImageFont.truetype(font_path, size=48)

    # Position and text color
    text_position = (400, 300)
    text_color = (0, 0, 0)  # Black

    # Draw the name on the certificate
    draw.text(text_position, name, font=font, fill=text_color)

    # Save the generated certificate
    template.save(output_path)

    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run()
