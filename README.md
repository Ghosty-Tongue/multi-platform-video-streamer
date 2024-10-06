Multi-Platform Video Streamer

This Python script enables you to stream videos from a local folder to multiple platforms like YouTube, Twitch, and Kick using FFmpeg. You can also manage your stream keys through an interactive GUI and choose to loop videos during the stream.

Features

Stream videos directly from a folder to YouTube, Twitch, and Kick.

Easily manage stream keys via a graphical user interface (GUI).

Option to loop the videos during the stream.

Start, stop, and pause streaming from the GUI.


Requirements

FFmpeg installed on your system.

Python 3.x with the tkinter library (comes pre-installed with most Python distributions).


How to Use

1. Clone the repository:

git clone https://github.com/ghosty-tongue/multi-platform-video-streamer.git


2. Configure your stream keys:

The script looks for a stream_keys.json file where your YouTube, Twitch, and Kick stream keys will be stored.

If the file does not exist, you will be prompted to add your stream keys through the GUI.



3. Add your video files to the specified folder.


4. Run the script to manage and start streaming:

python main.py



GUI Options

Start Stream: Starts the stream and prompts whether you want to loop the videos.

Stop Stream: Stops the ongoing stream.

Pause Stream: Temporarily halts the stream, with an option to resume.


Stream Keys Configuration

The stream_keys.json file is where your platform-specific stream keys are stored in the following format:

{
  "youtube": "YOUR_YOUTUBE_STREAM_KEY",
  "twitch": "YOUR_TWITCH_STREAM_KEY",
  "kick_url": "YOUR_KICK_STREAM_URL",
  "kick_key": "YOUR_KICK_STREAM_KEY"
}

If this file is missing, the script will prompt you to add the keys through a GUI.

Advanced Customization

Video Folder: You can modify the default video folder path by updating the VIDEO_FOLDER_PATH in the script.

Supported Formats: The script supports MP4, MKV, FLV, and MOV video formats. You can adjust this by editing the SUPPORTED_FORMATS list.


License

This project is licensed under the MIT License. See the LICENSE file for details.
