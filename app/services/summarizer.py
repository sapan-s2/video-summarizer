from app.services.video_processor import extract_keyframes
from app.utils.helpers import extract_audio
from app.utils.transcription import transcribe_audio
from app.utils.text_summarization import summarize_transcript

def summarize_video(file_path: str) -> dict:
    """
    Summarizes the video content by extracting keyframes.

    Args:
        file_path (str): Path to the video file.

    Returns:
        dict: Summary with keyframe paths and placeholder text.
    """
    from app.services.video_processor import extract_keyframes

    output_dir = "keyframes"
    keyframes = extract_keyframes(file_path, output_dir)

    # Placeholder fo    r AI-powered content summarization
    summary_text = "The video contains key scenes at the extracted frames."
    print("summary-text", summary_text)
    print("keyframes", keyframes)
    return {
        "summary_text": summary_text,
        "keyframes": keyframes
    }

def generate_text_summary(file_path: str) -> str:
    """
    Extracts a textual summary of the video by transcribing its audio and summarizing the transcript.
    """
    # Example logic for extracting audio, transcribing, and summarizing
    audio_path = extract_audio(file_path)
    print("auddio pathextracted : ",audio_path)
    transcript = transcribe_audio(audio_path)
    summary = summarize_transcript(transcript)
    print("summary : ",summary)
    return summary
