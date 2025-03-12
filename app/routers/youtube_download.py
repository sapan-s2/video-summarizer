from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from pytube import YouTube
import os

# Request model
class YouTubeURL(BaseModel):
    url: str

router = APIRouter()

@router.post("/download/")
async def download_youtube_video(request: YouTubeURL):
    """Downloads a YouTube video and saves it to the server."""
    try:
        yt = YouTube(request.url)
        stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
        if not os.path.exists("downloaded_videos"):
            os.makedirs("downloaded_videos")
        file_path = os.path.join("downloaded_videos", f"{yt.title}.mp4")
        stream.download(output_path="downloaded_videos", filename=f"{yt.title}.mp4")
        return {"message": "Video downloaded successfully!", "file_path": file_path}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error downloading video: {str(e)}")
