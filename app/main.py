from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from redis import Redis
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(title="FastAPI Containerized App")

# Redis configuration
redis_client = Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True
)

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI Containerized App"}

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "redis": "connected" if redis_client.ping() else "disconnected"
    } 