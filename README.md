# Python for Audio Processing
![](https://www.it-jim.com/wp-content/uploads/2021/06/Audio-processing-01-1024x240.png)
Python is a powerful language for audio processing due to its simplicity and ease of use. It provides several libraries for audio processing, including 
* wave (Inbuilt)
* [PyAudio](https://pypi.org/project/PyAudio/)
* [soundfile](https://pypi.org/project/soundfile/)
* [librosa](https://librosa.org/doc/latest/install.html)
* [Pydub](https://pypi.org/project/pydub/)

# Reading and Writing Audio Files
The first step in audio processing is reading and writing audio files. In Python, we can read and write audio files in various formats, including WAV, FLAC, and MP3.
<br><br>
#### Here’s an example of how to read an audio file using the python inbuilt <wave> library<br>
> NOTE: wave library only support read and write operations on WAV files

```python
import wave

# (constants) -----------------------
AUDIO_FILE  = "./assets/sample-9s.wav";
# ------------------------------------

# wave file object
fwav_obj  = wave.open(AUDIO_FILE, "rb"); # this will read the wav file in binary mode

# READING THE AUDIO FILE PROPERTIES
# -----------------------------------------------------------------

# Getting the number of channels in wav file
# 1 means MONO_CHANNEL
# 2 means STEREO_CHANNEL
print("Number of channels:", fwav_obj.getnchannels());

# Getting the sample width OR bytes per frame in audio
print("Sample width:", fwav_obj.getsamplewidth());

# Getting the frame rate (Number of sample frames per second)
print("Frame rate:", fwav_obj.getframerate());

# Getting total number of frames in audio
print("Number of frames:", fwav_obj.getnframes());

# READING THE CONTENT (FRAME) FROM AUDIO FILE
# -----------------------------------------------------------------

frames  = fwav_obj.readframes(-1);  # -1 denotes read the file until EOF
print(len(frames));  # Printing the total length of frame
"""
  NOTE:
    * The Length of frame is not equal to the Number of frames.
    * To get the same result we have to multiply it by sample width
"""

fwav_obj.close();  # Don't forget to close the file
```

#### Here’s an example of how to write an audio file using the python inbuilt <wave> library<br>
```python
import wave

AUDIO_FILE  = "./assets/sample-9s_new.wav";
fwav_obj  = wave.open(AUDIO_FILE, "wb");  # this will open the new ouput audio file for writing in binary mode

# SETTING THE BASIC PROPERTIES
# -----------------------------------------------------------------
fwav_obj.setnchannels(1);          # Setting the MONO channels for new audio
fwav_obj.setsamplewidth(2);        # Setting 2 bytes as sample width
fwave_obj.setframerate(44100.0);   # Setting framerate to standard CD quality rate

# WRITTING FRAMES INTO THE AUDIO FILE
# -----------------------------------------------------------------
fwav_obj.writeframes(frames);      # writing the frames into new audio file which was read above | Frames should be in bytes

fwav_obj.close();  # Closing the audio file (FOR GOOD PRACTICE AS WELL)
```
