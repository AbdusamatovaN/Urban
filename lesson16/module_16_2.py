from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()
@app.get("/")
async def welcome() -> dict:
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def admin() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def u_id(user_id : Annotated[int, Path(gt=1, le=100, description='Enter User ID', example=1)]) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get('/user/{username}/{age}')
async def user(username : Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example= 'UrbanUser')],
               age : Annotated[int, Path(gt=18, le=120, description='Enter age', example=24)]) -> dict:
    return {"message": "Информация о пользователе. Имя: <username>, Возраст: <age>"}