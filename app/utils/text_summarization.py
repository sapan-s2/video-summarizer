# from transformers import pipeline
import openai
from app.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def summarize_transcript(transcript: str) -> str:
    # """Generates a natural language summary of the transcript."""
    # summarizer = pipeline("summarization")
    # summary = summarizer(transcript, max_length=50, min_length=10, do_sample=False)[0]['summary_text']
    # return summary

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",  # Use the model suitable for summarization
            messages=[
                {"role": "system", "content": "You are a helpful assistant specialized in summarizing text."},
                {"role": "user", "content": f"Summarize this text: {text}"}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error during summarization: {e}"
