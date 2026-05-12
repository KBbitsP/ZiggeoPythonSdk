import os
import sys
import subprocess
import json
import time

# Ziggeo setup
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from Ziggeo import Ziggeo

if len(sys.argv) < 3:
    print("Error\n")
    print("Usage: python _videos_delete_master_script.py YOUR_APP_TOKEN YOUR_PRIVATE_KEY\n")
    sys.exit()

app_token = sys.argv[1]
private_key = sys.argv[2]

ziggeo = Ziggeo(app_token, private_key)

processes = []  # To track running child processes

def indexVideos(skip=0):
    """Fetch videos in batches and spawn parallel deletion processes."""
    video_list = ziggeo.videos().index({"limit": 100, "skip": skip })
    chunk_size = 10

    if not video_list:
        return  # No more videos

    print(f"Fetched {len(video_list)} videos at skip={skip}")

    # Process chunks in parallel
    for i in range(0, len(video_list), chunk_size):
        chunk = [video["token"] for video in video_list[i:i + chunk_size]]
        if chunk:
            cmd = [
                "python",
                "videos_delete_child_script.py",
                app_token,
                private_key,
                json.dumps(chunk)  # Pass as JSON string
            ]
            print(f"Spawning deletion process for {len(chunk)} videos: {chunk}")
            proc = subprocess.Popen(cmd)
            processes.append(proc)

    # Immediately move to the next set of videos
    time.sleep(10)
    indexVideos(skip + 100)

# Start fetching and deleting
indexVideos(0)

# Wait for all child processes to complete before exiting
print("Waiting for all deletion processes to finish...")
for p in processes:
    p.wait()
print("All deletions completed.")
