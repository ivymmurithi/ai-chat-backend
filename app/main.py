from fastapi import FastAPI
import requests
import json
import os
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from config import add_cors

load_dotenv()
api_key = os.getenv("API_KEY")

app = FastAPI()
add_cors(app)


class UserPrompt(BaseModel):
    prompt: str


@app.post("/")
def root(user_prompt: UserPrompt):
    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    },
    data=json.dumps({
        "model": "deepseek/deepseek-r1:free",
        "messages": [
        {
            "role": "user",
            "content": user_prompt.prompt
        }
        ],  
    }),
    )

    if response.status_code == 200:
        data = response.json()
        return JSONResponse(content=data)
    return JSONResponse(status_code=response.status_code, content={"error": response.text})
