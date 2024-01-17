# No loops means it won't loop the videos when it hits the end of the queue.

import os
import time
import ffmpeg

# Replace 'YOUR_STREAM_KEY' with your actual YouTube Live stream key
STREAM_KEY = 'YOUR_STREAM_KEY'
VIDEO_FOLDER_PATH = 'path\\to\\folder'

def get_video_format(video_path):
    _, ext = os.path.splitext(video_path)
    return ext.lower()[1:] 

def stream_video(video_path):
    stream_url = f'rtmp://a.rtmp.youtube.com/live2/{STREAM_KEY}'

    video_format = get_video_format(video_path)

    if video_format not in ['flv', 'mov', 'mp4']:
        print(f"Unsupported format: {video_format}")
        return

    # Da encoder yeahhhh
    command = [
        'ffmpeg',
        '-re',
        '-i', video_path,
        '-c:v', 'h264',
        '-preset', 'ultrafast',
        '-b:v', '1500k',
        '-s', '1280x720',
        '-r', '30',
        '-c:a', 'aac',
        '-ar', '44100',
        '-b:a', '320k',
        '-f', 'flv',  # Dont change if you want to fuck up the output feed.
        stream_url
    ]

    os.system(' '.join(command))

def main():
    video_files = [f for f in os.listdir(VIDEO_FOLDER_PATH) if f.lower().endswith(('.flv', '.mov', '.mp4'))]
    for video_file in video_files:
        video_path = os.path.join(VIDEO_FOLDER_PATH, video_file)
        stream_video(video_path)
        time.sleep(0)  # Set the sleep time to 0 for minimal delay

if __name__ == '__main__':
    main()
