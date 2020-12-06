#This plays some fireplace video or something

from omxplayer.player import OMXPlayer
from pathlib import Path

fireplace_video = OMXPlayer('/home/pi/Digital-Fireplace/fireplace_vid', args=['--loop'])