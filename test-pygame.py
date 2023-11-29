import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the size of the window
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Set the title of the window
pygame.display.set_caption('Hello, World!')

# Create a font object
font = pygame.font.Font(None, 36)

# Create a text surface

text = font.render('Hello, World!', True, (0, 0, 0))

# Main event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Draw the text onto the screen
    screen.blit(text, (50, 50))

    # Update the display
    pygame.display.flip()