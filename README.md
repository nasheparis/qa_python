# qa_python

1. test_add_new_book_add_two_books - тест проверяет, что можно добавить 2 книги (исправленный прекод)

2. test_add_new_book_with_long_name - тест проверяет, что книга с названием длиннее 40 символов не добавляется в список

3. test_add_new_book_twice - тест проверяет, что из двух книг с одинаковым названием, в список добавляется только одна

4. test_set_book_genre_add_existing_genre - тест проверяет, что жанр добавился к названию книги

5. test_set_book_genre_add_not_existing_genre - тест проверяет, что несуществующий жанр не добавляется к названию книги
   
6. test_get_book_genre_add_existing_genre - тест проверяет, что добавленный жанр соответствует добавляемому

7. test_get_books_with_specific_genre_positive - тест проверяет, что длина списка книг с определенным жанром совпадает с
   количеством книг

8. test_get_books_genre_positive - тест проверяет, что текущий словарь содержит добавленные книги

9. test_get_books_for_children_positive - тест проверяет, что при запросе списка детских книг в нем содержатся
   соответствующие книги

10. test_add_book_in_favorites_positive - тест проверяет, что книга добавляется в избранное

11. test_delete_book_from_favorites_positive - тест проверяет, что удалена из избранного

12. test_get_list_of_favorites_books_positive - тест проверяет, что в списке избранных книг содержатся добавленные книги
    