from fastapi import FastAPI, Path
app = FastAPI()


@app.get("/")
async def root():
    return "Главная страница"


@app.get("/user/admin")
async def admin_root():
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def users_root(user_id: int = Path(ge=1, le=100, description="Enter User ID", examples="27")):
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user/{username}/{age}")
async def users_info(username: str = Path(min_length=5, max_length=20, description="Enter username", examples="Tatiana"),
                     age: int = Path(ge=18, le=120, description="Enter age", examples="35")):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"