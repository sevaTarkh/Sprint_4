from main import BooksCollector
import pytest

class TestBooksCollector:
    
    # тест 1 метода add_new_book
    def test_add_new_book_two_books_books_added(self):
        biblioteka = BooksCollector()

        biblioteka.add_new_book('Война и мир')
        biblioteka.add_new_book('Тихий Дон')

        assert (len(biblioteka.books_genre) == 2 and 
                'Война и мир' in biblioteka.books_genre and 
                'Тихий Дон' in biblioteka.books_genre)
    
    # тест 2 метода add_new_book
    def test_add_new_book_same_book_book_not_added(self):
        biblioteka = BooksCollector()

        biblioteka.add_new_book('Война и мир')
        biblioteka.add_new_book('Война и мир')

        assert len(biblioteka.books_genre) == 1
    
    # тест 3 метода add_new_book
    def test_add_new_book_book_with_42_symbols_book_not_added(self):
        biblioteka = BooksCollector()

        biblioteka.add_new_book('Тень ветра. Кладбище забытых книг. Книга 1')

        assert len(biblioteka.books_genre) == 0

    # тест 4 метода set_book_genre
    def test_set_book_genre_book_genre_genre_added(self):
        biblioteka = BooksCollector()

        book_name = 'Война и мир'
        book_genre = 'Ужасы'

        biblioteka.add_new_book(book_name)
        biblioteka.set_book_genre(book_name, book_genre)

        assert biblioteka.books_genre[book_name] == book_genre


    # тест 5 метода set_book_genre
    def test_set_book_genre_random_genre_correct_book_genre_not_added(self):
        biblioteka = BooksCollector()

        book_1_name = 'Война и мир'
        book_genre = 'Драма'

        biblioteka.add_new_book(book_1_name)
        biblioteka.set_book_genre(book_1_name, book_genre)

        assert biblioteka.books_genre[book_1_name] != book_genre


    # тест 6 метода get_book_genre
    def test_get_book_genre_book_get_genre(self):
        biblioteka = BooksCollector()

        book_1_name = 'Война и мир'
        book_genre = 'Ужасы'
        biblioteka.add_new_book(book_1_name)
        biblioteka.set_book_genre(book_1_name, book_genre)

        assert biblioteka.get_book_genre(book_1_name) == book_genre

    # тест 7 метода get_books_with_specific_genre
    @pytest.mark.parametrize('genre, correct_books', [
        ('Ужасы', ['Война и мир', 'Тихий Дон']),
        ('Комедии', ['Мертвые души']),
        ('Детективы', [])
    ])
    def test_get_books_with_specific_genre_genre_array_books(self, genre, correct_books):
        biblioteka = BooksCollector()

        books = [
            ('Война и мир', 'Ужасы'),
            ('Тихий Дон', 'Ужасы'),
            ('Мертвые души', 'Комедии')
        ]
        for book, book_genre in books:
            biblioteka.add_new_book(book)
            biblioteka.set_book_genre(book, book_genre)

        assert biblioteka.get_books_with_specific_genre(genre) == correct_books

    #тест 8 метода get_books_genre
    @pytest.mark.parametrize('books, result',[
        ([('Война и мир', 'Ужасы')], {'Война и мир': 'Ужасы'}),
        ([('Война и мир', 'Ужасы'), ('Тихий Дон', 'Комедии')], {'Война и мир': 'Ужасы', 'Тихий Дон': 'Комедии'})
    ])
    def test_get_books_genre_books_books_genre(self, books, result):
        biblioteka = BooksCollector()

        for book, genre in books:
            biblioteka.add_new_book(book)
            biblioteka.set_book_genre(book, genre)

        assert biblioteka.get_books_genre() == result

    #тест 9 метода get_books_for_children
    @pytest.mark.parametrize('books, result',[
        ([('Война и мир', 'Ужасы')], []),
        ([('Война и мир', 'Ужасы'), ('Тихий Дон', 'Комедии')], ['Тихий Дон'])
    ])
    def test_get_books_for_children_books_genre_children_books(self, books, result):
        biblioteka = BooksCollector()

        for book, genre in books:
            biblioteka.add_new_book(book)
            biblioteka.set_book_genre(book, genre)

        assert biblioteka.get_books_for_children() == result

    # тест 10 метода add_book_in_favorites
    def test_add_book_in_favorites_book_book_added_in_favorites(self):
        biblioteka = BooksCollector()

        book_1_name = 'Война и мир'
        biblioteka.add_new_book(book_1_name)
        biblioteka.add_book_in_favorites(book_1_name)

        assert book_1_name in biblioteka.favorites
        
    #тест 11 метода delete_book_from_favorites
    def test_delete_book_from_favorites_book_name_book_deleted(self):
        biblioteka = BooksCollector()

        book_1_name = 'Война и мир'
        biblioteka.add_new_book(book_1_name)
        biblioteka.add_book_in_favorites(book_1_name)
        biblioteka.delete_book_from_favorites(book_1_name)

        assert (len(biblioteka.favorites) == 0 and
                book_1_name not in biblioteka.favorites)
        

    #тест 12 метода get_list_of_favorites_books
    def test_get_list_of_favorites_books_books_favorite_books(self):
        biblioteka = BooksCollector()
        books = ['Война и мир', 'Тихий Дон', 'Мертвые души']
        for book in books:
            biblioteka.add_new_book(book)
            biblioteka.add_book_in_favorites(book)

        assert biblioteka.get_list_of_favorites_books() == biblioteka.favorites == books
