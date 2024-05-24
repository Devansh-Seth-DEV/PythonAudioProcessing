from pydub import AudioSegment
from pydub.playback import play

AUDIO_FILE: str     = "./assets/vibe-on-173188.mp3";
OUTPUT_FILE: str    = "./assets/vibe-on_export.wav";

LoadMP3     = lambda file_path: AudioSegment.from_mp3(file_path);
LoadWAV     = lambda file_path: AudioSegment.from_wav(file_path);
INC_VOL     = lambda audio, db: audio + db; 
REP_AUD     = lambda audio, rep: audio * rep;
FADE_IN_AUD = lambda audio, millisec: audio.fade_in(millisec);
EXPORT_AUD  = lambda audio, file_path, expFormat: audio.export(file_path, format = expFormat)

def PlayAudio(audio_obj: AudioSegment, title: str="audio") -> None:
    try:
        print(f"Playing {title} ... \n(PRESS <ctrl+c> TO STOP)");
        play(audio_obj);
    except KeyboardInterrupt:
        print(f"Stopping {title} ...\n");

def main() -> None:
    print("Loading mp3 audio ...")
    audio_mp3: AudioSegment   = LoadMP3(AUDIO_FILE);

    audio_mp3: AudioSegment   = INC_VOL(audio_mp3, 6)           # Increases the volume by 6dB

    audio_mp3: AudioSegment   = REP_AUD(audio_mp3, 2)           # Repeate the clip 2 times

    audio_mp3: AudioSegment   = FADE_IN_AUD(audio_mp3, 2000);   # Fade in for 2000 milisec

    print("Converting mp3 to wav ...")
    EXPORT_AUD(audio_mp3, OUTPUT_FILE, "wav");
    print("Successfully converted");

    print("Loading exported wav audio ...\n")
    audio_wav: AudioSegment   = LoadWAV(OUTPUT_FILE);

    PlayAudio(audio_mp3, "Vibe ON");
    PlayAudio(audio_wav, "Vibe ON EXPORTED");


if __name__ == "__main__":
    main();