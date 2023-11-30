import cv2
import pygame
import numpy as np
import glob
from flask import Flask, request, jsonify
import threading

# pygame setup
pygame.init()
fullscreen = False  # Flag to indicate if the screen is in fullscreen mode
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN if fullscreen else 0)
clock = pygame.time.Clock()
running = True

file_list = glob.glob('./movies/*.mov')
mov_files = [file for file in file_list if file.endswith('.mov')]

print(mov_files)

cap = cv2.VideoCapture(mov_files[0])  # Use the first file in the list
playing = False  # Flag to indicate if video is playing

pygame.mouse.set_visible(False)  # Hide the mouse cursor

# Flask setup
app = Flask(__name__)
# app.run(port=8000, debug=True)


@app.route('/mines', methods=['POST'])
def handle_post_request():
    data = request.get_json()
    print(data)
    pygame.event.post(pygame.event.Event(pygame.USEREVENT, data=data))  # Send 'data' to pygame loop
    sensor_value = data.get('sensor')
    if sensor_value is not None:
        # Do something with the sensor value
        print(f"Received sensor value: {sensor_value}")
    return jsonify(success=True)

@app.route("/", methods=['GET'])
def hello_world():
    return "<p>Hello, World!</p>"

def run_flask_app():
    app.run(port=8000, debug=True, use_reloader=False)

if __name__ == "__main__":
    # Start Flask app in a separate thread
    flask_thread = threading.Thread(target=run_flask_app)
    flask_thread.start()

    print("Starting main loop")
    # Main game loop
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cap.release()
                cv2.destroyAllWindows()
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:                                
                    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Go back to frame 0
                    playing = True  # Start playing the video
                if event.key == pygame.K_ESCAPE:                                
                    pygame.quit()
                    playing = False  # Start playing the video
                if event.key == pygame.K_f:
                    fullscreen = not fullscreen  # Toggle fullscreen mode
                    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN if fullscreen else 0)
            if event.type == pygame.USEREVENT:
                data = event.data
                # Process 'data' received from Flask app
                print(f"Received data from Flask app: {data}")

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
        
        # RENDER YOUR GAME HERE
        if playing:
            ret, frame = cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = np.rot90(frame)

                frame = pygame.surfarray.make_surface(frame)

                window_center = (screen.get_width() // 2, screen.get_height() // 2)
                frame_pos = (window_center[0] - frame.get_width() // 2, window_center[1] - frame.get_height() // 2)

                screen.blit(frame, frame_pos)
                pygame.display.update()
        
        # flip() the display to put your work on screen
        pygame.display.flip()
        # Clean up GPIO
        
        clock.tick(60)  # limits FPS to 60

    # GPIO.cleanup()
    pygame.quit()

