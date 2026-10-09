from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Task Tracker API")


class TaskCreate(BaseModel):
    title: str = Field(min_length=1)
    completed: bool = False


class Task(TaskCreate):
    id: int


tasks: dict[int, Task] = {}
next_task_id = 1


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    return list(tasks.values())


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    # TODO: create a task, store it, and assign a unique ID
    raise NotImplementedError


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    # TODO: return the task, or raise HTTPException with status code 404
    raise NotImplementedError


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: TaskCreate):
    # TODO: replace the task, or raise HTTPException with status code 404
    raise NotImplementedError


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    # TODO: delete the task, or raise HTTPException with status code 404
    raise NotImplementedError
