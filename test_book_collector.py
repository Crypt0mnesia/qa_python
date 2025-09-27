import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize('book_name, expected', [
        ('', False),
        ('a', True),
        ('a' * 2, True),
        ('Серединка книжки', True),
        ('a' * 39, True),
        ('a' * 40, True),
        ('a' * 41, False)

    ])
    def test_add_new_book_boundary_cases(self, collector, book_name, expected):
        collector.add_new_book(book_name)
        assert (book_name in collector.get_books_genre()) == expected

    def test_set_book_genre(self, collector):
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Фантастика')
        assert collector.get_book_genre('Книга') == 'Фантастика'

    def test_get_book_genre(self, collector):
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Ужасы')
        assert collector.get_book_genre('Книга') == 'Ужасы'

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('Фантастика книга')
        collector.add_new_book('Ужасы книга')
        collector.set_book_genre('Фантастика книга', 'Фантастика')
        collector.set_book_genre('Ужасы книга', 'Ужасы')
        fantasy_books = collector.get_books_with_specific_genre('Фантастика')
        assert fantasy_books == ['Фантастика книга']

    def test_get_books_genre(self, collector):
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        books = collector.get_books_genre()
        assert len(books) == 2

    @pytest.mark.parametrize('book_name, genre, expected', [
        ('Ужасы', 'Ужасы', False),
        ('Детектив', 'Детективы', False),
        ('Неизвестная книжка', '', False),
        ('Фантастика', 'Фантастика', True),
        ('Мультфильм', 'Мультфильмы', True),
    ])
    def test_get_books_for_children_cases(self, collector, book_name, genre, expected):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)

        children_books = collector.get_books_for_children()
        assert (book_name in children_books) == expected

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        assert 'Книга' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.delete_book_from_favorites('Книга')
        assert 'Книга' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        favorites = collector.get_list_of_favorites_books()
        assert favorites == ['Книга']
