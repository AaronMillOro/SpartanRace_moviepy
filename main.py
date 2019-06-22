"""
Script used for editing the videos from the Spartan Race 2019 Andorra.
Videos size ranged between 15 Mb to 1.4 Gb.
To do so I used the library 'moviepy'
Documentation is available at:
https://zulko.github.io/moviepy/index.html
"""
import numpy as np
from moviepy.editor import *
from moviepy.editor import VideoFileClip as vfc
import moviepy.video.fx.all as vfx

#/////////////// Arrival to Encamp (all in black and white) ///////////////
# Clips are loaded and cut into ligther pieces with adapted speed
clip0 = vfc("vid/20180101_041209A.mp4").subclip(0,12).resize(0.3).speedx(1.4)
clip1 = vfc("vid/20180101_041621A.mp4").subclip(9,18).resize(0.3).speedx(1.4)
clip2 = vfc("vid/20180101_042045A.mp4").subclip(0,14).resize(0.3).speedx(1.3)
clip3 = vfc("vid/20180101_043802A.mp4").subclip(0,17).resize(0.3).speedx(1.3)
clip4 = vfc("vid/20180101_044536A.mp4").subclip(0,25).resize(0.3).speedx(1.5)
#//////////// Start SpartanRace Andorra 2019 ////////////
clip5 = vfc("vid/20180101_044536A.mp4").subclip(30,36).resize(0.3).speedx(0.6)
clip6 = vfc("vid/20180101_044536A.mp4").subclip(56,68).resize(0.3).speedx(1.2)
clip7 = vfc("vid/20180101_044919A.mp4").subclip(1,9).resize(0.3)
clip8 = vfc("vid/20180101_045035A.mp4").subclip(13,22).resize(0.3).speedx(1.3)
#//////////// Obstacles ////////////

#//////////// End of Race ////////////

videos_batch1 = [clip0, clip1, clip2, clip3, clip4]
videos_batch2 = [clip5, clip6, clip7, clip8]

entry = []
# Some videos will be produced into black/white
for video in videos_batch1:
    entry.append(video.fx( vfx.blackwhite))

for video in videos_batch2:
    entry.append(video)

# Optional preview
# entry.preview()

final = concatenate_videoclips(entry)

final.write_videofile("Spartans2019.mp4", codec = "mpeg4", fps=60)
