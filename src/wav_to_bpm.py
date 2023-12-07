import librosa
import librosa.beat as beat

def extract_bpm(file_path):
    audio, sample_rate = librosa.load(file_path)
    onset_env = librosa.onset.onset_strength(y=audio, sr=sample_rate)
    tempo, beats = beat.beat_track(onset_envelope=onset_env, sr=sample_rate)
    bpm = round(tempo) # round float to nearest int


    beats_string = str(beats).strip("[]")

    num_beats = len(beats)
    # beats_string = ' '.join(str(beats)) # pre-processing beats
    # beats_string.strip("[]")

    print(beats_string)

    return bpm, beats_string, num_beats

if __name__ == "__main__":
    wav_file = 'panama.wav'
    extract_bpm(wav_file)
