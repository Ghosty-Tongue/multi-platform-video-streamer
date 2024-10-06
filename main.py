import os
import time
import json
import subprocess
import tkinter as tk
from tkinter import messagebox

STREAM_KEYS_FILE = 'stream_keys.json'
VIDEO_FOLDER_PATH = 'path/to/folder'
SUPPORTED_FORMATS = ['mp4', 'mkv', 'flv', 'mov']

paused = False
process = None

def get_video_format(video_path):
    _, ext = os.path.splitext(video_path)
    return ext.lower()[1:]

def load_stream_keys():
    try:
        with open(STREAM_KEYS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        messagebox.showerror("Error", f"{STREAM_KEYS_FILE} not found! Please add your stream keys.")
        return {}

def save_stream_keys(stream_keys):
    with open(STREAM_KEYS_FILE, 'w') as f:
        json.dump(stream_keys, f, indent=4)

def stream_video(video_path, stream_keys, loop=False):
    global process
    command = [
        'ffmpeg', '-re', '-nostdin', '-i', video_path,
        '-c:v', 'libx264', '-preset', 'ultrafast', '-minrate', '3000k', '-maxrate', '3000k', '-bufsize', '3000k',
        '-g', '30', '-c:a', 'aac', '-ar', '44100', '-b:a', '128k', '-vf', 'scale=1920:1080', '-r', '30',
        '-f', 'tee'
    ]

    streams = []
    if stream_keys.get('youtube'):
        streams.append(f"[f=flv:onfail=ignore]rtmp://a.rtmp.youtube.com/live2/{stream_keys['youtube']}")
    if stream_keys.get('twitch'):
        streams.append(f"[f=flv:onfail=ignore]rtmp://live-lax.twitch.tv/app/{stream_keys['twitch']}")
    if stream_keys.get('kick_url') and stream_keys.get('kick_key'):
        streams.append(f"[f=flv:onfail=ignore]{stream_keys['kick_url']}/app/{stream_keys['kick_key']}")

    if streams:
        tee_targets = '|'.join(streams)
        command.append(f'"{tee_targets}"')

        if loop:
            command.extend(['-stream_loop', '-1'])

        try:
            process = subprocess.Popen(' '.join(command), shell=True)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start streaming: {e}")

def edit_stream_keys():
    def save_keys():
        stream_keys = {
            'youtube': youtube_entry.get(),
            'twitch': twitch_entry.get(),
            'kick_url': kick_url_entry.get(),
            'kick_key': kick_key_entry.get()
        }
        save_stream_keys(stream_keys)
        messagebox.showinfo("Saved", "Stream keys have been saved successfully!")
        window.destroy()

    def stop_stream():
        global process
        if process:
            process.terminate()
        window.quit()

    def pause_stream():
        global paused, process
        if process and not paused:
            process.terminate()
            paused = True
            pause_button.config(text="Resume Stream")
        elif paused:
            paused = False
            pause_button.config(text="Pause Stream")
            start_streaming()

    def start_stream():
        loop = ask_loop_videos()
        start_streaming(loop)

    stream_keys = load_stream_keys()

    window = tk.Tk()
    window.title("Edit Stream Keys")

    tk.Label(window, text="YouTube Stream Key:").grid(row=0, column=0, padx=10, pady=5)
    youtube_entry = tk.Entry(window, width=40)
    youtube_entry.insert(0, stream_keys.get('youtube', ''))
    youtube_entry.grid(row=0, column=1)

    tk.Label(window, text="Twitch Stream Key:").grid(row=1, column=0, padx=10, pady=5)
    twitch_entry = tk.Entry(window, width=40)
    twitch_entry.insert(0, stream_keys.get('twitch', ''))
    twitch_entry.grid(row=1, column=1)

    tk.Label(window, text="Kick Stream URL:").grid(row=2, column=0, padx=10, pady=5)
    kick_url_entry = tk.Entry(window, width=40)
    kick_url_entry.insert(0, stream_keys.get('kick_url', ''))
    kick_url_entry.grid(row=2, column=1)

    tk.Label(window, text="Kick Stream Key:").grid(row=3, column=0, padx=10, pady=5)
    kick_key_entry = tk.Entry(window, width=40)
    kick_key_entry.insert(0, stream_keys.get('kick_key', ''))
    kick_key_entry.grid(row=3, column=1)

    save_button = tk.Button(window, text="Save", command=save_keys)
    save_button.grid(row=4, column=0, columnspan=2, pady=10)

    start_button = tk.Button(window, text="Start Stream", command=start_stream, fg='green')
    start_button.grid(row=5, column=0, padx=10, pady=10)

    stop_button = tk.Button(window, text="Stop Stream", command=stop_stream, fg='red')
    stop_button.grid(row=5, column=1, padx=10, pady=10)

    global pause_button
    pause_button = tk.Button(window, text="Pause Stream", command=pause_stream)
    pause_button.grid(row=6, column=0, columnspan=2, pady=10)

    window.mainloop()

def ask_loop_videos():
    result = messagebox.askyesno("Loop Videos", "Do you want to loop the videos?")
    return result

def main(loop=False):
    stream_keys = load_stream_keys()

    if not stream_keys:
        edit_stream_keys()
        stream_keys = load_stream_keys()

    while True:
        video_files = [f for f in os.listdir(VIDEO_FOLDER_PATH) if get_video_format(f) in SUPPORTED_FORMATS]

        if not video_files:
            break

        for video_file in video_files:
            video_path = os.path.join(VIDEO_FOLDER_PATH, video_file)
            stream_video(video_path, stream_keys, loop)
            time.sleep(0)

def start_streaming(loop=False):
    main(loop)

if __name__ == '__main__':
    edit_stream_keys()
