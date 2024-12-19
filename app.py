from flask import Flask, request, send_file
import pyttsx3
import os
import base64
from flask import render_template

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def tts():
    if request.method == 'POST':
        text = request.form['text']
        engine = pyttsx3.init()
        engine.save_to_file(text, 'speech.mp3')
        engine.runAndWait()
        engine.stop()
        return send_file('speech.mp3', mimetype='audio/mpeg', as_attachment=True, download_name='speech.mp3')
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
