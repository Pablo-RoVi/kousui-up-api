from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import engine
from app.dependencies import db_dependency

app = FastAPI()

app.title = "Kousui Up API"
app.version = "0.0.1"
app.description = "API-side Application to manage marketplace fragrances and their dupes, as well as your inventory and wish list"

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db_dependency = db_dependency

@app.get("/health", tags=["Health Check"])
async def health_check():
    return {"status": "healthy"}
