import os

class Settings:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql+asyncpg://postgres:postgres@db:5432/tickets"
    )
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://redis:6379")

settings = Settings()
