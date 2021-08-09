from application import app
from mongo_database import collection
from flask import request
from application.mongo_utils import MongoFilter as Database


@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World!'

@app.route('/books', methods=["GET"])
def books():
    query_strings = request.args.to_dict()
    return Database.filter_books(collection, query_strings)

@app.route('/books/<int:book_id>', methods=["GET"])
def books_id(book_id):
    filter = {"id": book_id}
    return Database.filter_books(collection, filter)

