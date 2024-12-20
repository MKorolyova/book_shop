from .db import dbConnection;
from .db import cursor;

class Book:

    def __init__(self):
        self.book_id = None
        self.author_name = None
        self.book_name = None
        self.price = None
        self.publication_year =  None
        self.publication_city = None
        self.genre = None
        self.genre_id = None
        self.description = None
        self.author_info = None
        self.review = None
    
     
    def load(self, id):

        sql = "SELECT * FROM Books WHERE Books.book_id = %s;"
        cursor.execute(sql, (id,))

        values = cursor.fetchone()
        columns = cursor.description
        result = {}

        for (index, value) in enumerate(values):
            result[columns[index][0]] = value

        self.book_id = result["book_id"]
        self.author_name = result["author_name"]
        self.book_name = result["book_name"]
        self.price = result["price"]
        self.publication_year = result["publication_year"]
        self.publication_city = result["publication_city"]
        self.genre_id =  result["genre_id"]
        self.genre =  result["genre"]
        self.description =  result["description"]
        self.author_info =  result["author_info"]
        self.review =  result["review"]
    
        result = None   
        return self
    

    def save(self):
        return self

    def to_dict(self):
        return {
            'book_id': self.book_id,
            'author_name': self.author_name,
            'book_name': self.book_name,
            'price': float(self.price),
            'publication_year': self.publication_year,
            'publication_city': self.publication_city,
            'genre_id': self.genre_id,
            'genre': self.genre,
            'description': self.description,
            'author_info': self.author_info,
            'review': self.review,
        }
    
    
    def from_dict(self, data):

        self.book_id = data["book_id"]
        self.author_name = data["author_name"]
        self.book_name = data["book_name"]
        self.price = data["price"]
        self.publication_year = data["publication_year"]
        self.publication_city = data["publication_city"]
        self.genre_id =  data["genre_id"]
        self.genre =  data["genre"]
        self.description =  data["description"]
        self.author_info =  data["author_info"]
        self.review =  data["review"]
        return self
    
