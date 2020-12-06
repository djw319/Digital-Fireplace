#This plays some fireplace video or something

from omxplayer.player import OMXPlayer
from pathlib import Path

fireplace_video = OMXPlayer('/home/pi/Digital-Fireplace/fireplace_vid.mp4', args=['--loop'])

def main():
    while True:
        print('playing back video')
        fireplace_video.play()
        