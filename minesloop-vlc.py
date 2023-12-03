import RPi.GPIO as GPIO
import vlc
import sys
import tty
import termios
import os
import vlc



BUTTON_PIN = 40
player = None
fullscreen = False

def check_sensor_state():
    return GPIO.input(BUTTON_PIN) == GPIO.LOW # normal state : no people activity

def play_video(media):
    # You need to call "set_media()" to (re)load a video before playing it
    player.set_media(media)
    player.set_fullscreen(fullscreen)  # Set fullscreen mode
    # player.play()

def main():
    # GPIO init
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # Create a new VLC instance and media player:
    #
    # This could be done in one line using vlc.MediaPlayer()
    # that will create an instance behind the scene
    # but we will pass some parameters to the instance in future example codes
    # instance = vlc.Instance()
    # player = instance.media_player_new()
    global player
    player = vlc.MediaPlayer()
    # Create libVLC objects representing the videos
    movie_directory = './movies'
    movies = []
    # Get a list of all files in the movie directory
    files = os.listdir(movie_directory)
    # Filter out non-movie files
    movie_files = [file for file in files if file.endswith('.mp4')]
    # separete file named black.mp4
    movie_files = [file for file in movie_files if file != 'black.mp4']

    # Create VLC media objects for each movie file
    for movie_file in movie_files:
        movie_path = os.path.join(movie_directory, movie_file)
        movie = vlc.Media(movie_path)
        movies.append(movie)

    black = vlc.Media(os.path.join(movie_directory, 'black.mp4'))
    
    # Start the player for the first time
    play_video(black)
    current_video = 0
    player.play()

    # TODO: Add some error handling or at least a proper Ctrl-C handler
    while True:
        # triggered = check_sensor_state()
        # print("Triggered: {}".format(triggered))
        # Stop playback if triggered and current video is video1
        # if triggered and current_video == 0:
        #     play_video(player, movies[1])
        #     player.play()

        if player.get_state() == vlc.State.Ended:
            current_video += 1
            if current_video >= len(movies):
                current_video = 0
            play_video(player, movies[current_video])
            player.play()
            # player.stop()

if __name__ == '__main__':
    main()