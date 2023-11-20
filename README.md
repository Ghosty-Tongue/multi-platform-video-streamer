# YouTube Folder Streamer

This Python script enables easy streaming of videos from a local folder directly to YouTube Live using FFmpeg.

## Features

- Stream videos from a specified folder to YouTube Live.
- Configurable settings for video quality and audio bitrate.
- Automatic handling of supported video formats.

## Prerequisites

- [FFmpeg](https://ffmpeg.org/) installed on your system.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/ghosty-tongue/youtube-folder-streamer.git
    ```

2. Set your YouTube Live stream key in the `main.py` file:

    ```python
    # Replace 'YOUR_STREAM_KEY' with your actual YouTube Live stream key
    STREAM_KEY = 'YOUR_STREAM_KEY'
    ```

3. Place your video files in the specified folder (`videos/` by default).

4. Run the script to start streaming:

    ```bash
    python main.py
    ```

## Configuration

Edit the `main.py` file to configure stream settings such as video quality, audio bitrate, and more.

## Advanced Usage

- You can customize the video folder path by modifying the `VIDEO_FOLDER_PATH` variable in the script.
- Adjust other settings in the script based on your preferences.

## Contribution

Feel free to contribute, report issues, or enhance the script based on your requirements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
