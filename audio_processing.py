import sounddevice as sd
import random
import numpy as np
import scipy.io.wavfile as wav
import os
import whisper
model = whisper.load_model("base")

def record_snippet(duration : int) -> str:
    # Set the sample rate and the number of channels for the audio capture
    id = [str(random.randint(1,9)) for i in range(5)]
    id = "_".join(id)
    filename = f"{id}transcript.wav"
    sample_rate = 16000
    channels = 1

    # Create a buffer to hold the audio data
    buffer = []

    # Create a callback function to capture audio data
    def callback(indata, frames, time, status):
        buffer.append(indata.copy())

    # Create a stream to capture audio
    stream = sd.InputStream(callback=callback, channels=channels, samplerate=sample_rate)

    print("Recording...")
    # Start the audio stream and record for the specified duration
    with stream:
        sd.sleep(duration * 1000)

    print("Finished recording.")

    # Convert the buffer to a NumPy array
    audio_data = np.concatenate(buffer, axis=0)

    # Save the audio data to a WAV file
    wav.write(filename, sample_rate, audio_data)

    # Return the file path
    return os.path.abspath(filename)

def transcribe(audio_file: str) -> str: # ?
    result = model.transcribe(audio_file)
    return result["text"]


def classify(transcription: str) -> str or None:
    keyword = 'floor is yours'
    if keyword in transcription.lower():
        return 'floor.given'
    return None


def AudioProcessingComponentPipeline(time : int) -> str or None:
    io_pipeline = [
        record_snippet,
        transcribe,
        classify
    ]

    nxt = time
    while io_pipeline:
        nxt = io_pipeline.pop(0)(nxt)
    return nxt
