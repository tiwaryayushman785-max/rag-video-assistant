#converts the video to mp3
import os 
import subprocess
file = os.listdir("video")
for files in file:
    #tutorial_name=files.split("[")[0].split(" #")[1] 
    file_name =files.split(" | ")[0]
    print(file_name)
    subprocess.run(["ffmpeg", "-i", f"video/{files}", f"audio/{file_name}.mp3"])