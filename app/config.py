from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Settings:
    AZURE_TRANSLATOR_KEY = os.getenv("AZURE_TRANSLATION_KEY")
    AZURE_TRANSLATOR_LOCATION = os.getenv("AZURE_TRANSLATOR_LOCATION")
    AZURE_TRANSLATOR_ENDPOINT=os.getenv("AZURE_TRANSLATION_ENDPOINT")

settings = Settings()
