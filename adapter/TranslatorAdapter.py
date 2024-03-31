from adapter import SpanishToEnglishTranslator, SpanishToPortugueseTranslator, SpanishToFrenchTranslator


class TranslatorAdapter:
    def __init__(self):
        self.translators = {
            "en": SpanishToEnglishTranslator(),
            "pt": SpanishToPortugueseTranslator(),
            "fr": SpanishToFrenchTranslator()
        }

    def translate(self, text, target_language):
        translator = self.translators.get(target_language)
        if translator:
            return translator.translate(text, target_language)
        raise ValueError(f"No translator available for target language: {target_language}")
