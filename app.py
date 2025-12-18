from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Input(BaseModel):
    message: str

@app.post("/decide")
def decide(data: Input):
    keywords = ["urgent", "important", "critical", "asap"]
    is_important = any(k in data.message.lower() for k in keywords)
    return {"important": is_important}
