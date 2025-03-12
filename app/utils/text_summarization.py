from transformers import pipeline

def summarize_transcript(transcript: str) -> str:
    """Generates a natural language summary of the transcript."""
    summarizer = pipeline("summarization")
    summary = summarizer(transcript, max_length=50, min_length=10, do_sample=False)[0]['summary_text']
    return summary
