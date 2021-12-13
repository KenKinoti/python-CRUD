from typing import Optional

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Dunia"}

@app.post("/todo")
def create_item():
    return {"Create todo item"}

@app.get("/todo/{id}")
def read_todo(id: int, q: Optional[str] = None):
    return {"item_id": id, "q": q}

@app.put("/todo/{id}")
def update_todo(id: int):
    return {"Update the todo item with id {id}"}

@app.delete("/")
def delete_todo(id: int):
    return {"Delete todo item with id {id}"}

