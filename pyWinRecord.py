# Author: David Bernal
# This simple script can be used to take multiple screenshots of the Windows desktop, that can later be added with ffmpeg.exe to generate a mp4 video
# requires: pip install Pillow

# License: Apache license version 2
# Press Ctr + C to finish recording, then delete the last capture-n.png file and use the following command to generate the video:
# ffmpeg.exe -r 12 -f image2 -s 1920x1080 -i capture-%d.png -vcodec libx264 -crf 8 -pix_fmt yuv420p video.mp4

from PIL import ImageGrab
from PIL import Image
import time
import base64

image = {}
strImage = ""
i = 1

fps = 12

print "Start recording in two seconds"
time.sleep(2)
print "Recording... press Ctr + C when done :)"

while True:
    time.sleep(1/fps)
    print i
    sourceImage = ImageGrab.grab()
    sourceImage.save("capture-" + str(i) +".png", "PNG")
    i = i + 1
