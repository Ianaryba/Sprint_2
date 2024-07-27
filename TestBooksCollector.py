import pytest
from main import BooksCollector
@pytest.fixture
def collector():
    return BooksCollector()

def test_add_new_book(collector):
    collector.add_new_book("Book1")
    assert "Book1" in collector.get_books_genre()
    assert collector.get_books_genre()["Book1"] == ''

def test_add_new_book_with_invalid_name(collector):
    collector.add_new_book("")
    collector.add_new_book("A" * 41)
    assert "" not in collector.get_books_genre()
    assert "A" * 41 not in collector.get_books_genre()

@pytest.mark.parametrize("book, genre", [
    ("Book1", "Фантастика"),
    ("Book2", "Ужасы"),
    ("Book3", "Детективы")
])
def test_set_book_genre(collector, book, genre):
    collector.add_new_book(book)
    collector.set_book_genre(book, genre)
    assert collector.get_book_genre(book) == genre

def test_set_invalid_book_genre(collector):
    collector.add_new_book("Book1")
    collector.set_book_genre("Book1", "Invalid Genre")
    assert collector.get_book_genre("Book1") == ''

def test_get_book_genre(collector):
    collector.add_new_book("Book1")
    collector.set_book_genre("Book1", "Фантастика")
    assert collector.get_book_genre("Book1") == "Фантастика"

@pytest.mark.parametrize("genre, expected_books", [
    ("Фантастика", ["Book1"]),
    ("Ужасы", ["Book2"]),
    ("Детективы", ["Book3"])
])
def test_get_books_with_specific_genre(collector, genre, expected_books):
    collector.add_new_book("Book1")
    collector.add_new_book("Book2")
    collector.add_new_book("Book3")
    collector.set_book_genre("Book1", "Фантастика")
    collector.set_book_genre("Book2", "Ужасы")
    collector.set_book_genre("Book3", "Детективы")
    assert collector.get_books_with_specific_genre(genre) == expected_books

def test_get_books_genre(collector):
    collector.add_new_book("Book1")
    collector.add_new_book("Book2")
    assert collector.get_books_genre() == {"Book1": "", "Book2": ""}

def test_get_books_for_children(collector):
    collector.add_new_book("Book1")
    collector.add_new_book("Book2")
    collector.set_book_genre("Book1", "Фантастика")
    collector.set_book_genre("Book2", "Ужасы")
    assert collector.get_books_for_children() == ["Book1"]

def test_add_book_in_favorites(collector):
    collector.add_new_book("Book1")
    collector.add_book_in_favorites("Book1")
    assert "Book1" in collector.get_list_of_favorites_books()

def test_delete_book_from_favorites(collector):
    collector.add_new_book("Book1")
    collector.add_book_in_favorites("Book1")
    collector.delete_book_from_favorites("Book1")
    assert "Book1" not in collector.get_list_of_favorites_books()

def test_get_list_of_favorites_books(collector):
    collector.add_new_book("Book1")
    collector.add_new_book("Book2")
    collector.add_book_in_favorites("Book1")
    assert collector.get_list_of_favorites_books() == ["Book1"]