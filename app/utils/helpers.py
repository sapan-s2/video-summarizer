import ffmpeg
import os

UPLOAD_DIR = "uploaded_videos"

def save_file(file) -> str:
    """Saves the uploaded file and returns its path."""
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)
    
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
    
    return file_path

import ffmpeg

def extract_audio(video_path: str) -> str:
    """Extracts the audio from a video file."""
    audio_path = video_path.rsplit(".", 1)[0] + ".mp3"
    ffmpeg.input(video_path).output(audio_path).run(quiet=True, overwrite_output=True)
    return audio_path

