# YouTube Video Downloader

This Python script allows you to download YouTube videos and merge them with audio tracks using the `pytubefix` and `moviepy` libraries.  
The script downloads the highest resolution video and the highest bitrate audio available for a given YouTube URL, combines them, and saves the final video file.

## Requirements

Before running the script, ensure you have the following libraries installed:

- [`pytubefix`](https://pypi.org/project/pytubefix/)
- [`moviepy`](https://pypi.org/project/moviepy/)
- `os`
- `re`

If you don't have them, you can easily install the required libraries using pip and the `requirements.txt` file:

```
pip install -r requirements.txt
```
## Overview

The script performs the following steps:

1. **Function Definition**:
   - `sanitize_filename(filename: str) -> str`: this function takes a filename as input and performs the following:
     - removes the unwanted characters from the given filename using `re`
     - outputs the new filename without the unwanted characters
    
   - `download_and_merge(url: str)`: this function takes a YouTube video URL as input and performs the following:
     - creates a `YouTube` object with the provided URL and sets a progress callback.
     - filters and selects the highest resolution video stream and the highest bitrate audio stream.
     - downloads the selected video and audio streams to the current directory.
     - renames the downloaded files to temporary names for processing.
     - loads the video and audio clips using `moviepy`.
     - combines the audio with the video clip.
     - writes the final merged video file to the current directory with the title of the YouTube video.
     - cleans up by removing the temporary files.

3. **Main Execution Block**:
   - prompts the user to input a YouTube video URL.
   - calls the `download_and_merge` function with the provided URL.


## Conclusion

With this YouTube Video Downloader and Merger, you have the power to take your favorite videos offline and enjoy them anytime, anywhere **without ADS**.  
Whether you're curating a personal collection of cat videos or compiling the ultimate playlist of motivational speeches, this script is your trusty sidekick.  
Remember, the code is open for modification! Feel free to tweak it, enhance it, or even turn it into a full-fledged video editing suite.  
Just keep in mind: **with great power comes great responsibility**.  
So, while you’re free to modify the code, please don’t use it to create a 10-hour loop of your neighbor’s karaoke night—unless, of course, you’re planning to win a “Best Neighbor” award!

Happy coding!


~*That's it. That's all there is.*~
