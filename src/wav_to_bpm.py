import librosa
import librosa.beat as beat
import numpy as np


def extract_audio_data(file_path):
    bpm = extract_bpm(file_path)
    beats, num_beats = calculate_peaks(file_path)

    return bpm, beats, num_beats


def extract_bpm(file_path):
    audio, sample_rate = librosa.load(file_path)
    onset_env = librosa.onset.onset_strength(y=audio, sr=sample_rate)
    # instead of using beats from beat_track, we use peak_pick in calculate_peaks
    # which gives more control over how many beats per second are selected,
    # selecting only the biggest/loudest/main beats    
    tempo, beats = beat.beat_track(onset_envelope=onset_env, sr=sample_rate,
                                   units='time', start_bpm=86)
    """ get the bpm """
    bpm = round(tempo) # round float to nearest int

    return bpm


def calculate_peaks(input_file):
    y, sr = librosa.load(input_file)
    onset_env = librosa.onset.onset_strength(y=y, sr=sr,
                                         hop_length=512,
                                         aggregate=np.median)
    # custom params so that peaks don't occur > 1 every second
    peaks = librosa.util.peak_pick(onset_env, pre_max=100, post_max=100, 
                                   pre_avg=100, post_avg=100, delta=0.5, wait=10)
    
    peak_times = librosa.frames_to_time(peaks, sr=sr)

    # convert to millis & round to nearest integer
    rounded_peaks = []
    for x in peak_times:
        r_peak = x * 1000
        r_peak = round(r_peak)
        rounded_peaks.append(r_peak)

    print("detecting beats...")
    print(f"{len(peak_times)} peaks found")
    # [print(x) for x in rounded_peaks]
    print(f"beat timestamp: \n{rounded_peaks}")

    num_peaks = len(peak_times)

    return rounded_peaks, num_peaks

if __name__ == "__main__":
    wav_file = 'panama.wav'
    extract_audio_data(wav_file)
