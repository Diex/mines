import os
import pygame
import time
os.putenv('SDL_FBDEV', '/dev/fb0')
os.environ["SDL_FBDEV"] = "/dev/fb0"
pygame.mixer.pre_init(buffer=4096)
pygame.init()
lcd = pygame.display.set_mode((800, 480))
lcd.fill((0,0,0))
pygame.display.update()
pygame.draw.line(lcd, (30,80,200),[0,270],[0,319],2);
pygame.display.update()
time.sleep(5)