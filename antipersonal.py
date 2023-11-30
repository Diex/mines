import cv2
import pygame
import numpy as np

def play_fullscreen():
    pygame.init()
    pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    screen = pygame.display.get_surface()

    cap = cv2.VideoCapture('./movies/test.mov')

    playing = False  # Flag to indicate if video is playing

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cap.release()
                cv2.destroyAllWindows()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:                                
                    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Go back to frame 0
                    playing = True  # Start playing the video

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
play_fullscreen()

               