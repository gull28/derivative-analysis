from fastapi import FastAPI
from db.session import Base, engine
from contextlib import asynccontextmanager



@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    print("Database tables created.")
    yield
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)


@app.get("/") 
def read_root(): return {"message": "Hello, World!"}


