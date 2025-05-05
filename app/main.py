from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text
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

# PostgreSQL configuration
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@postgres:5432/fastapi")
engine = create_engine(DATABASE_URL)

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI Containerized App"}

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "redis": "connected" if redis_client.ping() else "Redis disconnected",
        "postgres": "connected" if engine.connect() else "PostgreSQL disconnected",
        "app": "running",
        "version": "1.0.0"
    }

@app.get("/test/postgres")
async def test_postgres():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT version();"))
            version = result.scalar()
            return {
                "status": "success",
                "message": "PostgreSQL connection successful",
                "version": version
            }
    except Exception as e:
        return {
            "status": "error",
            "message": f"PostgreSQL connection failed: {str(e)}"
        }

@app.get("/test/redis")
async def test_redis():
    try:
        # Test Redis connection and basic operations
        redis_client.set("test_key", "Hello Redis!")
        value = redis_client.get("test_key")
        redis_client.delete("test_key")
        
        return {
            "status": "success",
            "message": "Redis connection successful",
            "test_value": value
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Redis connection failed: {str(e)}"
        } 