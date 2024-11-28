from fastapi import FastAPI
from routers.user import user
from routers.task import task

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "Welcome to Taskmanager"}

app.include_router(user)
app.include_router(task)
