"""Application configuration. Values can be overridden via environment variables."""
import os

# Security
SECRET_KEY = os.getenv("WOMENRISE_SECRET", "womenrise-dev-secret-change-in-prod")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days

# Database — SQLite file in the backend directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASE_URL = os.getenv("WOMENRISE_DB", f"sqlite:///{os.path.join(BASE_DIR, 'womenrise.db')}")

# CORS — frontend dev origins
CORS_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:4173",
    "http://localhost:3000",
]
