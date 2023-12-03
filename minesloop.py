import pygame
import vlc
import glob

# pygame setup
pygame.init()
fullscreen = False  # Flag to indicate if the screen is in fullscreen mode
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN if fullscreen else 0)
clock = pygame.time.Clock()
running = True

file_list = glob.glob('./movies/*.mp4')
mov_files = [file for file in file_list if file.endswith('.mp4')]

print(mov_files)

instance = vlc.Instance()
player = instance.media_player_new()
media = instance.media_new(mov_files[0])
player.set_media(media)
player.play()

pygame.mouse.set_visible(False)  # Hide the mouse cursor

print("Starting main loop")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player.is_playing():
                    player.pause()
                else:
                    player.play()
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_f:
                fullscreen = not fullscreen  # Toggle fullscreen mode
                screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN if fullscreen else 0)

    screen.fill("black")  # Clear the screen

    if player.is_playing():
        frame = player.get_video_frame()
        if frame:
            frame = pygame.image.fromstring(frame.data, frame.shape[1::-1], "RGB")
            screen.blit(frame, (0, 0))  # Draw the frame at the top-left corner

    pygame.display.flip()  # Update the display
    clock.tick(30)  # Reduce the frame rate to 30 FPS

player.stop()
pygame.quit()
print("Done")
