import sounddevice as sd
import random
import numpy as np
import scipy.io.wavfile as wav
import os
from pydub import AudioSegment

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

    # Start the audio stream and record for the specified duration
    with stream:
        sd.sleep(duration * 1000)

    # Convert the buffer to a NumPy array
    audio_data = np.concatenate(buffer, axis=0)

    # Save the audio data to a WAV file
    wav.write(filename, sample_rate, audio_data)

    # Transform the WAV file to a mp3 file

    new_name = filename.replace('.wav', '.mp3')

    filename = AudioSegment.from_wav(filename).export(f"{new_name}", format='mp3')

    # Return the file path
    return os.path.abspath(new_name)

