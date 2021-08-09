import requests
import pytest


def test_should_return_index_page():
    rv = requests.get('http://localhost:5000/')

    assert "Index Page" == rv.text


def test_should_return_hello_world():
    rv = requests.get('http://localhost:5000/hello')

    assert "Hello World!" == rv.text


def test_should_return_books_containing_row():
    r = requests.get('http://localhost:5000/books?author=mey')
    json_object = r.json()
    author_name = json_object['results'][0]['author'].lower()

    assert 200 == r.status_code
    assert "mey" in author_name


def test_should_return_books_containing_exact_price():
    r = requests.get("http://localhost:5000/books?price=3409")
    json_object = r.json()
    price = int(json_object['results'][0]["price"])

    assert 200 == r.status_code
    assert 3409 == price


def test_should_return_books_containing_language_code():
    r = requests.get("http://localhost:5000/books?language_code=en")

    json_object = r.json()
    language = json_object['results'][0]['language_code'].lower()
    assert 200 == r.status_code
    assert "en" in language


def test_should_return_books_containing_isbn():
    r = requests.get("http://localhost:5000/books?isbn=316")

    json_object = r.json()
    isbn = json_object['results'][0]['isbn']
    assert 200 == r.status_code
    assert "316" in isbn


def test_should_return_books_containing_isbn13():
    r = requests.get("http://localhost:5000/books?isbn13=978")
    json_object = r.json()
    isbn = json_object['results'][0]['isbn13']
    assert 200 == r.status_code
    assert "978" in isbn


def test_that_route_returns_average_rating():
    r = requests.get("http://localhost:5000/books/ratings?param=average")
    json_object = r.json()
    average = json_object['mean']
    assert 200 == r.status_code
    assert average == 4.01
