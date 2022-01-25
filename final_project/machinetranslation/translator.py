import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """Translates from English to French.

    Keyword arguments:
    english_text -- the english text to be translated
    """
    if english_text is not None:
        translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
        frenchText =  translation['translations'][0]['translation']
        return frenchText
    return None

def french_to_english(french_text):
    """Translates from French to English.

    Keyword arguments:
    french_text -- the french text to be translated
    """

    if french_text is not None:
        translation = language_translator.translate(
            text = french_text,
            model_id='fr-en').get_result()
        englishText = translation['translations'][0]['translation']
        return englishText
    return None


