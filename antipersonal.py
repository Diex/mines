import cv2
import pygame
import numpy as np

def play_fullscreen():
    pygame.init()
    pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    screen = pygame.display.get_surface()

    cap = cv2.VideoCapture('./movies/test.mov')

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = np.rot90(frame)
            frame = pygame.surfarray.make_surface(frame)
            screen.blit(frame, (0,0))
            pygame.display.update()
        else:
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cap.release()
                cv2.destroyAllWindows()
                break

play_fullscreen()