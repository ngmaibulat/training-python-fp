from __future__ import annotations
import requests
from pydantic import BaseModel


BASE_URL = "https://todo.pixegami.io"


class RootPage(BaseModel):
    message: str


class Task(BaseModel):
    content: str
    user_id: str
    task_id: str
    is_done: bool


def test_root_page():
    res = requests.get(BASE_URL)
    json = res.json()
    # check header content type
    assert res.status_code == 200
    assert res.headers["Content-Type"] == "application/json"
    assert "message" in json
    assert json["message"] == "Hello World from Todo API"
    assert res.text == '{"message":"Hello World from Todo API"}'

    model_instance = RootPage.parse_obj(json)
    model_instance.validate(model_instance)


def test_create_task():
    url = f"{BASE_URL}/create-task"

    # data = {
    #     "content": "write tests",
    #     "user_id": "pythondev",
    #     "task_id": "task-001",
    #     "is_done": False,
    # }

    task_instance = Task(
        content="write tests", user_id="pythondev", task_id="task-001", is_done=False
    )

    # Convert the task instance to a dictionary
    data = task_instance.dict()

    res = requests.put(url, json=data)
    json = res.json()

    assert res.status_code == 200
    assert res.headers["Content-Type"] == "application/json"
    assert "task" in json
    assert "content" in json["task"]
    assert "task_id" in json["task"]
    assert "created_time" in json["task"]
    assert "ttl" in json["task"]
    # assert res.text == '{"message":"Hello World from Todo API"}'

    task_id = json["task"]["task_id"]
    url = f"{BASE_URL}/get-task/{task_id}"
    res = requests.get(url)
    json = res.json()
    assert res.status_code == 200
    assert res.headers["Content-Type"] == "application/json"
    assert "content" in json
    assert "task_id" in json
    assert json["task_id"] == task_id
