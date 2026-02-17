from fastapi import FastAPI, HTTPException
from .schemas import TicketRequest, TicketResponse
from .database import engine, Base
from .services import process_ticket

app = FastAPI(title="AI Ticket Agent")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.post("/tickets", response_model=TicketResponse)
async def create_ticket(ticket: TicketRequest):
    try:
        result = await process_ticket(ticket.user_id, ticket.message)
        return TicketResponse(
            id=result.id,
            category=result.category,
            priority=result.priority,
            reply=result.reply,
        )
    except ValueError:
        raise HTTPException(status_code=409, detail="Duplicate request")
    except Exception:
        raise HTTPException(status_code=500, detail="Internal error")
