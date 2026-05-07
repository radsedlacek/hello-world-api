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