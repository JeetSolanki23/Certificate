from flask import Flask, render_template, request
#from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

@app.route('/')
def index():
    return "hello"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
