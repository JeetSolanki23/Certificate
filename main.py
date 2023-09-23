from flask import Flask, render_template, request
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

@app.route('/')
def index():
    return "hello"
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    name = request.form['name']
    template = Image.open('certificate_template.png')  # Replace with your certificate template image

    # Load the font for the certificate text
    font = ImageFont.truetype('arial.ttf', 48)  # Replace with your desired font and size

    # Create a draw object
    draw = ImageDraw.Draw(template)

    # Calculate the position to center the text
    text_width, text_height = draw.textsize(name, font=font)
    x = (template.width - text_width) / 2
    y = (template.height - text_height) / 2

    # Draw the text on the certificate
    draw.text((x, y), name, fill='black', font=font)

    # Save the generated certificate
    certificate_path = f'certificates/{name}.png'  # Replace with your desired output path
    template.save(certificate_path)

    return render_template('certificate.html', name=name, certificate_path=certificate_path)

if __name__ == '__main__':
    app.run(debug=True)
