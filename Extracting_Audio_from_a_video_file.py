#Import packages - moviepy
#Code by Ishaq

import moviepy.editor

from tkinter.filedialog import *

#Making the user to select a file from his device.
Input_video_file = askopenfilename()

#Using a variable the video file is offically declared for a variable 
video_file = moviepy.editor.VideoFileClip(Input_video_file)

#Extracting the audio from video 
audio = video_file.audio

#Declaring a name for the audio file extracted
audio.write_audiofile("Sample file.mp3")

print("Completed extracting the audio")
