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


def edit_clips():
    #///// Audio ////
    audio_1 = AudioFileClip("music/illitheas_last_forever.mp3")
    audio_2 = AudioFileClip("music/kyau-albert-trace-driftmoon.mp3")
    audio_3 = AudioFileClip("music/manuel-rocca-illitheas-enchanted.mp3")

    # Clips are loaded and cut into ligther pieces with variable speed
    #//////// Arrival to Encamp  ////////////
    clip0 = vfc("vid/20180101_041209A.mp4").subclip(0,12).resize(0.5).speedx(1.5)
    clip1 = vfc("vid/20180101_041621A.mp4").subclip(9,18).resize(0.5).speedx(1.3)
    clip2 = vfc("vid/20180101_042045A.mp4").subclip(0,14).resize(0.5).speedx(1.3)
    clip3 = vfc("vid/20180101_043802A.mp4").subclip(0,17).resize(0.5).speedx(1.3)
    clip4 = vfc("vid/20180101_044536A.mp4").subclip(0,25).resize(0.5).speedx(1.5)
    #//////////// Start SpartanRace Andorra 2019 ////////////
    clip5 = vfc("vid/20180101_044536A.mp4").subclip(30,36).resize(0.5).speedx(0.7)
    clip6 = vfc("vid/20180101_044536A.mp4").subclip(56,68).resize(0.5).speedx(1.3)
    clip8 = vfc("vid/20180101_045035A.mp4").subclip(13,22).resize(0.5).speedx(1.5)
    #//////////// Obstacles ////////////
    clip9 = vfc("vid/20180101_050013A.mp4").subclip(2,18).resize(0.5).speedx(1.5)
    clip10 = vfc("vid/20180101_050013A.mp4").subclip(28,39).resize(0.5).speedx(1.5)
    clip11 = vfc("vid/20180101_050058A.mp4").subclip(0,21).resize(0.5).speedx(1.5)
    clip12 = vfc("vid/20180101_051248A.mp4").subclip(0,52).resize(0.5).speedx(2)
    clip13 = vfc("vid/20180101_051646A.mp4").subclip(18,62).resize(0.5).speedx(2)
    clip15 = vfc("vid/20180101_052622A.mp4").subclip(5,16).resize(0.5).speedx(1.3)
    clip16 = vfc("vid/20180101_053101A.mp4").subclip(5,17).resize(0.5).speedx(1.5)
    clip17 = vfc("vid/20180101_053350A.mp4").subclip(12,120).resize(0.5).speedx(2.3)
    clip18 = vfc("vid/20180101_054430A.mp4").subclip(19,75).resize(0.5).speedx(2.5)
    clip19 = vfc("vid/20180101_054956A.mp4").subclip(29,35).resize(0.5).speedx(1.3)
    clip20 = vfc("vid/20180101_054956A.mp4").subclip(49,59).resize(0.5).speedx(1.3)
    clip21 = vfc("vid/20180101_054956A.mp4").subclip(75,85).resize(0.5).speedx(1.3)
    clip22 = vfc("vid/20180101_055451A.mp4").subclip(39,75).resize(0.5).speedx(1.3)
    clip24 = vfc("vid/20180101_060051A.mp4").subclip(6,10).resize(0.5).speedx(1.2)
    clip25 = vfc("vid/20180101_060813A.mp4").subclip(6,13).resize(0.5).speedx(1.3)
    clip26 = vfc("vid/20180101_060813A.mp4").subclip(128,135).resize(0.5).speedx(1.3)
    clip27 = vfc("vid/20180101_060813A.mp4").subclip(143,150).resize(0.5).speedx(1.3)
    clip28 = vfc("vid/20180101_060813A.mp4").subclip(157,164).resize(0.5).speedx(1.3)
    clip29 = vfc("vid/20180101_061348A.mp4").subclip(64,115).resize(0.5).speedx(1.3)
    clip30 = vfc("vid/20180101_062243A.mp4").subclip(13,18).resize(0.5).speedx(0.7)
    clip31 = vfc("vid/20180101_062243A.mp4").subclip(48,53).resize(0.5).speedx(0.7)
    clip32 = vfc("vid/20180101_062243A.mp4").subclip(70,75).resize(0.5).speedx(0.7)
    clip33 = vfc("vid/20180101_062243A.mp4").subclip(75,77).resize(0.5).speedx(2)
    clip34 = vfc("vid/20180101_062843A.mp4").subclip(23,40).resize(0.5).speedx(1.3)
    clip35 = vfc("vid/20180101_062843A.mp4").subclip(72,86).resize(0.5).speedx(1.3)
    clip36 = vfc("vid/20180101_063133A.mp4").subclip(65,85).resize(0.5).speedx(1.3)
    clip37 = vfc("vid/20180101_064043A.mp4").subclip(0,9).resize(0.5).speedx(1.3)
    clip38 = vfc("vid/20180101_064043A.mp4").subclip(25,38).resize(0.5).speedx(1.3)
    clip40 = vfc("vid/20180101_064351A.mp4").subclip(34,110).resize(0.5).speedx(1.3)
    clip41 = vfc("vid/20180101_064659A.mp4").subclip(14,34).resize(0.5).speedx(1.3)
    clip42 = vfc("vid/20180101_064830A.mp4").subclip(14,30).resize(0.5).speedx(1.3)
    clip43 = vfc("vid/20180101_064924A.mp4").subclip(4,67).resize(0.5).speedx(1.5)
    clip44 = vfc("vid/20180101_002037A.mp4").subclip(7,120).resize(0.5).speedx(1.5)
    clip45 = vfc("vid/20180101_002409A.mp4").resize(0.5).speedx(1.3)
    clip47 = vfc("vid/20180101_002756A.mp4").subclip(14,180).resize(0.5).speedx(1.3)
    clip48 = vfc("vid/20180101_003543A.mp4").subclip(22,60).resize(0.5).speedx(1.3)
    clip49 = vfc("vid/20180101_003914A.mp4").subclip(19,29).resize(0.5).speedx(1.3)
    clip50 = vfc("vid/20180101_011722A.mp4").subclip(60,71).resize(0.5).speedx(1.3)

    #//////////// Burpees and slow motion videos !!! ////////////
    clip7s = vfc("vid/20180101_044919A.mp4",fps_source='fps').subclip(0,9).resize(0.5)
    clip14s = vfc("vid/20180101_051954A.mp4",fps_source='fps').subclip(6,21).resize(0.5)
    clip23s = vfc("vid/20180101_055757A.mp4",fps_source='fps').subclip(9,25).resize(0.5)
    clip39s = vfc("vid/20180101_064244A.mp4",fps_source='fps').resize(0.5)
    # Parameter  fps_source='fps' is important for importing slow-motion videos
    #//////////// End of Race ////////////
    clip51 = vfc("vid/20180101_012219A.mp4").subclip(3,43).resize(0.5).speedx(1.3)

    multi_25_28 = clips_array([[clip25, clip26],[clip27, clip28]]).resize(0.8)
    print('Clips array created !')
    multi_30_32 = clips_array([[clip32, clip30],[clip31, clip32]]).resize(0.8)
    print('Clips array created !')

    videos_batch1 = [clip0, clip1, clip2, clip3, clip4]
    videos_batch2 = [
                     clip5, clip6, clip7s, clip8, clip9, clip10, clip11, clip12,
                     clip13, clip14s, clip15, clip16, clip17, clip18, clip19,
                     clip20, clip21, clip22, clip23s, clip24
                    ]
    videos_batch3 = [
                     clip33, clip33, clip33, clip33, clip34,
                     clip35, clip36, clip37, clip38, clip39s,
                     clip40, clip41, clip42, clip43, clip44,
                     clip45, clip47, clip48, clip49, clip50, clip51
                    ]

    # Some videos will be produced in black/white
    entry = []
    for video in videos_batch1:
        entry.append(video.fx(vfx.blackwhite))

    for video in videos_batch2:
        entry.append(video)

    entry.append(multi_25_28)
    entry.append(clip29)
    entry.append(multi_30_32)

    for video in videos_batch3:
        entry.append(video)

    final_audio = concatenate_audioclips([audio_1, audio_2,audio_3])
    final = concatenate_videoclips(entry, method="compose")
    final_vid = final.without_audio().set_audio(final_audio.set_duration(880))
    final_vid.resize(width=360)
    final_vid.write_videofile("Spartans2019.mov", codec="libx264", fps=60)


if __name__ == '__main__':
    edit_clips()
