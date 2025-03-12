import whisper

def transcribe_audio(audio_path: str) -> str:
    """Transcribes audio content using OpenAI Whisper."""
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result['text']
