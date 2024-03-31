class Translator:
    def translate(self, text, target_language):
        raise NotImplementedError("Subclasses must implement this method")


class SpanishToEnglishTranslator(Translator):
    def translate(self, text, target_language):
        if target_language == "en":
            return "Hello world"
        raise ValueError("Unsupported target language")


class SpanishToPortugueseTranslator(Translator):
    def translate(self, text, target_language):
        if target_language == "pt":
            return "Olá mundo"
        raise ValueError("Unsupported target language")


class SpanishToFrenchTranslator(Translator):
    def translate(self, text, target_language):
        if target_language == "fr":
            return "Bonjour le monde"
        raise ValueError("Unsupported target language")
