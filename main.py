from audio_processing import AudioProcessingComponentPipeline
import warnings
RECORDING_TIME = 5


def main():
    warnings.filterwarnings("ignore")
    print("Starting audio processing component...")
    print("Press Ctrl+C to stop the program.")
    action = None
    while True:
        try:
            action = AudioProcessingComponentPipeline(RECORDING_TIME)
        except KeyboardInterrupt:
            print("Stopping audio processing component...")
            break
        if action is not None:
            print(f"Action: {action}")
        else:
            print("No action detected.")


if __name__ == "__main__":
    main()
