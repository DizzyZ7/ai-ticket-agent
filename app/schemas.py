from pydantic import BaseModel

class TicketRequest(BaseModel):
    user_id: str
    message: str

class TicketResponse(BaseModel):
    id: int
    category: str
    priority: str
    reply: str
