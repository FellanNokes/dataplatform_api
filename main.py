from typing import Union

from fastapi import FastAPI

app = FastAPI(title="My first API APP")

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/items/{item_id}") # localhost:8000/items/248?color=black
def get_item(item_id: int, color: Union[str, None] = None):
    return{"item_id": item_id, "color": color}