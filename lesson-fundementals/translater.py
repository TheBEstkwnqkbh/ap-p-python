import string


RANDOM_LANGUAGE_NAME = "Glyphish"
ENGLISH_ALPHABET = string.ascii_lowercase + string.ascii_uppercase
GLYPH_ALPHABET = (
    "☯⊗✦◉⌘♢☼⌖⚙⊙◇✧◈☍❖♤◌♨◊☷⊕❂✶❄✺❈"
    "₪☂✿♕⚑◍☄✚♛⌬☁⚒✪☾✣☘❋☠✴♙☀⊛♬♠♥♦"
)

TO_GLYPHISH = str.maketrans(ENGLISH_ALPHABET, GLYPH_ALPHABET)
FROM_GLYPHISH = str.maketrans(GLYPH_ALPHABET, ENGLISH_ALPHABET)


def translate_to_glyphish(text: str) -> str:
    """Translate English letters into Glyphish symbols."""
    return text.translate(TO_GLYPHISH)


def translate_to_english(text: str) -> str:
    """Translate Glyphish symbols back into English letters."""
    return text.translate(FROM_GLYPHISH)


def main() -> None:
    print(f"English ↔ {RANDOM_LANGUAGE_NAME} Translator")
    print("1. English to Glyphish")
    print("2. Glyphish to English")
    direction = input("Choose 1 or 2: ").strip()
    text = input("Enter text to translate: ")

    if direction == "1":
        print(translate_to_glyphish(text))
    elif direction == "2":
        print(translate_to_english(text))
    else:
        print("Invalid choice. Please choose 1 or 2.")


if __name__ == "__main__":
    main()