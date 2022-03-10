# Save all videos to be converted in one single directory
# Save this script in that directory and run this script from that directory
# Make sure you open terminal/command prompt in same directory


import moviepy.editor as mp
import os
from pathlib import Path

path = "E:\Gitamrit_Bindu_Hindi_360p" #path where all the videos are stored
files = os.listdir(path)
#print(files)

for file in files:
    print(file)
    if(file[-4:] == '.mp4'):
        clip = mp.VideoFileClip(file)
        clip.audio.write_audiofile(Path(file).stem + ".mp3")