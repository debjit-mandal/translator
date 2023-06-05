from googletrans import Translator, LANGUAGES

def translate_text(text, dest_language):
    translator = Translator()
    try:
        translation = translator.translate(text, dest=dest_language)
        return translation.text
    except Exception as e:
        print(f"Translation error: {str(e)}")
        return ""

def detect_language(text):
    translator = Translator()
    try:
        detection = translator.detect(text)
        return detection.lang
    except Exception as e:
        print(f"Language detection error: {str(e)}")
        return ""

def print_languages():
    print("Supported Languages:")
    for code, language in LANGUAGES.items():
        print(f"{code}: {language}")

print("Language Translator")
print("-------------------")

while True:
    print("\nOptions:")
    print("1. Translate text")
    print("2. Detect language")
    print("3. Display supported languages")
    print("4. Quit")

    choice = input("Enter your choice (1, 2, 3, or 4): ")

    if choice == "1":
        text_to_translate = input("Enter the text to translate: ")
        destination_language = input("Enter the destination language code: ")

        # Validate destination language code
        if destination_language not in LANGUAGES:
            print("Invalid destination language code.")
            continue

        # Validate input text
        if not text_to_translate:
            print("Input text cannot be empty.")
            continue

        # Translate the text
        sentences = text_to_translate.split(".")
        translated_sentences = []

        for sentence in sentences:
            sentence = sentence.strip()
            if sentence:
                translated_sentence = translate_text(sentence, destination_language)
                if translated_sentence:
                    translated_sentences.append(translated_sentence)

        if not translated_sentences:
            print("Translation failed. Please try again.")
            continue

        detected_language = detect_language(text_to_translate)

        if detected_language in LANGUAGES:
            detected_language = LANGUAGES[detected_language]

        print(f"\nDetected language: {detected_language}")
        print(f"Translated text: {' '.join(translated_sentences)}\n")

    elif choice == "2":
        text_to_detect = input("Enter the text to detect language: ")

        # Validate input text
        if not text_to_detect:
            print("Input text cannot be empty.")
            continue

        detected_language = detect_language(text_to_detect)

        if detected_language in LANGUAGES:
            detected_language = LANGUAGES[detected_language]

        print(f"\nDetected language: {detected_language}\n")

    elif choice == "3":
        print_languages()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
