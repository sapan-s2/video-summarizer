import os
from fastapi import FastAPI
from app.routers import video_upload, summarize, youtube_download

app = FastAPI()

port = int(os.environ.get("PORT", 8000))
# Use uvicorn to run the app when executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)

# Include routers
app.include_router(video_upload.router, prefix="/video", tags=["Video Upload"])
app.include_router(summarize.router, prefix="/video", tags=["Summarization"])
# app.include_router(youtube_download.router, prefix="/youtube", tags=["YouTube Download"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Video Summarizer API!"}
