import os
video_name = os.listdir("output")
for item in video_name:
    print("output/"+item,item.split("@")[0])