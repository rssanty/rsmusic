import yt_dlp
import os
import config
from flask import Flask, request, jsonify, render_template
from pathlib import Path

output_folder = os.path.join(Path.home(), 'Downloads', 'rs music')
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    data = request.get_json()
    url = data.get('url')

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    ydl_opts = config.key.copy()
    ydl_opts['outtmpl'] = os.path.join(output_folder, '%(title)s.%(ext)s')

    try:
        print("Iniciado descargar...")

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("Descarga finalizada.")
        return jsonify({'message': 'Descarga finalizada.'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
