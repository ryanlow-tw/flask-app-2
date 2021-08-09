import os
import tempfile

import pytest

from application import app

@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_should_return_index_page(client):

    rv = client.get('/')

    assert b"Index Page" == rv.data

def test_should_return_hello_world(client):

    rv = client.get('/hello')

    assert b"Hello World!" == rv.data