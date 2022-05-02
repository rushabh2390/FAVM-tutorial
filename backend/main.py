from typing import Collection
from fastapi import FastAPI, HTTPException, responses
from fastapi.middleware.cors import CORSMiddleware
from model import Todo

#App Object
app = FastAPI()
origins = ["*"]

from database import(
    remove_todo,
    update_todo,
    create_todo,
    fetch_all_todos,
    fetch_on_todo,
     
)


app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/")
def read_root():
    return{"Welcome to Fast api as backend"}

@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos()
    return response 

@app.get("/api/todo{title}",response_model=Todo)
async def get_todo_by_title(title):
    response = await fetch_on_todo(title)
    if response:
        return response
    raise HTTPException(404,f"There is no TODO item with this title {title}")
    

@app.post("/api/todo", response_model=Todo)
async def post_todo(todo:Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400,"Something went wrong/ Bad Request")

@app.put("/api/todo{title }", response_model=Todo)
async def put_todo(title:str,desc:str ):
    response = await update_todo(title,desc)
    if response:
        return response
    raise HTTPException(404,f"There is no TODO item with this title {title}")
    

@app.delete("/api/todo/{title}")
async def delete_todo(title):
    response = await remove_todo(title)
    if response:
        return "successfully deleted todo Item!"
    raise HTTPException(404,f"There is no TODO item with this title {title}")