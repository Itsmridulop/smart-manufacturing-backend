from fastapi import FastAPI
from routers.temperature_route import router as temperature_router
from routers.gps_route import router as gps_router
from routers.acoustic_route import router as acoustic_router
from routers.magnetic_route import router as magnetic_router
from routers.vibration_route import router as vibration_router
from routers.humidity_route import router as humidity_router
from database import startup_db_client, shutdown_db_client
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await startup_db_client()
    try:
        yield
    finally:
        await shutdown_db_client()


app = FastAPI(title="Smart Manufacturing Sensor Data API", lifespan=lifespan)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

app.include_router(temperature_router)
app.include_router(gps_router)
app.include_router(acoustic_router)
app.include_router(magnetic_router)
app.include_router(vibration_router)
app.include_router(humidity_router)