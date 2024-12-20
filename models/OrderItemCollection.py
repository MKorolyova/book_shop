from .db import dbConnection;
from .db import cursor;
from models.OrderItem import OrderItem

# create objekt in function OrderItem 

class OrderItemCollection:
    def __init__(self):
        self.sql = None
        self.where = None
        self.order = None
        self.limit = None
        self.offset = None
        self.data = []

    def load(self, filter=None):

        self.build_sql()
        if not self.sql:
            return

        cursor.execute(self.sql)
        columns = cursor.description
        values_array = cursor.fetchall()


        values_array = [values for values in values_array if any(value is not None for value in values)]


        if  values_array:
            for values in values_array:
                result = {}
                for (index, value) in enumerate(values):
                    result[columns[index][0]] = value

                order_item = OrderItem()
                order_item.from_dict(result)
                self.data.append(order_item)

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
        self.sql = """SELECT Books.book_id, Order_item.order_id, Order_item.order_item_id, Order_item.quantity
                      FROM Orders  LEFT JOIN Order_item ON Orders.order_id = Order_item.order_id  LEFT JOIN Books ON  Books.book_id=Order_item.book_id"""

        if self.where:
            self.addWhere()

        if self.order:
            self.addOrder()

        if self.limit:
            self.addLimit()

            if self.offset:
                self.addOffset()
   
    def to_dict(self):
        return [order_item.to_dict() for order_item in self.data]