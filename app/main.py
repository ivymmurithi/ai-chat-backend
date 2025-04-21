from fastapi import FastAPI
import requests
import json
import os
from dotenv import load_dotenv
from fastapi.responses import JSONResponse


load_dotenv()
api_key = os.getenv("API_KEY")

app = FastAPI()

@app.get("/")
def root():
    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    },
    data=json.dumps({
        "model": "deepseek/deepseek-v3-base:free",
        "messages": [
        {
            "role": "user",
            "content": "What is the meaning of life?"
        }
        ],  
    }),
    )

    if response.status_code == 200:
        data = response.json()
        return JSONResponse(content=data)
    return JSONResponse(status_code=response.status_code, content={"error": response.text})
