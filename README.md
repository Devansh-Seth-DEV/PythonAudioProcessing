# Python for Audio Processing
![](https://www.it-jim.com/wp-content/uploads/2021/06/Audio-processing-01-1024x240.png)
Python is a powerful language for audio processing due to its simplicity and ease of use. It provides several libraries for audio processing, including 
* wave (Inbuilt)
* [PyAudio](https://pypi.org/project/PyAudio/)
* [soundfile](https://pypi.org/project/soundfile/)
* [librosa](https://librosa.org/doc/latest/install.html)
* [Pydub](https://pypi.org/project/pydub/)
<br><br>

# Reading and Writing Audio Files
![](https://images.ctfassets.net/qpn1gztbusu2/3tUrVr1yqnRx8DI33vRIVa/9bbf991463f6eb94c5d419f213a5b11a/writing-for-audio-desktop_2_.jpg?fm=avif&w=1920&q=70)
<br>
The first step in audio processing is reading and writing audio files. In Python, we can read and write audio files in various formats, including WAV, FLAC, and MP3.
<br><br>
### Here’s an example of how to read an audio file using the python inbuilt <wave> library<br>
> NOTE: wave library only support WAV files

Importing the wave library
```python
import wave
```

After importing the library we need to open the audio file for reading
```python
AUDIO_FILE  = "./assets/sample-9s.wav";

# wave file object
fwav_obj    = wave.open(AUDIO_FILE, "rb"); # this will read the wav file in binary mode
```

Now we can start reading the properties of the file
```python
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
```

To read the contents of the audio file we have to use "readframes" method
```python
frames  = fwav_obj.readframes(-1);  # -1 denotes read the file until EOF
print(len(frames));  # Printing the total length of frame
"""
  NOTE:
    * The Length of frame is not equal to the Number of frames.
    * To get the same result we have to multiply it by sample width
"""
```

Don't forget to close the file
```python
fwav_obj.close();
```
<br>

### Here’s an example of how to write an audio file using the python inbuilt <wave> library<br>
Import the wave library
```python
import wave
```

After importing the library we need to open the audio file for writing
```python
AUDIO_FILE  = "./assets/sample-9s_new.wav";
fwav_obj    = wave.open(AUDIO_FILE, "wb");  # this will open the new ouput audio file for writing in binary mode
```

After the file object is created we need to setup some basic properties about the audio
```python
fwav_obj.setnchannels(1);          # Setting the MONO channels for new audio
fwav_obj.setsamplewidth(2);        # Setting 2 bytes as sample width
fwave_obj.setframerate(44100.0);   # Setting framerate to standard CD quality rate
```

Now we can write the frames to the file
```python
fwav_obj.writeframes(frames);      # writing the frames into new audio file which was read above | Frames should be in bytes

fwav_obj.close();  # Closing the audio file (FOR A GOOD PRACTICE)
```
<br>

# Loading and Playing MP3 files
![](https://upload.wikimedia.org/wikipedia/commons/b/b2/MP3_Logo.png)
<br>
Pyaudio allows us to play and record sounds with Python. To play MP3, however, we first need to convert the MP3 file to WAV format with ffmpeg. To use ffmpeg in Python, we use an interface tool called Pydub, which directly calls our ffmpeg executable and integrates with Pyaudio.
<br><br>

### Here’s an example of how to play mp3 audio files using pydub
Importing AudioSegment from pydub to load mp3 and play function from pydub.playback to play the audio
```python
from pydub import AudioSegment
from pydub.playback import play
```

Loading mp3 file
```python
AUDIO_FILE    = "./assets/vibe-on-173188.mp3"
audMP3_obj    = AudioSegment(AUDIO_FILE);
```

Playing mp3 file
```python
try:
  print("Playing ...");
  play(audMP3_obj);
except KeyboardInterrupt:
  print("Stopped !");
```

Exporting the audio in another format
```python
OUTPUT_FILE  = "./assets/vibe-on_export.wav";
audMP3_obj.export(OUTPUT_FILE, format = "wav");
```
<br>

# Audio Visualization
![](https://miro.medium.com/v2/resize:fit:786/format:webp/0*X8V9OosecAyGjb97)
<br>
Visualizing audio data is important for analyzing and understanding audio signals. In Python, we can use the matplotlib library to plot audio signals in the time domain or frequency domain.
<br><br>

### Here’s an example of how to plot an audio signal in the time domain
Importing the wave library for reading WAV file, matplotlib for visualizing the audio signals and numpy that we will use for storing audio frames
```python
import wave
import matplotlib.pyplot as plt
import numpy as np
```

Next we will read the audio file properties using wave
```python
AUDIO_FILE  = "./assets/sample-9s.wav";
fwav_obj  = wave.open(AUDIO_FILE, "rb");  # Opening the WAV file for reading

sampleWidth      = fwav_obj.getsamplewidth();  # getting the bytes per frame
sampleFramerate  = fwav_obj.getframerate();    # getting the number of frames per seconds
nframes          = fwav_obj.getnframes();      # getting total number of frames
frames           = fwav_obj.readframes(-1);    # Reading all the frames

fwav_obj.close();  # Closing the WAV file
```

Calculates the total time of the audio in seconds
```python
audio_ts  = round(nframes/sampleFramerate, 2);  # getting the total time of audio in seconds and rounding it of upto 2 decimals
```

Creating the array of audio frames and time interval of signals using numpy
```python
signalsArray  = np.frombuffer(frames, dtype=np.int16);                 # creating numpy array of audio frames each of size 16bits
times         = np.linespace(0, audio_ts, num=nframes*sampleWidth);    # getting the time invterval in X-axis of audio time
```

Now we can visualize the audio signals using matplotlib
```python
# VISUALIZATION OF AUDIO
plt.figure(figsize=figsize);    # setting the dimention of graph
plt.plot(times, signals);       # ploting the audio where audio time (x-axis) and audio signals (y-axis)
plt.title("Audio Signals");     # setting the title of graph
plt.ylabel("Signal waves");     # setting the y-axis label of graph
plt.xlabel("Time (sec)");       # setting the x-axis label of graph
plt.xlim(0, audio_ts);          # setting the boundaries of x-axis
plt.show();                     # Displaying the graph
```
<br>

# Audio Recording And Reproduction
![](https://www.bandicam.com/v/audio-recorder/bandicam-audio-recording-noise.jpg)
<br>
A voice recorder records a sound or a voice of a person and converts it into an audio file. The file can be stored in different audio formats like MP3 format, Waveform Audio File (WAV), Advanced Audio Coding (AAC), Audio Interchange File Format (AIFF), etc. and later it can be transferred to other devices. Any device that is capable of recording a sound or a voice is said to be a voice recorder by default.<br>
In python PyAudio provides Python bindings for PortAudio, the cross-platform audio I/O library. With PyAudio, you can easily use Python to play and record audio.
<br><br>

### Here’s an example of how to record sound using PyAudio
Import pyaudio for recording the audio and wave for saving the audio in WAV format
```python
import pyaudio
import wave
```

Next we'll set some constants which we'll use for recording the audio and a constant for file path where the output file is going to be stored
```python
MONO_CHANNEL        = 1;
STEREO_CHANNEL      = 2;
FRAMES_PER_BUFFER   = 3200;
FORMAT_T            = pyaudio.paInt16;
CHANNELS            = MONO_CHANNEL;
RATE                = 16000;

OUPUT_FILE          = "./assets/output.wav";
```

Now initialize the PyAudio for streaming the audio
```python
p         = pyaudio.PyAudio();
stream    = p.open(
  format             = FORMAT_T,
  channels           = CHANNELS,
  rate               = RATE,                  # framerate
  input              = True,                  # Speaker/Microphone .. input state
  frames_per_buffer  = FRAMES_PER_BUFFER
);
```

Start recording using **stream object**
```python
rec_ts  = 5    # for recording the audio for 5 seconds
frames  = [];

# (framerate/frame_per_buffer)  -> audio time wrt framerate
# audio time * rec_ts           -> loops rec_ts times the audio time
for i in range(0, int((framerate/frame_per_buffer)*rec_ts)):
  chunks  = stream.read(frame_per_buffer);    # frames_per_buffer bytes read from input stream
  frames.append(chunks);

stream.stop_stream();
stream.close();
p.terminate();
```

Now as the recorded audio data is now stored in **frames list** we can now save it as WAV file
```python
fwav_obj  = wave.open(OUTPUT_FILE, "wb");

fwav_obj.setnchannels(CHANNELS);
fwav_obj.setsamplewidth(p.get_sample_size(FORMAT_T));    # Setting up the bytes per frame is taking
fwav_obj.setframerate(RATE);
fwav_obj.writeframes(b"".join(frames));                  # Writing the frames in binary

fwav_obj.close();
```
