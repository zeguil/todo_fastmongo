from http import HTTPStatus

from fastapi.testclient import TestClient

from todo_fastmongo.app import app
from todo_fastmongo.database import collection

client = TestClient(app)


def test_create_task():
    task_data = {
        'title': 'Test Task',
        'description': 'This is a test task',
        'completed': False,
    }

    response = client.post('/tasks/', json=task_data)
    assert response.status_code == HTTPStatus.OK

    data = response.json()
    assert data['title'] == task_data['title']
    assert data['description'] == task_data['description']
    assert data['completed'] == task_data['completed']
    assert 'created_at' in data


def test_create_task_is_none():
    task_data = {
        'title': 'Test Task',
        'description': 'This is a test task',
        'completed': False,
    }

    db_task = collection.find_one({'title': task_data['title']})
    assert db_task is None

    response = client.post('/tasks/', json=task_data)
    assert response.status_code == HTTPStatus.OK

    db_task = collection.find_one({'title': task_data['title']})
    assert db_task is not None
    assert db_task['title'] == task_data['title']
    assert db_task['description'] == task_data['description']
    assert db_task['completed'] == task_data['completed']
    assert 'created_at' in db_task
