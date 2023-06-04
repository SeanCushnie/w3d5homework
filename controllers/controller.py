from flask import render_template, request, redirect
from app import app
from models.book import Book
from models.book_list import book_list, add_new_book, remove_book, delete_book_by_index

@app.route("/")
def index():
    titles = []
    for item in book_list:
        titles.append(item.title)
    book = None
    return render_template("index.html", book_list = book_list, titles = titles, book = book)

@app.route("/", methods=["POST"])
def add_book():
    book_title = request.form["title"]
    book_author = request.form["author"]
    book_genre = request.form["genre"]
    book_checked_out = request.form.get("checked_out", False)
    book = Book(book_title, book_author, book_genre, book_checked_out)
    add_new_book(book)
    return redirect("/")

@app.route('/books/<index>')
def show_book(index):
    chosen_book = book_list[int(index)]
    return render_template("book.html", book = chosen_book)

@app.route("/books/del/<index>", methods = ["POST"])
def delete_by_index(index):
    delete_book_by_index(int(index))
    return redirect("/")