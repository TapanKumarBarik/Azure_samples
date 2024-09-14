import requests, uuid, json
from app.config import settings


def translate_text(text: str, from_lang: str, to_langs: list):
    print("translate_text API started-------------")
    key = settings.AZURE_TRANSLATOR_KEY
    location = settings.AZURE_TRANSLATOR_LOCATION
    endpoint = settings.AZURE_TRANSLATOR_ENDPOINT

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': from_lang,
        'to': to_langs
    }
    print("params------------")
    print(params)
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{
        'text': text
    }]

    try:
        response = requests.post(constructed_url, params=params, headers=headers, json=body)
        return response.json()
    except Exception as e:
        return {"message":e}


def detect_language(query):
    print("detect_language API started-------------")
    key = settings.AZURE_TRANSLATOR_KEY
    location = settings.AZURE_TRANSLATOR_LOCATION
    endpoint = settings.AZURE_TRANSLATOR_ENDPOINT

    path = '/detect'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0'
    }
    print("params------------")
    print(params)


    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{
        'text': query
    }]
    print("body------------")
    print(body)
    try:
        response=requests.post(constructed_url, params=params, headers=headers, json=body)
        return response.json()
    except Exception as e:
        return {"message":e}

def detect_language_during_translation(text: str,  to_langs: list):
    print("detect_language_during_translation API started-------------")
    key = settings.AZURE_TRANSLATOR_KEY
    location = settings.AZURE_TRANSLATOR_LOCATION
    endpoint = settings.AZURE_TRANSLATOR_ENDPOINT

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'to': to_langs
    }
    print("params------------")
    print(params)
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{
        'text': text
    }]
    print("body------------")
    print(body)
    try:
        response = requests.post(constructed_url, params=params, headers=headers, json=body)
        return response.json()
    except Exception as e:
        return {"message":e}