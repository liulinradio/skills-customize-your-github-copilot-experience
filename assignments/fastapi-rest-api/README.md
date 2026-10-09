# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small task-tracking REST API with FastAPI. Practice defining request and response models, handling HTTP methods and status codes, and testing endpoints through the automatically generated API documentation.

## 📝 Tasks

### 🛠️ Define the API and Task Model

#### Description
Install FastAPI and Uvicorn, then complete the task data model in `main.py`. Start the server and explore the interactive documentation FastAPI provides.

#### Requirements
Completed program should:

- Install dependencies with `python -m pip install fastapi uvicorn`
- Define a task with an integer `id`, a non-empty `title`, and a `completed` value that defaults to `False`
- Store tasks in the provided in-memory dictionary
- Start the server with `uvicorn main:app --reload` and open `http://127.0.0.1:8000/docs`


### 🛠️ Create and Read Tasks

#### Description
Implement endpoints for creating tasks and reading all tasks or one task by its ID. Use the interactive API documentation to send requests and inspect responses.

#### Requirements
Completed program should:

- Create a task with `POST /tasks` and return its assigned ID and task data
- Return all tasks with `GET /tasks`
- Return one task with `GET /tasks/{task_id}`
- Return an HTTP 404 response when a requested task ID does not exist


### 🛠️ Update and Delete Tasks

#### Description
Complete the remaining endpoints so clients can replace a task's details or remove a task. Check that each operation returns an appropriate response.

#### Requirements
Completed program should:

- Replace a task's title and completion state with `PUT /tasks/{task_id}`
- Delete a task with `DELETE /tasks/{task_id}` and return HTTP 204 when successful
- Return HTTP 404 when an update or delete request targets a task ID that does not exist
- Confirm the create, read, update, and delete operations work in `/docs`
