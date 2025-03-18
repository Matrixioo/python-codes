from fastapi import FastAPI
from contextlib import asynccontextmanager
from databaswe import create_tables, delete_tables
from router import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("DB is cleared")
    await create_tables()
    print("DB is ready for work")
    yield
    print("Turning off")


app = FastAPI(lifespan=lifespan)
app.include_router(router)