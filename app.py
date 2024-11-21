from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
import os
from audio_processing.spleeter_utils import split_audio
from audio_processing.pydub_utils import synthesize_audio
from audio_processing.magenta_utils import generate_music

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# 音頻暫存目錄
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_audio():
    file = request.files['audio']
    if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        return jsonify({"status": "success", "file_path": file_path})
    return jsonify({"status": "error"})

@app.route('/split', methods=['POST'])
def split():
    data = request.json
    file_path = data.get('file_path')
    if file_path:
        output_path = split_audio(file_path)
        return jsonify({"status": "success", "output_path": output_path})
    return jsonify({"status": "error"})

@app.route('/synthesize', methods=['POST'])
def synthesize():
    data = request.json
    file_paths = data.get('file_paths')
    if file_paths:
        output_path = synthesize_audio(file_paths)
        return jsonify({"status": "success", "output_path": output_path})
    return jsonify({"status": "error"})

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    file_path = data.get('file_path')
    if file_path:
        output_path = generate_music(file_path)
        return jsonify({"status": "success", "output_path": output_path})
    return jsonify({"status": "error"})

if __name__ == '__main__':
    socketio.run(app, debug=True)
