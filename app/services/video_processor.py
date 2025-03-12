import cv2
import os
import logging


def extract_keyframes(video_path: str, output_dir: str, threshold: float = 10.0):
    logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
    """
    Extracts keyframes from a video based on scene changes.

    Args:
        video_path (str): Path to the video file.
        output_dir (str): Directory to save keyframes.
        threshold (float): Scene change detection threshold.

    Returns:
        List[str]: List of file paths to extracted keyframes.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
       
        print(f"Error: Could not open video file at {video_path}.")
    else:
        print("Video file opened successfully!")

        # Check video properties
    frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    print(f"Width: {frame_width}, Height: {frame_height}, Frame Count: {frame_count}")

    # ret, frame = cap.read()
    # if not ret:
    #     print("Error: Could not read the first frame.")
    # else:
    #     print("First frame read successfully!")

    # cap.release()
    prev_frame = None
    frame_count = 0
    keyframes = []
    print(f"Initial Frame {frame_count}")
    while True:
        print(f"cap",{cap})
        ret, frame = cap.read()
        print(f"ret", {ret})
        if not ret:
            print(f"Failed to read frame {frame_count}.")
            print("break",{frame})
            break

        print(f"Frame {frame_count}, before gray scale: {frame}") 
        # Convert frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        print(f"Frame {frame_count}, gray frame: {gray_frame}")

        # Compare with the previous frame
        if prev_frame is not None:
            diff = cv2.absdiff(prev_frame, gray_frame)
            score = diff.mean()
             
            # Save keyframe if scene change detected
            if score > threshold:
                print(f"Frame {frame_count}, Change Score: {score}")
                frame_path = os.path.join(output_dir, f"keyframe_{frame_count}.jpg")
                cv2.imwrite(frame_path, frame)
                print("frames", frame)
                keyframes.append(frame_path)

        prev_frame = gray_frame
        frame_count += 1

    cap.release()
    logging.info(keyframes)
    print("keyframes extracted",keyframes)
    return keyframes
