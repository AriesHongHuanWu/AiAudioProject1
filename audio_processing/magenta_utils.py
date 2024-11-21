import subprocess
import os

def generate_music(file_path):
    output_folder = "output/magenta"
    os.makedirs(output_folder, exist_ok=True)
    output_path = os.path.join(output_folder, "generated_music.wav")
    command = f"magenta-music-utility --input_file={file_path} --output_file={output_path} --model_name=melody_rnn"
    subprocess.run(command, shell=True)
    return output_path
