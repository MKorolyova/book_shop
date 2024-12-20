from .db import dbConnection;
from .db import cursor;
from .Book import Book;

# create objekt in function  Book 

class BookCollection:
    
    def __init__(self):
        self.sql = None
        self.where = None
        self.order = None
        self.limit = None
        self.offset = None
        self.data = [] 

    def load(self, filters=None):

        self.build_sql()
        if not self.sql:
            return

        cursor.execute(self.sql)
        columns = cursor.description
        values_array = cursor.fetchall()

        for values in values_array:
            result = {}
            for (index, value) in enumerate(values):
                result[columns[index][0]] = value
   
            book = Book()
            book.from_dict(result)
            self.data.append(book)

        return self.data
    
    def set_where(self, where):
        self.where = where
    
    def set_order(self, order):
        self.order = order

    def set_limit(self, limit):
        self.limit = limit

    def set_offset(self, offset):
        self.offset = offset

    def addWhere(self):
        keys_list = list(self.where.keys())
        val_list = list(self.where.values())
        
        conditions = []
        for key, val in zip(keys_list, val_list):
            conditions.append(f"{key} = '{val}'")
        
        if conditions:
            self.sql += " WHERE " + " AND ".join(conditions)

    def addOrder(self):
        keys_list = list(self.order.keys())
        val_list = list(self.order.values())

        conditions = []
        for key, val in zip(keys_list, val_list):
            conditions.append(f"{key} {val}")

        if conditions:
            self.sql += " ORDER BY " + ", ".join(conditions)

    def addLimit(self):
        self.sql += f" LIMIT {self.limit}"

    def addOffset(self):
        self.sql += f" LIMIT {self.offset}"


    def build_sql(self):
        self.sql = "SELECT * FROM Books"

        if self.where:
            self.addWhere()

        if self.order:
            self.addOrder()

        if self.limit:
            self.addLimit()

            if self.offset:
                self.addOffset()
   
    def to_dict(self):
        return [book.to_dict() for book in self.data]