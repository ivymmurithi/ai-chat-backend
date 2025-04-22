from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

def add_cors(app: FastAPI):
    origins = [
        "http://localhost:3000",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_methods=["*"],
        allow_headers=["*"],
    )