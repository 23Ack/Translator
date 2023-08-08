pip install googletrans==4.0.0-rc1
from googletrans import Translator

def translate_text(text, source_language, target_language):
    translator = Translator()
    translated_text = translator.translate(text, src=source_language, dest=target_language)
    return translated_text.text

if __name__ == "__main__":
    print("Translator AI - Supported Languages:")
    print("1. English (en)\n2. Spanish (es)\n3. French (fr)\n4. German (de)\n5. Chinese (zh-CN)")
    
    source_text = input("Enter the text to translate: ")
    source_language = input("Enter the source language code (e.g., 'en' for English): ")
    target_language = input("Enter the target language code (e.g., 'es' for Spanish): ")
    
    translated_text = translate_text(source_text, source_language, target_language)
    print(f"\nTranslated text: {translated_text}")

    
