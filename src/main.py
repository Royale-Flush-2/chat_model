from fastapi import FastAPI

app = FastAPI(title="Centinela Chat Model")


@app.get("/health")
async def health_check():
    return {"status": "ok"}
