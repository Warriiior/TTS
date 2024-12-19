from flask import Flask, request, send_file
import pyttsx3
import os
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def tts():
    if request.method == 'POST':
        text = request.form['text']
        engine = pyttsx3.init()
        engine.save_to_file(text, 'speech.mp3')
        engine.runAndWait()
        engine.stop()
        return send_file('speech.mp3', mimetype='audio/mpeg', as_attachment=True, download_name='speech.mp3')
    return '''
        <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
        <div class="flex justify-center items-center h-screen bg-gray-100">
            <div class="bg-white p-8 rounded shadow-md w-96">
                <h1 class="text-2xl font-bold mb-4 text-center">Text to Speech</h1>
                <form method="post" class="space-y-4">
                    <textarea name="text" class="w-full p-2 border rounded" placeholder="Enter text to convert to speech"></textarea>
                    <div class="flex space-x-2">
                        <input type="submit" value="Generate Audio" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded cursor-pointer">
                    </div>
                </form>
            </div>
        </div>
    '''



if __name__ == '__main__':
    app.run(debug=True)
