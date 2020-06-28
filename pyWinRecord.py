# Author: David Bernal
# This simple script can be used to take multiple screenshots of the Windows desktop, that can later be added with ffmpeg.exe to generate a small mp4 video
# requires: pip install Pillow

# License: Apache license version 2
# Press Ctr + C to finish recording, then delete the last capture-n.png file and use the following command to generate the video:

# ffmpeg.exe -r 4 -f image2 -i capture-%d.png -vcodec libx264 -crf 2 -pix_fmt yuv420p video.mp4

import time
import base64
import sys
import os
from datetime import datetime

try:
	from PIL import ImageGrab
	from PIL import Image
except:
	print("Please install Pillow: pip install Pillow")
	sys.exit(1)

image = {}
strImage = ""
i = 1

sleep = 0.2

outputFolder = "pyRecord-" + str(datetime.today().strftime('%Y-%m-%d-%H-%M-%S'))
os.mkdir(outputFolder)
#sys.exit(1)

print("Start recording in two seconds")
time.sleep(2)
print("Recording... press Ctr + C when done :) and then run ffmpeg to create your minimal mp4")

try:
	while True:
		time.sleep(sleep)
		print(i)
		sourceImage = ImageGrab.grab()
		filename = "capture-" + str(i) +".png"
		sourceImage.save(outputFolder + "\\" + filename, "PNG")
		i = i + 1
except (KeyboardInterrupt,OSError):
	os.remove(outputFolder + "\\" + filename)
	
	print("Screenshots saved to: " + outputFolder)
	print("Enter that folder and run ffmpeg to generate your video by running: \"ffmpeg.exe -r 4 -f image2 -i capture-%d.png -vcodec libx264 -crf 2 -pix_fmt yuv420p video.mp4\" Tweak the -r parameter to increase or reduce speed.")
