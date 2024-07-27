from main import BooksCollector


class TestBooksCollector:
    def setUp(self):
        self.collector = BooksCollector()

    def test_add_new_book(self):
        self.collector.add_new_book("The Shining")
        self.assertIn("The Shining", self.collector.books_genre)

        # Проверяем, что нельзя добавить книгу с именем длиннее 40 символов
        long_book_name = "A" * 41
        self.collector.add_new_book(long_book_name)
        self.assertNotIn(long_book_name, self.collector.books_genre)

        # Проверяем, что нельзя добавить одну и ту же книгу дважды
        self.collector.add_new_book("The Shining")
        self.assertEqual(len(self.collector.books_genre), 1)

    def test_set_book_genre(self):
        self.collector.add_new_book("The Shining")
        self.collector.set_book_genre("The Shining", "Ужасы")
        self.assertEqual(self.collector.get_book_genre("The Shining"), "Ужасы")

        # Проверяем, что нельзя установить несуществующий жанр
        self.collector.set_book_genre("The Shining", "Приключения")
        self.assertEqual(self.collector.get_book_genre("The Shining"), "Ужасы")
        
from main import BooksCollector

class TestBooksCollector:
    def setUp(self):
        self.collector = BooksCollector()

    def test_add_new_book(self):
        self.collector.add_new_book("The Shining")
        assert "The Shining" in self.collector.books_genre

    def test_set_book_genre(self):
        self.collector.add_new_book("The Shining")
        self.collector.set_book_genre("The Shining", "Horror")
        assert self.collector.get_book_genre("The Shining") == "Horror"

    def test_get_books_with_specific_genre(self):
        self.collector.add_new_book("The Shining")
        self.collector.set_book_genre("The Shining", "Horror")
        self.collector.add_new_book("The Godfather")
        self.collector.set_book_genre("The Godfather", "Crime")
        assert "The Shining" in self.collector.get_books_with_specific_genre("Horror")
        assert "The Godfather" in self.collector.get_books_with_specific_genre("Crime")

    def test_get_books_for_children(self):
        self.collector.add_new_book("The Shining")
        self.collector.set_book_genre("The Shining", "Horror")
        self.collector.add_new_book("The Godfather")
        self.collector.set_book_genre("The Godfather", "Crime")
        self.collector.add_new_book("Toy Story")
        self.collector.set_book_genre("Toy Story", "Cartoons")
        assert "Toy Story" in self.collector.get_books_for_children()
        assert "The Shining" not in self.collector.get_books_for_children()
        assert "The Godfather" not in self.collector.get_books_for_children()

    def test_add_and_delete_book_from_favorites(self):
        self.collector.add_new_book("The Shining")
        self.collector.add_book_in_favorites("The Shining")
        assert "The Shining" in self.collector.get_list_of_favorites_books()
        self.collector.delete_book_from_favorites("The Shining")
        assert "The Shining" not in self.collector.get_list_of_favorites_books()