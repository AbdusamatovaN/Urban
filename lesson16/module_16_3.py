from fastapi import FastAPI

app = FastAPI()
users = {1: 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_users() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def new_user(username: str, age: int) -> str:
    user_id = max(users) + 1 if users else 1
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"

@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> str:
    users.pop(user_id)
    return f"The user {user_id} was deleted"

