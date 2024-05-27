import wave
import matplotlib.pyplot as plt
import numpy as np

ASSETS_PATH: str    = "./assets/";
AUD_FILENAME: str   = "sample-9s";
AUD_FMT: str        = ".wav";

def PlotAudioSignals(
        figsize: tuple[float, float],
        times: np.ndarray[np.floating[np.any]],
        signals: np.ndarray[np.int16],
        title: str,
        xlabel: str,
        ylabel: str,
        xlim: tuple[float, float]
) -> None:
    plt.figure(figsize=figsize);
    plt.plot(times, signals);
    plt.title(title);
    plt.ylabel(ylabel);
    plt.xlabel(xlabel);
    plt.xlim(*xlim);
    plt.show();


def main() -> None:
    fwav_obj            = wave.open(ASSETS_PATH+AUD_FILENAME+AUD_FMT, "rb");

    sample_width        = fwav_obj.getsampwidth();
    sample_framerate    = fwav_obj.getframerate();
    nsamples            = fwav_obj.getnframes();
    signal_wave         = fwav_obj.readframes(-1);

    fwav_obj.close();

    audio_tm = round(nsamples/sample_framerate, 2);

    signals_array    = np.frombuffer(signal_wave, dtype=np.int16);
    times            = np.linspace(0, audio_tm, num=nsamples*sample_width);

    PlotAudioSignals((10, 5), times, signals_array, "Audio Signals", "Time (sec)", "Signal Wave", (0, audio_tm));

if ("__main__" == __name__):
    main();