from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.db.main import init_db

from src.auth.routes import auth_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    await init_db()
    yield
    print("Shutting down...")


version = "0.1.0"
prefix = f"/api/v{version}"

app = FastAPI(
    title="Christmapp API",
    description="API for the Christmapp application",
    version=version,

)

app.include_router(auth_router, prefix=f"{prefix}/auth", tags=["auth"])


@app.get("/")
def read_root():
    return {"Hello": "World"}
