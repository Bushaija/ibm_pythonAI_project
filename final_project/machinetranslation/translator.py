import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API key and URL from environment variables
apikey = os.environ['apikey']
url = os.environ['url']
model_id = 'en-it'

# Initialize language translator instance
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)


def englishToFrench(englishText):
    """Translate English text to French and return the result."""
    result = language_translator.translate(
        text=englishText,
        source='en',
        target='fr'
    ).get_result()
    frenchText = result['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    """Translate French text to English and return the result."""
    result = language_translator.translate(
        text=frenchText,
        source='fr',
        target='en'
    ).get_result()
    englishText = result['translations'][0]['translation']
    return englishText

