from spleeter.separator import Separator
import os

def split_audio(file_path):
    separator = Separator('spleeter:2stems')
    output_folder = os.path.join("output", os.path.splitext(os.path.basename(file_path))[0])
    os.makedirs(output_folder, exist_ok=True)
    separator.separate_to_file(file_path, output_folder)
    return output_folder
