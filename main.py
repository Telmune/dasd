from fastapi import FastAPI

from contextlib import asynccontextmanager
from router import router as task_router
from datebase import create_tables, delete_tables



@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('delete tables')
    await create_tables()
    print('create tables')
    yield
    print('close app')

app = FastAPI(lifespan=lifespan)
app.include_router(task_router)
