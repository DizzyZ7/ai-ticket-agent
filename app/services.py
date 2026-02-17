import hashlib
import aioredis
from sqlalchemy import select
from .database import AsyncSessionLocal
from .models import Ticket
from .ai import analyze_ticket
from .config import settings

redis = aioredis.from_url(settings.REDIS_URL, decode_responses=True)

def generate_hash(user_id: str, message: str) -> str:
    raw = f"{user_id}:{message}"
    return hashlib.sha256(raw.encode()).hexdigest()

async def process_ticket(user_id: str, message: str):
    request_hash = generate_hash(user_id, message)

    if await redis.get(request_hash):
        raise ValueError("Duplicate request")

    await redis.set(request_hash, "1", ex=300)

    ai_result = await analyze_ticket(message)

    async with AsyncSessionLocal() as session:
        ticket = Ticket(
            user_id=user_id,
            message=message,
            category=ai_result["category"],
            priority=ai_result["priority"],
            reply=ai_result["reply"],
        )
        session.add(ticket)
        await session.commit()
        await session.refresh(ticket)

    return ticket
