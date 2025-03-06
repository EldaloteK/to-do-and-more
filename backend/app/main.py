from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Success": "OK"}


@app.get("/tasks")
def get_tasks():
    return [{"task_id": "1", "text": "Buy Groceries", "done": False}]
