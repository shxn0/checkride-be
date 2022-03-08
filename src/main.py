from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .speech_to_text.controller import router as speech_router
from . import config

api = FastAPI()
origins = [
    config.FRONTEND_URL
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

api.include_router(speech_router)