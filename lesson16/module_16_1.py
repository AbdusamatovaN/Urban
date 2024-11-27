from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def welcome() -> dict:
    return {"message": "Главная страница"}

@app.get("/user/admin")
async def admin() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def u_id(user_id : str) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user")
async def user(username : str = "Username", age : int = 0) -> dict:
    return {"message": "Информация о пользователе. Имя: <username>, Возраст: <age>"}