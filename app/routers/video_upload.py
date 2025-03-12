import logging
from fastapi import APIRouter, File, UploadFile, HTTPException
import os
from app.utils.helpers import save_file

logging.basicConfig(level=logging.INFO)

router = APIRouter()

@router.post("/upload/")
async def upload_video(file: UploadFile = File(...)):
    """Handles video uploads."""
    logging.info("file content type{file.content_type}")
    if not file.content_type.startswith("video/"):
        print("file content type",file.content_type)
        raise HTTPException(status_code=404, detail=f"Invalid file type. Please upload a video {file.content_type}")
    
    file_path = save_file(file)
    return {"message": "Video uploaded successfully!", "file_path": file_path}
