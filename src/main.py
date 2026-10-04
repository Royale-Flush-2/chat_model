import asyncio
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from src.schemas import ChatRequest, DecisionRequest

app = FastAPI(title="Centinela Chat Model")


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.post("/alertas/{alerta_id}/decision")
async def process_decision(alerta_id: int, request: DecisionRequest):
    return {"status": "success", "alerta_id": alerta_id, "decision": request.decision}


async def mock_stream():
    yield "data: Hola\n\n"
    await asyncio.sleep(0.1)
    yield "data: Soy el agente\n\n"


@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    return StreamingResponse(mock_stream(), media_type="text/event-stream")

