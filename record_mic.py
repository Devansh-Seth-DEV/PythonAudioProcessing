import pyaudio
import wave

# (constants) -------------------------
MONO_CHANNEL        = 1;
STEREO_CHANNEL      = 2;
FRAMES_PER_BUFFER   = 3200;
FORMAT_T            = pyaudio.paInt16;
CHANNELS            = MONO_CHANNEL;
RATE                = 16000;
FILE_PATH           = "./assets/"
FILE_NAME           = "ouput";
FILE_FMT            = ".wav";
# --------------------------------------

def InitPyAudio() -> pyaudio.PyAudio:
    p: pyaudio.PyAudio  = pyaudio.PyAudio(); # Initialize PyAudio object
    return p;

def InitAudioStream(
        p: pyaudio.PyAudio,     # PyAudio Object
        fmt: int,               # Bytes per frame
        audio_channels: int,    # Channel of audio
        framrate: int,          # Number of sample frames per second
        audio_input: bool,      # Speaker/Microphone .. input state
        audio_fbuffer: int      # Frame chunks per buffer to be read
) -> pyaudio.PyAudio.Stream:

    # Initializing stream object
    stream: pyaudio.PyAudio.Stream = p.open(
        format              = fmt,
        channels            = audio_channels,
        rate                = framrate,
        input               = audio_input,
        frames_per_buffer   = audio_fbuffer
    );

    return stream;

def StopPyAudio(p: pyaudio.PyAudio) -> None:
    p.terminate();

def StopStream(stream: pyaudio.PyAudio.Stream) -> None:
    stream.stop_stream();
    stream.close();

def StartRecording(
        p: pyaudio.PyAudio,                 # PyAudio Object
        stream: pyaudio.PyAudio.Stream,     # PyAudio Stream Object
        framerate: int,                     # Number of sample frames per second
        frame_per_buffer: int,              # Frames chunks per buffer
        rec_ts: int                         # Record time in seconds
) -> list[bytes]:

    frames: list[bytes]  = [];

    # (framerate/frame_per_buffer) -> audio time wrt framerate
    # audio time * rec_ts -> loops rec_ts times the audio time
    for i in range(0, int((framerate/frame_per_buffer)*rec_ts)):
        chunks: bytes   = stream.read(frame_per_buffer);    # frames_per_buffer bytes read from input stream
        frames.append(chunks);
    
    StopStream(stream);
    StopPyAudio(p);

    return frames;

def CreateWav(
        save_path: str,         # Output wave file path
        p: pyaudio.PyAudio,     # PyAudio Object
        channels: int,          # wave audio channels
        fmt: int,               # bytes per frame
        framerate: int,         # Number of sample frames per second
        frames: list[bytes]     # list of frames to write
) -> None:

    fwav    = wave.open(save_path, "wb");           # Open wave audio file for writing in binary mode

    fwav.setnchannels(channels);                    # Setting the audio channels
    fwav.setsampwidth(p.get_sample_size(fmt));      # Setting up the bytes per frame is taking
    fwav.setframerate(framerate);                   # Number of sample frames in one second
    fwav.writeframes(b"".join(frames));             # Writing the frames in binary

    fwav.close();                                   # Closing the wave file

def main() -> None:
    p: pyaudio.PyAudio              = InitPyAudio();
    stream: pyaudio.PyAudio.Stream  = InitAudioStream(p, FORMAT_T, CHANNELS, RATE, True, FRAMES_PER_BUFFER);
    
    print("Recording...");
    frames: list[bytes] = StartRecording(p, stream, RATE, FRAMES_PER_BUFFER, 5);

    CreateWav(FILE_PATH+FILE_NAME+FILE_FMT, p, CHANNELS, FORMAT_T, RATE, frames);

if ("__main__" == __name__):
    main();