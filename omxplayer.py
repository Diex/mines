from pathlib import Path
from time import sleep

VIDEO_PATH = Path("./movies/test.mov")

try:
    from omxplayer.player import OMXPlayer
except ImportError:
    print("OMXPlayer module not found. Please make sure it is installed.")
    exit(1)  # Exit the script if OMXPlayer cannot be imported

player = OMXPlayer(VIDEO_PATH)

sleep(5)

player.quit()