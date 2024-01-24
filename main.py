from audio_processing import record_snippet
import whisper
model = whisper.load_model("base")

# create a function to access the microphone and convert speech to text


def transcribe(audio_file: str) -> str: # ?
    result = model.transcribe(audio_file)
    return result["text"]


def classify(transcription: str) -> str or None:
    keyword = 'floor is yours'
    if keyword in transcription:
        return 'floor.given'
    return None


def main():
    io_pipeline = [
        record_snippet,
        transcribe,
        classify
    ]

    nxt = 15
    for step in io_pipeline:
        nxt = io_pipeline.pop(0)(nxt)
        print(nxt)


if __name__ == "__main__":
    main()
