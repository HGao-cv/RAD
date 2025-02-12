import shutil
import os
dirs = os.listdir(".")
for path in dirs:
    if path == "output":
        continue
    _path = "save"
    video_path = os.path.join(path,_path,"it1200-test.mp4")
    out_video_path = os.path.join(output,path+".mp4")
    try:
        shutil.copy2(video_path,out_video_path)
    except:
        print(video_path,"not exists")