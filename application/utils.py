# pip install googletrans==3.1.0a0
from cv2 import triangulatePoints
from googletrans import Translator

translator = Translator()

def detect_language(text):
    # get language used
    detected_lang_data = translator.detect(text)
    # print(lang)
    lang = detected_lang_data.lang
    conf = detected_lang_data.confidence

    return lang, conf

def translate_text(text, dest):
    translated_text = translator.translate(text, dest=dest)
    return translated_text.text


languages = {
    'hi': 'hindi',
    'bn': 'bengali',
    'te': 'telegu',
    'mr': 'marathi',
    'ta': 'tamil',
    'ur': 'urdu',
    'gu': 'gujrati',
    'kn': 'kannada',
    'or': 'odia',
    'ml': 'malayalam',
    'my': 'myanmar (burmese)',
    'as': 'assamese',
    'pa': 'punjabi',
    'sa': 'sanskrit',
    'ks': 'kashmiri',
    'sd': 'sindhi',
    'mi': 'manipuri',
    'ne': 'nepali',
}