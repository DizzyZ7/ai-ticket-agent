import json
from openai import AsyncOpenAI
from .config import settings

client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

SYSTEM_PROMPT = """
You are an AI support agent.
Return strictly valid JSON:

{
  "category": "billing | technical | account | other",
  "priority": "low | medium | high",
  "reply": "professional short reply"
}
"""

async def analyze_ticket(message: str) -> dict:
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.2,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": message},
        ],
        response_format={"type": "json_object"},
    )

    return json.loads(response.choices[0].message.content)
