import cv2
import os
import streamlink
from livescore import Livescore

url = 'http://www.twitch.tv/firstwa_blue'

# Create new Livescore instance
frc = Livescore()

# Create new read from stream
streams = streamlink.streams(url)
stream = streams['best'] # Will crash if stream is not live
fname = 'read.mpg'
vid_file = open(fname, 'wb')

# Buffer video
fd = stream.open()
for i in range(0, 256):
    new_bytes = fd.read(1024)
    vid_file.write(new_bytes)

# Close video file
vid_file.close()

# Read frame from buffer
cam = cv2.VideoCapture(fname)
ret, img = cam.read()

# Analyse frame for score info
score_data = frc.read(img)

# Display score info
print score_data
cv2.imshow('Livestream', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Remove video file
os.remove(vid_file.name)
