from models.book import *

book1 = Book("The Hound of the Baskervilles", "Sir Arthur Conan Doyle", "Horror", True)
book2 = Book("The Outsider", "Stephen King", "Horror / Thriller", False)

book_list = [book1, book2]

def add_new_book(book):
    book_list.append(book)

def remove_book(book):
    item_to_delete = None
    for item in book_list:
        if item.title == book.title and item.author == book.author:
            item_to_delete = item
            break
    if item_to_delete:
        book_list.remove(item_to_delete)
            

def delete_book_by_index(index):
    if 0 <= index < len(book_list):
        book_list.pop(index)