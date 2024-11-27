from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    age: int

app = FastAPI()
users = []

@app.get("/users", response_model=List[User])
async def get_users():
    return users

@app.post('/user/{username}/{age}')
async def new_user(username: str, age: int):
    user_id = len(users) + 1 if users else 1
    user = User(id = user_id, username = username, age = age)
    users.append(user)
    return user

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int):
    try:
        user = User(id=user_id, username=username, age=age)
        users[user_id - 1] = user
        return user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> str:
    try:
        user = users[user_id - 1]
        users.pop(user_id)
        return user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")

