from models.Book import Book
from models.GenresCollection import GenresCollection
from models.BookCollection import BookCollection

# create objekt in function Book GenresCollection BookCollection

class BookController:
    
    def get_book_page_action(self, request, responce):
        book = Book()
        genres = GenresCollection()
        
        data = {}
        parameters = request.get_parameters()

        if 'book_id' in parameters:
            book_id = parameters['book_id']

            book.load(book_id)
            genres.load()
 
            responce.set_status(200)
            data = {}
            data["book"] = book.to_dict()
            data["genre"] = genres.to_dict() 
            responce.set_json(data)

        return responce
    
    def get_book_by_genre_page_action(self, request, responce):
        bookCollection = BookCollection()
        genres = GenresCollection()
        
        data = {}

        parameters = request.get_parameters()

        if 'genre_id' in parameters:
            genre_id = parameters['genre_id']

            bookCollection.set_where({'genre_id': genre_id})
            bookCollection.set_order({'price': 'asc'})
            bookCollection.load()
            genres.load()

            responce.set_status(200)
            data["book"] = bookCollection.to_dict()
            data["genre"] = genres.to_dict() 
            responce.set_json(data)

        return responce
    
    def get_book_by_random_page_action(self, request, responce):
        bookCollection = BookCollection()
        genres = GenresCollection()
        
        data = {}

        parameters = request.get_parameters()

        if 'limit' in parameters:
            limit = parameters['limit']

            bookCollection.set_limit(limit)
            bookCollection.set_order({'price': 'asc'})
            bookCollection.load()
            genres.load()

            responce.set_status(200)
            data["book"] = bookCollection.to_dict()
            data["genre"] = genres.to_dict() 

            responce.set_json(data)

        return responce

