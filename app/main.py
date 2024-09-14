from fastapi import FastAPI

from routes import translator

# Initialize the FastAPI app
app = FastAPI(title="Cloud Services API", version="1.0")

# Include routes from each cloud service
app.include_router(translator.router, prefix="/translator", tags=["Translator"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Cloud Services API"}
