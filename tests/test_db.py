def test_mongo_connection(mongo_client):
    db = mongo_client['todo_db']
    collection = db['tasks']
    assert db.name == 'todo_db'
    assert collection.name == 'tasks'
