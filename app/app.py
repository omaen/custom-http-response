from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    text_output = os.getenv('TEXT_OUTPUT', 'Hello, World!')
    text_color = os.getenv('TEXT_COLOR', 'Hello, World!')
    background_color = os.getenv('BACKGROUND_COLOR', 'white')
    return render_template('index.html', text_output=text_output, text_color=text_color, background_color=background_color)


if __name__ == '__main__':
    app.run(host='0.0.0.0')