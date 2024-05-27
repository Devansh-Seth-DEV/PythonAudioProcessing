'''
Audio file formats
.mp3
.flac
.wav
'''

import wave

'''

Audio signal parameters
- number of channels [1: MONO, 2: STERIO]
    STERIO - has 2 independent channels, gives the impression that audio is coming from 2 different directions

- sample width: no of bytes for each sample

- framerate or sample_rate or sample_frequency: no. of samples for each second
    e.g 44,100 Hz (standard sampling rate for CD quality): means we get 44,100 sample values in each second

- number of frames: total number of frames we get

- values of a frame

'''

def main() -> None:
    SAMPLE_WAV_FILE = "./assets/sample-9s";
    AUDIO_FMT:      = ".wav";
    wavf_obj        = wave.open(SAMPLE_WAV_FILE+AUDIO_FMT, "rb");

    print("Number of channels:", wavf_obj.getnchannels());
    print("Sample width:", wavf_obj.getsampwidth());
    print("Frame rate:", wavf_obj.getframerate());
    print("Number of frames:", wavf_obj.getnframes());
    print("Parameters:", wavf_obj.getparams());

    audio_tm = wavf_obj.getnframes() / wavf_obj.getframerate();
    print("Duration: %0.2fs"%audio_tm);


    frames = wavf_obj.readframes(-1);
    print(type(frames), type(frames[0]))
    print(len(frames));

    print("Duplicating ....")
    wavf_new = wave.open(SAMPLE_WAV_FILE+"_new"+AUDIO_FMT, "wb");
    wavf_new.setnchannels(1);
    wavf_new.setsampwidth(2);
    wavf_new.setframerate(44100.0);

    wavf_new.writeframes(frames);
    print("File duplicated ...")

    wavf_new.close();
    wavf_obj.close();

if ("__main__" == __name__):
    main();
