from flask import Flask, render_template, request
from googletrans import Translator, LANGUAGES
from unidecode import unidecode

app = Flask(__name__)

def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    transliteration = unidecode(translation.text)

    return translation.text, transliteration

@app.route('/')
def index():
    return render_template('index.html', languages=LANGUAGES)

@app.route('/translate', methods=['POST'])
def translate():
    word = request.form['word']
    target_language = request.form['target_language']

    translation, transliteration = translate_text(word, target_language)

    return render_template('result.html', word=word, target_language=target_language, translation=translation, transliteration=transliteration)

if __name__ == '__main__':
    app.run()
