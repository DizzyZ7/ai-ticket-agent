# AI Ticket Agent

Production-ready AI ticket processing system.

Stack:
- FastAPI
- OpenAI
- PostgreSQL
- Redis
- Docker

Run:

docker-compose up --build

POST http://localhost:8000/tickets

{
  "user_id": "42",
  "message": "I was charged twice"
}
