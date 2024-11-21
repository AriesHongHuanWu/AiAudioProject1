from pydub import AudioSegment
import os

def synthesize_audio(file_paths):
    combined = None
    for file_path in file_paths:
        audio = AudioSegment.from_file(file_path)
        combined = audio if combined is None else combined.overlay(audio)
    output_path = "output/synthesized_audio.wav"
    combined.export(output_path, format="wav")
    return output_path
