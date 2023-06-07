import requests


def test_todo():
    res = requests.get("https://todo.pixegami.io")
    assert res.status_code == 200
    assert res.text == '{"message":"Hello World from Todo API"}'
    pass
