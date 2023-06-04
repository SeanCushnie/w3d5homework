from models.book import *

book1 = Book("'Salmon'", "Whiskers, The Cat", "Non-Fiction", True)
book2 = Book("'Salmon 2'", "Whiskers, The Cat", "Non-Fiction", True)
book3 = Book("'Salmon 3: With a Vengeance'", "Whiskers, The Cat", "Fiction", False)
book4 = Book("'Salmon 4: Live Free or Cat Hard'", "Whiskers, The Cat", "Fiction", False)
book5 = Book("'Salmon 5: A Good Day to Cat Hard'", "Whiskers, The Cat", "Fiction", False)

book_list = [book1, book2, book3, book4, book5]

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