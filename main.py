from fastapi import FastAPI
from pydantic import BaseModel

from extractor_v2_spacy import extract_entities_spacy

app = FastAPI(
    title= "Medi_Extract API",
    description = " An API for extracting entities from instructured medical reports"
)

# Pydantic models define the structure of your request and response
class MedicalTextRequest(BaseModel): 
    text:str

# Define the endpoint decorator
#app.post("/extract" means this function will handle HTTP POST request)
@app.post("/extract/")
async def extract_entities_from_text(request: MedicalTextRequest):
    text_to_process = request.text
    extracted_entities = extract_entities_spacy(text_to_process)

    return { 
        "input_text": text_to_process[:100] + "...", 
        "extracted_entities": extracted_entities
    }

@app.get("/")
def read_root():
    return {"status": "Medi_Extract API is running"}