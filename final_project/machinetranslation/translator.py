"""
This module has functions to translate between english and french
"""

import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
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

language_translator.set_disable_ssl_verification(True)

def englishToFrench(TEXT):
    """
    This function returns the translated englishText.
    """
    if TEXT is None:
        return None

    translation = language_translator.translate(
    text=TEXT,
    model_id='en-fr').get_result()

    return translation["translations"][0]["translation"]

def frenchToEnglish(TEXT):
    """
    This function returns the translated frenchText.
    """
    if TEXT is None:
        return None

    translation = language_translator.translate(
    text=TEXT,
    model_id='fr-en').get_result()

    return translation["translations"][0]["translation"]
