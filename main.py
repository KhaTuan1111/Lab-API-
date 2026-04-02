from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM

app = FastAPI()

model_name = "LiquidAI/LFM2.5-350M"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

class RequestData(BaseModel):
    prompt: str

@app.get("/")
def root():
    return {"message": "Text Generation API"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/generate")
def generate(data: RequestData):
    if not data.prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt cannot be empty")

    inputs = tokenizer(data.prompt, return_tensors="pt")

    outputs = model.generate(**inputs, max_length=100)

    result = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return {
        "input": data.prompt,
        "output": result
    }