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
    bpm, beats = wav_to_bpm.extract_bpm("panama.wav")
    g.bpm = bpm
    g.beats = beats

@app.route("/")
def homepage():
    return f"<p>homepage\nBPM: {g.bpm}\nBeats: {g.beats}</p>"

@app.route("/bpm")
def bpm():
    return f"<p>BPM: {g.bpm}</p>"

@app.route("/beats")
def beats():
    return f"<p>Beats: {g.beats}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)






