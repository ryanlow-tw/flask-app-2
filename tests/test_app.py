import requests
import pytest


def test_should_return_index_page():

    rv = requests.get('http://localhost:5000/')

    assert "Index Page" == rv.text

def test_should_return_hello_world():

    rv = requests.get('http://localhost:5000/hello')

    assert "Hello World" == rv.text

