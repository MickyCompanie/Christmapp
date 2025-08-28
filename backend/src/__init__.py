from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from src.db.main import init_db
from src.config import Config

from src.user.routes import user_router
from src.auth.routes import auth_router
from src.person.routes import person_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    await init_db()
    yield
    print("Shutting down...")




version = Config.VERSION
prefix = Config.PREFIX


url = f"/{prefix}{version}"

app = FastAPI(
    title="Christmapp API",
    description="API for the Christmapp application",
    version=version
)

app.include_router(user_router, prefix=f"{url}/users", tags=["users"])
app.include_router(auth_router, prefix=f"{url}/auth", tags=["auth"])
app.include_router(person_router, prefix=f"{url}/persons", tags=["persons"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=[Config.FRONT_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}
