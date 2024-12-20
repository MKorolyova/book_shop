import uuid
from models.Book import Book
from .db import dbConnection, cursor

# create as field Book 

class OrderItem:
    def __init__(self):
        self.order_item_id = None
        self.order_id = None
        self.quantity = None
        self.book = Book()
     
    def load(self, id):
        sql = "SELECT * FROM Order_item WHERE Order_item.order_item_id = %s;"
        cursor.execute(sql, (id,))

        values = cursor.fetchone()
        columns = cursor.description
        result = {}

        if values:
            for (index, value) in enumerate(values):
                result[columns[index][0]] = value

            self.order_item_id = result["order_item_id"]
            self.order_id = result["order_id"]
            self.quantity = result["quantity"]
            self.book.load(result["book_id"]) 
    
        result = None   
        return self
    
    def delete(self):
        if self.order_item_id:
            sql = "DELETE FROM Order_item WHERE order_item_id = %s"
            cursor.execute(sql, (self.order_item_id,))
            dbConnection.commit()
    
    def save(self):
        if self.book and self.order_id and not self.order_item_id:   
            self.order_item_id = int(uuid.uuid4().int % 2147483647) 
            self.quantity = 1
            sql = "INSERT INTO Order_item (order_item_id, order_id, book_id, quantity, price) VALUES (%s, %s, %s, %s, %s)"
            values = (self.order_item_id, self.order_id, self.book.book_id, self.quantity, self.book.price)

            cursor.execute(sql, values)
            dbConnection.commit()

    def set_book(self, book_id):
        self.book.load(book_id)
        return self

    def set_order_id(self, order_id):
        self.order_id = order_id
        return self


    def to_dict(self):
        return {
            'order_item_id': self.order_item_id,
            'order_id': self.order_id,
            'book': self.book.to_dict(),
            'quantity': self.quantity
        }
    
    
    def from_dict(self, data):

        self.order_item_id = data["order_item_id"]
        self.order_id = data["order_id"]
        self.book.load(data["book_id"])
        self.quantity = data["quantity"]

        return self
    