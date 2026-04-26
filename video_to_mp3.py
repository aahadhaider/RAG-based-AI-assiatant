## convert the videos into mp3
import os
import subprocess
files=os.listdir("videos")
print(files)
for file in files:
    print(file)
    tutorial_number=file.split(".")[0]
    print(tutorial_number)
    file_name=file.split(".")[1]
    print(file_name)
    subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios/{tutorial_number}_{file_name}.mp3"])
