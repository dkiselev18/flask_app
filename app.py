from flask import Flask
from flask import render_template
from flask import request
from get_word_translate import *

app = Flask(__name__)


@app.route('/')
def index():
    word = request.args.get('word')
    image_url = None
    sound = None
    if word:
        result = translate(word)
        if len(word) > 0:
            image_url = result[0][7]
            sound = result[0][8]
            definition = result[0][5]
            transcription = result[0][4]
            translate_words = []
            for row in result:
                translate_words.append((row[2], row[6]))
    else:
        result = None
    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run()
