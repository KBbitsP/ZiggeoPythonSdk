import os, sys
import json
import time


dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from Ziggeo import Ziggeo

if(len(sys.argv) < 4):
	print("Error\n")
	print("Usage: $>python videos_delete.py YOUR_APP_TOKEN YOUR_PRIVATE_KEY VIDEO_TOKEN\n")
	sys.exit()

app_token = sys.argv[1]
private_key = sys.argv[2]
video_list = json.loads(sys.argv[3])

print("Deleting tokens: " + str(video_list))

ziggeo = Ziggeo(app_token, private_key)

for video in video_list:
	print("Deleting Video: " + str(video))	
	ziggeo.videos().delete(video)
	time.sleep(100)