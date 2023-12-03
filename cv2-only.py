import cv2

def play_video(video_path):
    # Open the video file
    video = cv2.VideoCapture(video_path)

    # Check if the video file was successfully opened
    if not video.isOpened():
        print("Error opening video file")
        return

    # Get the width and height of the video frames
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Create a fullscreen window
    cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("Video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while True:
        # Read a frame from the video
        ret, frame = video.read()

        # If the frame was not successfully read, then we have reached the end of the video
        if not ret:
            break

        # Display the frame
        cv2.imshow("Video", frame)

        # Wait for the 'q' key to be pressed to exit the video playback
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video file and close the window
    video.release()
    cv2.destroyAllWindows()

# Example usage
video_path = "./movies/test.mp4"
play_video(video_path)
