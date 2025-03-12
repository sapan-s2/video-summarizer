from fastapi import APIRouter, HTTPException
from app.services.summarizer import summarize_video, generate_text_summary

router = APIRouter()

@router.post("/summarize/")
async def summarize(file_path: str):
    """
    Summarizes the video content by extracting keyframes and generating a textual summary.
    """
    try:
        summary = summarize_video(file_path)
        return {"message": "Summarization successful!", "summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing video: {str(e)}")

@router.post("/summarize-text/")
async def summarize_text(file_path: str):
    """
    Extracts a textual summary of the video's audio content.
    """
    try:
        summary_text = generate_text_summary(file_path)
        return {"message": "Textual summarization successful!", "summary_text": summary_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating textual summary: {str(e)}")
