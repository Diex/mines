import RPi.GPIO as GPIO
import vlc
import sys
import tty
import termios
import os
import vlc
import random




BUTTON_PIN = 40
player = None
fullscreen = False

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def check_sensor_state():
    return GPIO.input(BUTTON_PIN) == GPIO.HIGH # normal state : no people activity

def play_video(media):
    global player
    # You need to call "set_media()" to (re)load a video before playing it
    player.set_media(media)
    player.set_fullscreen(fullscreen)  # Set fullscreen mode
    player.play()

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
    blacks = []
    # Get a list of all files in the movie directory
    files = os.listdir(movie_directory)
    # Filter out non-movie files
    movie_files = [file for file in files if file.startswith('Minas')]
    print(movie_files)
    # Create VLC media objects for each movie file
    for movie_file in movie_files:
        movie_path = os.path.join(movie_directory, movie_file)
        movie = vlc.Media(movie_path)
        movies.append(movie)


    black_files = [file for file in files if file.startswith('black')]
    print(black_files)
    # Create VLC media objects for each black movie file
    for black_file in black_files:
        black_path = os.path.join(movie_directory, black_file)
        black = vlc.Media(black_path)
        blacks.append(black)





    
    # Start the player for the first time
    current_video = 0
    black = random.choice(blacks)
    play_video(black)
    print("playing black " + str(black) + str(player.get_length()))
    is_black = True    

    # TODO: Add some error handling or at least a proper Ctrl-C handler
    while True:
        triggered = check_sensor_state()        
        # Stop playback if triggered and current video is video1
        if triggered: 
            # Note the order of libvlc_state_t enum must match exactly the order of See mediacontrol_playerstatus, 
            # See input_state_e enums, and videolan.libvlc.state (at bindings/cil/src/media.cs). 
            # expected states by web plugins are: idle/close=0, opening=1, playing=3, paused=4, stopping=5, ended=6, error=7.
            if player.get_state() == vlc.State.Playing:
            # do nothing keep playing
                # print("playing " + str(current_video) + " state: " + str(player.get_state())+" " + str(player.get_time()) + " " + str(player.get_length()))
                pass
            elif player.get_state() == vlc.State.Paused:
                pass
            elif player.get_state() == vlc.State.Stopped:
                pass
            elif player.get_state() == vlc.State.Ended:   
                    if(is_black):
                        is_black = False
                        current_video += 1                
                        if current_video >= len(movies):
                            current_video = 0                    
                        play_video(movies[current_video])
                        print("playing " + str(current_video) + " " + str(player.get_length()))
                    else:
                        # select random black video
                        black = random.choice(blacks)
                        play_video(black)  
                        print("playing random black" + str(black) + " " + str(player.get_length()))
                        is_black = True                      
        else:            
            if player.get_state() == vlc.State.Playing:
                pass            
            elif player.get_state() == vlc.State.Ended:                
                play_video(blacks[1])
                print(" no activity playing black" + str(black) + " " + str(player.get_length()))
                is_black = True  

if __name__ == '__main__':
    main()