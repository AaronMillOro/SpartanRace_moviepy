"""
Script used for editing the videos from the Spartan Race 2019 Andorra.
Videos size ranged between 15 Mb to 1.4 Gb.
The library 'moviepy' was used.
Documentation is available at:
https://zulko.github.io/moviepy/index.html
"""
import numpy as np
from moviepy.editor import *
from moviepy.editor import VideoFileClip as vfc
import moviepy.video.fx.all as vfx

def edit_films():
    #//////// Arrival to Encamp (all in black and white) ////////////
    # Clips are loaded and cut into ligther pieces with adapted speed
    clip0 = vfc("vid/20180101_041209A.mp4").subclip(0,12).resize(0.3).speedx(1.5)
    clip1 = vfc("vid/20180101_041621A.mp4").subclip(9,18).resize(0.3).speedx(1.3)
    clip2 = vfc("vid/20180101_042045A.mp4").subclip(0,14).resize(0.3).speedx(1.3)
    clip3 = vfc("vid/20180101_043802A.mp4").subclip(0,17).resize(0.3).speedx(1.3)
    clip4 = vfc("vid/20180101_044536A.mp4").subclip(0,25).resize(0.3).speedx(1.5)
    #//////////// Start SpartanRace Andorra 2019 ////////////
    clip5 = vfc("vid/20180101_044536A.mp4").subclip(30,36).resize(0.3).speedx(0.7)
    clip6 = vfc("vid/20180101_044536A.mp4").subclip(56,68).resize(0.3).speedx(1.3)
    clip7s = vfc("vid/20180101_044919A.mp4",fps_source='fps').subclip(0,9).resize(0.3)
    clip8 = vfc("vid/20180101_045035A.mp4").subclip(13,22).resize(0.3).speedx(1.5)
    #//////////// Obstacles ////////////
    clip9 = vfc("vid/20180101_050013A.mp4").subclip(2,18).resize(0.3).speedx(1.5)
    clip10 = vfc("vid/20180101_050013A.mp4").subclip(28,39).resize(0.3).speedx(1.5)
    clip11 = vfc("vid/20180101_050058A.mp4").subclip(0,21).resize(0.3).speedx(1.5)
    clip12 = vfc("vid/20180101_051248A.mp4").subclip(0,52).resize(0.3).speedx(2.3)
    clip13 = vfc("vid/20180101_051646A.mp4").subclip(18,62).resize(0.3).speedx(3)
    clip15 = vfc("vid/20180101_052622A.mp4").subclip(5,16).resize(0.3).speedx(1.3)
    clip16 = vfc("vid/20180101_053101A.mp4").subclip(5,17).resize(0.3).speedx(1.5)
    clip17 = vfc("vid/20180101_053350A.mp4").subclip(12,120).resize(0.3).speedx(2.3)
    clip18 = vfc("vid/20180101_054430A.mp4").subclip(19,75).resize(0.3).speedx(2.5)
    clip19 = vfc("vid/20180101_054956A.mp4").subclip(29,35).resize(0.3).speedx(1.3)
    clip20 = vfc("vid/20180101_054956A.mp4").subclip(49,59).resize(0.3).speedx(1.3)
    clip21 = vfc("vid/20180101_054956A.mp4").subclip(75,85).resize(0.3).speedx(1.3)
    clip22 = vfc("vid/20180101_055451A.mp4").subclip(39,75).resize(0.3).speedx(1.3)
    clip24 = vfc("vid/20180101_060051A.mp4").subclip(6,10).resize(0.3).speedx(1.2)
    clip25 = vfc("vid/20180101_060813A.mp4").subclip(5,13).resize(0.3).speedx(1.3)
    clip26 = vfc("vid/20180101_060813A.mp4").subclip(129,135).resize(0.3).speedx(1.3)
    clip27 = vfc("vid/20180101_060813A.mp4").subclip(143,150).resize(0.3).speedx(1.3)
    clip28 = vfc("vid/20180101_060813A.mp4").subclip(157,163).resize(0.3).speedx(1.3)
    clip29 = vfc("vid/20180101_061348A.mp4").subclip(64,115).resize(0.3).speedx(1.3)

    #//////////// Burpees !!! ////////////
    clip14s = vfc("vid/20180101_051954A.mp4",fps_source='fps').subclip(6,21).resize(0.3)
    clip23s = vfc("vid/20180101_055757A.mp4",fps_source='fps').subclip(9,25).resize(0.3)
    # Parameter  fps_source='fps' is important for importing slow-motion videos
    #//////////// End of Race ////////////

    videos_batch1 = [clip0, clip1, clip2, clip3, clip4]
    videos_batch2 = [
                     clip5, clip6, clip8, clip9, clip10, clip11, clip12,
                     clip13, clip15, clip16, clip17, clip18, clip19,
                     clip20, clip21, clip22, clip24, clip25, clip26,
                     clip27, clip28, clip29
                    ]
    """
    videos_batch3 = [
                     clip24, clip25, clip26, clip27, clip28, clip29
                    ]
    """
    entry = []
    # Some videos will be produced into black/white
    for video in videos_batch1:
        entry.append(video.fx( vfx.blackwhite))

    for video in videos_batch2:
        entry.append(video)

    # Optional preview
    # entry.preview()

    final = concatenate_videoclips(entry)
    final.resize(width=100)
    final.write_videofile("Spartans2019.webm",codec="libvpx",audio=False,fps=60)
    #fps=60 , codec = libx264 for .mov

if __name__ == '__main__':
    edit_films()
