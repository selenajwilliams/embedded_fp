from flask import Flask, g

# import wav_to_bpm
# from wav_to_bpm import extract_bpm
import sys
import os
sys.path.append("./")

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from . import wav_to_bpm

app = Flask(__name__)

# to run locally & externally:
# flask run --host=0.0.0.0 --port=5001

@app.before_request
def before_request():
    bpm, beats, num_beats = wav_to_bpm.extract_audio_data("panama.wav")

    g.bpm = bpm
    g.beats = beats
    g.num_beats = num_beats

@app.route("/")
def homepage():
    return f"<p>homepage\nBPM: {g.bpm}\nBeats: {g.beats}</p>"

@app.route("/bpm") # note: I am not using this endpoint currently
def bpm():
    return f"<p>{g.bpm}</p>"

@app.route("/beats")
def beats():
    return f"<p>{g.beats}</p>"

@app.route("/num_beats")
def num_beats():
    print(g.num_beats)
    return f"<p>{g.num_beats}</p>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
