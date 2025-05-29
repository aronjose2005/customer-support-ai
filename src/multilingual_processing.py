import openai_whisper as whisper
from transformers import pipeline

# Audio-to-text in multiple languages using Whisper
def audio_to_text(audio_path, language="en"):
    try:
        model = whisper.load_model("small")
        result = model.transcribe(audio_path, language=language)
        return result["text"]
    except FileNotFoundError:
        return "Audio file not found. Please provide a valid audio file."

# Translate text to target language
def translate_text(text, target_language="en"):
    translator = pipeline("translation", model=f"Helsinki-NLP/opus-mt-{target_language}-en")
    translated = translator(text, max_length=512)[0]["translation_text"]
    return translated
