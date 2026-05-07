from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class TextRequest(BaseModel):
    text: str


class TextResponse(BaseModel):
    message: str
    length: int


@app.get("/")
def read_root():
    return {"message": "Hello World API is running"}


@app.post("/process-text", response_model=TextResponse)
def process_text(request: TextRequest):
    return {
        "message": f"Přijal jsem text: {request.text}",
        "length": len(request.text)
    }

class ClassificationResponse(BaseModel):
    text: str
    is_invoice: bool
    reason: str


@app.post("/classify-text", response_model=ClassificationResponse)
def classify_text(request: TextRequest):
    invoice_keywords = ["invoice", "faktura", "fakturu", "daňový doklad"]

    text_lower = request.text.lower()
    is_invoice = any(keyword in text_lower for keyword in invoice_keywords)

    return {
        "text": request.text,
        "is_invoice": is_invoice,
        "reason": "Text contains invoice-related keyword."
        if is_invoice
        else "Text does not contain invoice-related keyword."
    }