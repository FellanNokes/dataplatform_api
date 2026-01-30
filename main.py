import requests

from typing import Union
from fastapi import FastAPI, status, HTTPException

from schema.fox import FoxSchema
from schema.user import UserSchema, UserSchemaResponse

userList: list[UserSchema] = [
    UserSchema(username="Benny", password="123", isEnabled=True),
    UserSchema(username="Frida", password="321", isEnabled=True),
    UserSchema(username="Tommy", password="abc", isEnabled=False),
]
app = FastAPI(title="My first API APP")


@app.get("/")
def root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")  # localhost:8000/items/248?color=black
def get_item(item_id: int, color: Union[str, None] = None):
    return {"item_id": item_id, "color": color}

@app.get("/users", response_model=list[UserSchemaResponse])
def get_users() -> list[UserSchemaResponse]:
    return userList # TODO: Check this out later

@app.post(
    "/users",
    response_model=UserSchema,
    status_code=status.HTTP_201_CREATED
)
def post_user(user: UserSchema) -> UserSchema:
    userList.append(user)
    return user

@app.delete("/users/{username}", status_code=status.HTTP_200_OK)
def delete_user(username: str) -> dict[str, str]:
    for user in userList:
        if user.username == username:
            userList.remove(user)
            return {"message": "User deleted"}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )

@app.get("/fox", response_model=FoxSchema)
def get_fox() -> FoxSchema:
    response = requests.get("https://randomfox.ca/floof/")
    result_json = response.json()

    fox = FoxSchema(**result_json) # Convert JSON -> Python Object

    return fox
