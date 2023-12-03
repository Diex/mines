import pygame
from ffpyplayer.player import MediaPlayer

def PlayVideo(filename):
    player = MediaPlayer(filename)
    val = ''
    while val != 'eof':
        frame, val = player.get_frame()
        screen = pygame.display.set_mode(frame.size)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.blit(pygame.image.fromstring(frame.to_bytearray()[0], frame.size, "RGB"), (0,0))
        pygame.display.update()

pygame.init()
PlayVideo('./movies/test.mp4')