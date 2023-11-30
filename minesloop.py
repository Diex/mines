# Example file showing a basic pygame "game loop"
import cv2
import pygame
import numpy as np
import glob

# pygame setup
pygame.init()
pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screen = pygame.display.get_surface()
clock = pygame.time.Clock()
running = True


file_list = glob.glob('./movies/*.mov')
mov_files = [file for file in file_list if file.endswith('.mov')]

print(mov_files)

cap = cv2.VideoCapture(mov_files[0])  # Use the first file in the list
playing = False  # Flag to indicate if video is playing

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cap.release()
            cv2.destroyAllWindows()
            # running = False
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:                                
                    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Go back to frame 0
                    playing = True  # Start playing the video


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

    clock.tick(60)  # limits FPS to 60

pygame.quit()