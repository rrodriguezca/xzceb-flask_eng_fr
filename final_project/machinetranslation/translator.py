 from deep_translator import MyMemoryTranslator

 def english_to_french(english_text):
    """
    English to French
    """
    french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)
    print(french_text)
    return french_text

    def french_to_english(french_text):
    """
    French to English
    """
    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    print(english_text)
    return english_text