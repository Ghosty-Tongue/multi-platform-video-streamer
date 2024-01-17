import os
import time
import ffmpeg

STREAM_KEY = 'YOUR_STREAM_KEY'
VIDEO_FOLDER_PATH = 'path\\to\\folder'

def get_video_format(video_path):
    _, ext = os.path.splitext(video_path)
    return ext.lower()[1:]

def stream_video(video_path, loop):
    stream_url = f'rtmp://a.rtmp.youtube.com/live2/{STREAM_KEY}'

    video_format = get_video_format(video_path)

    if video_format not in ['flv', 'mov', 'mp4']:
        print(f"Unsupported format: {video_format}")
        return
        
# Comments are left on ffmpeg commands for people who don't have any knowledge on ffmpeg commands.
    command = [
        'ffmpeg',
        '-re',
        '-i', video_path,
        '-c:v', 'h264',        # Video codec  (Importent this command should not be mess with unless you know what you are doing.)
        '-preset', 'ultrafast',# Video preset for speed  (Importent this command should not be mess with unless you know what you are doing.)
        '-b:v', '1500k',       # Video bitrate  (Importent this command should not be mess with unless you know what you are doing.)
        '-s', '1280x720',      # Video resolution
        '-r', '30',            # Frame rate
        '-c:a', 'aac',         # Audio codec  (Importent this command should not be mess with unless you know what you are doing.)
        '-ar', '44100',        # Audio sample rate  (Importent this command should not be mess with unless you know what you are doing.)
        '-b:a', '320k',        # Audio bitrate  (Importent this command should not be mess with unless you know what you are doing.)
        '-f', 'flv',           # Output format (Importent this command should not be mess with unless you know what you are doing.)
        stream_url
    ]

    if loop:
        command.extend(['-stream_loop', '-1'])

    os.system(' '.join(command))

def main():
    loop_input = input("Do you want to loop the videos? (yes/no): ").lower()
    loop = loop_input == 'yes'

    while True:
        video_files = [f for f in os.listdir(VIDEO_FOLDER_PATH) if f.lower().endswith(('.flv', '.mov', '.mp4'))]

        for video_file in video_files:
            video_path = os.path.join(VIDEO_FOLDER_PATH, video_file)
            stream_video(video_path, loop)
            time.sleep(0)

if __name__ == '__main__':
    main()
