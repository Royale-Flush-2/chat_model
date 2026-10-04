from fastapi import FastAPI
from src.schemas import DecisionRequest

app = FastAPI(title="Centinela Chat Model")


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.post("/alertas/{alerta_id}/decision")
async def process_decision(alerta_id: int, request: DecisionRequest):
    return {"status": "success", "alerta_id": alerta_id, "decision": request.decision}

