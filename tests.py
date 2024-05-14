import pytest

from main import BooksCollector


class TestBooksCollector:
    # тест проверяет, что можно добавить 2 книги
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # тест проверяет, что книга с названием длиннее 40 символов не добавляется в список
    def test_add_new_book_with_long_name(self):
        collector = BooksCollector()

        collector.add_new_book('Странная история доктора Джекила и мистера Хайда')
        assert collector.get_books_genre() == {}

    # тест проверяет, что из двух книг с одинаковым названием, в список добавляется только одна
    def test_add_new_book_twice(self):
        collector = BooksCollector()

        book_name = 'Шерлок Холмс'
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 1

    # тест проверяет, что жанр добавился к названию книги
    @pytest.mark.parametrize(
        'book_names, book_genres',
        [
            ['Дюна', 'Фантастика'],
            ['Оно', 'Ужасы'],
            ['Десять негритят', 'Детективы'],
            ['Маленький принц', 'Мультфильмы'],
            ['Вторая жизнь Уве', 'Комедии']
        ],
        ids=[
            'Test for book1',
            'Test for book2',
            'Test for book3',
            'Test for book4',
            'Test for book5'
        ]
    )
    def test_set_book_genre_add_existing_genre(self, book_names, book_genres):
        collector = BooksCollector()

        book = book_names
        collector.add_new_book(book)

        genre = book_genres
        collector.set_book_genre(book, genre)
        assert collector.get_book_genre(book) == genre

    # тест проверяет, что несуществующий жанр не добавляется к названию книги
    def test_set_book_genre_add_not_existing_genre(self):
        collector = BooksCollector()

        book = 'Молчание ягнят'
        collector.add_new_book(book)

        genre = 'Триллер'
        collector.set_book_genre(book, genre)
        assert collector.get_book_genre(book) == ''

    # тест проверяет, что добавленный жанр соответствует добавляемому
    def test_get_book_genre_add_existing_genre(self):
        collector = BooksCollector()

        book = 'Война миров'
        collector.add_new_book(book)

        genre = 'Фантастика'
        collector.set_book_genre(book, genre)

        assert collector.get_book_genre(book) == 'Фантастика'

    # тест проверяет, что длина списка книг с определенным жанром совпадает с количеством книг
    def test_get_books_with_specific_genre_positive(self):
        collector = BooksCollector()

        genre = 'Фантастика'
        books = ['Война миров', 'Дюна', 'Автостопом по Галактике']

        for book_name in books:
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name, genre)

        assert len(collector.get_books_with_specific_genre(genre)) == len(books)

    # тест проверяет, что текущий словарь содержит добавленные книги
    def test_get_books_genre_positive(self):
        collector = BooksCollector()

        collector.books_genre = {'Десять негритят': 'Детективы',
                                 'Маленький принц': 'Мультфильмы',
                                 'Вторая жизнь Уве': 'Комедии'}

        assert collector.get_books_genre() == {'Десять негритят': 'Детективы',
                                               'Маленький принц': 'Мультфильмы',
                                               'Вторая жизнь Уве': 'Комедии'}

    # тест проверяет, что при запросе списка детских книг в нем содержатся соответствующие книги
    def test_get_books_for_children_positive(self):
        collector = BooksCollector()

        collector.books_genre = {'Десять негритят': 'Детективы',
                                 'Маленький принц': 'Мультфильмы',
                                 'Оно': 'Ужасы'}

        assert collector.get_books_for_children() == ['Маленький принц']

        # тест проверяет, что книга добавляется в избранное

    def test_add_book_in_favorites_positive(self):
        collector = BooksCollector()

        collector.books_genre = {'Десять негритят': 'Детективы'}
        collector.add_book_in_favorites('Десять негритят')
        assert collector.get_list_of_favorites_books() == ['Десять негритят']

    # тест проверяет, что удалена из избранного
    def test_delete_book_from_favorites_positive(self):
        collector = BooksCollector()
        collector.favorites = ['Шерлок Холмс']
        collector.delete_book_from_favorites('Шерлок Холмс')
        assert collector.get_list_of_favorites_books() == []

    # тест проверяет, что в списке избранных книг содержатся добавленные книги
    def test_get_list_of_favorites_books_positive(self):
        collector = BooksCollector()
        collector.favorites = ['Война миров', 'Автостопом по галактике']
        assert len(collector.get_list_of_favorites_books()) == 2
