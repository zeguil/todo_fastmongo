from http import HTTPStatus

from fastapi.testclient import TestClient

from todo_fastmongo.app import app
from todo_fastmongo.database import collection

client = TestClient(app)


def test_create_task():
    task_data = {
        'title': 'Teste Task',
        'description': 'Essa é uma task test',
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
        'title': 'Teste Task',
        'description': 'Essa é uma task test',
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


def test_read_tasks():
    tasks_in_db = [
        {
            'title': 'Task 1',
            'description': 'Descricao 1',
            'completed': False,
        },
        {'title': 'Task 2', 'description': 'Descricao 2', 'completed': True},
    ]
    collection.insert_many(tasks_in_db)

    response = client.get('/tasks/')
    assert response.status_code == HTTPStatus.OK

    returned_tasks = response.json()
    assert type(returned_tasks) is list
    assert len(returned_tasks) == len(tasks_in_db)
