import pytest
from pymongo import MongoClient

from todo_fastmongo.database import collection


@pytest.fixture()
def mongo_client():
    client = MongoClient('mongodb://localhost:27017/')
    yield client
    client.close()


@pytest.fixture(autouse=True)
def _cooncetion_mongo_tests():
    collection.delete_many({})
    yield
    collection.delete_many({})
