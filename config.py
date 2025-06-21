import os
from pathlib import Path

output_folder = os.path.join(Path.home(), 'Downloads', 'rs music')

key = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'postprocessor_args': [
        '-ar', '44100'
    ],
    'prefer_ffmpeg': True,
    'geo_bypass': True,
    'verbose': True
}