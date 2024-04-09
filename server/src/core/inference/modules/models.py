import torch
import whisper


class InferenceSession:
    def __init__(self, model_name):
        self._audio = None
        self._model = whisper.load_model(model_name)

    def load_audio(self, audio_path):
        self._audio = whisper.load_audio(audio_path)
        return self

    def run(self):
        # load audio and pad/trim it to fit 30 seconds
        if self._audio is None:
            raise ValueError("No audio loaded")
        audio = whisper.pad_or_trim(self._audio)
        # make log-Mel spectrogram and move to the same device as the model
        mel = whisper.log_mel_spectrogram(audio).to(self._model.device)

        # detect the spoken language
        _, probs = self._model.detect_language(mel)
        print(f"Detected language: {max(probs, key=probs.get)}")

        # decode the audio
        options = whisper.DecodingOptions()
        result = whisper.decode(self._model, mel, options)
        # print the recognized text
        return result

    def transcribe(self, audio_path):
        result = self._model.transcribe(audio_path)
        return result
