#!/usr/bin/python3
import pygame

pygame.init();
image = "mario.png"
screen = pygame.display.set_mode((1280, 720), 0, 32)
background = pygame.image.load(image).convert()


screen.blit(background, (0,0))

pygame.display.update()

import time
time.sleep(2)

print("end")