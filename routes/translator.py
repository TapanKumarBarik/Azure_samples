from typing import Optional, List

from fastapi import APIRouter, HTTPException

from pydantic import BaseModel

from services.translator_service import translate_text, detect_language, detect_language_during_translation

router = APIRouter()



class TranslationRequest(BaseModel):
    text: str
    from_lang: Optional[str] = "en"
    to_langs: Optional[List[str]] = ["fr", "es"]

class DetectSourceDuringTranslationRequest(BaseModel):
    text: str
    to_langs: Optional[List[str]] = ["fr", "es","en"]
@router.post("/translate/",description="Translate the given text from one language to multiple target languages. Specify the source language and a list of target languages for translation.")
def translate(request: TranslationRequest):
    try:
        result = translate_text(request.text, request.from_lang, request.to_langs)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation error: {e}")


@router.post("/deletct-language/",description="Detect source language without translation")
def translate(query:str):
    try:
        result = detect_language(query)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation error: {e}")


@router.post("/deletct-language-while-translation/", description="Detect source language during translation")
def translate(request: DetectSourceDuringTranslationRequest):
    try:
        result = detect_language_during_translation(request.text, request.to_langs)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation error: {e}")


#Transliterate text

#https://learn.microsoft.com/en-us/azure/ai-services/translator/translator-text-apis?tabs=python#transliterate-text



