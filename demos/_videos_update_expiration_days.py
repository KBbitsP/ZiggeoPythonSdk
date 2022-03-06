import os, sys

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from Ziggeo import Ziggeo

if(len(sys.argv) < 4):
	print("Error\n")
	print("Usage: $>python _videos_update_expiration_days.py.py YOUR_APP_TOKEN YOUR_PRIVATE_KEY VIDEO_TOKEN EXPIRATION\n")
	print "" # Expiration days are integer
	sys.exit()

app_token = sys.argv[1]
private_key = sys.argv[2]
video_token = sys.argv[3]
expiration_days = sys.argv[4]

ziggeo = Ziggeo(app_token, private_key)

arguments = {}
arguments["expiration_days"] = expiration_days

print ziggeo.videos().update(video_token, arguments)