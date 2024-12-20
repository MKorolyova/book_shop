import uuid
from datetime import datetime, timedelta
from .db import dbConnection, cursor

class Order:
    def __init__(self):
        self.order_id = None
        self.customer_id = None
        self.first_name = None
        self.last_name = None
        self.address =  None
        self.postal_zip = None
        self.city = None
        self.country = None
        self.total = None
        self.create_date = None
        self.update_date = None
        self.status = None
        self.shipment_date = None
     
    def load(self, customer_id):

        self.customer_id = customer_id

        sql = "SELECT * FROM Orders WHERE Orders.customer_id = %s AND Orders.status = 'inprocess';"
        cursor.execute(sql, (customer_id,))

        values = cursor.fetchone()
        columns = cursor.description
        result = {}

        if values:
            for (index, value) in enumerate(values):
                result[columns[index][0]] = value

            self.order_id = result["order_id"]
            self.customer_id = result["customer_id"]
            self.first_name = result["first_name"]
            self.last_name = result["last_name"]
            self.address = result["address"]
            self.postal_zip = result["postal_zip"]
            self.city =  result["city"]
            self.country =  result["country"]
            self.total =  result["total"]
            self.create_date =  result["create_date"]
            self.update_date =  result["update_date"]
            self.status =  result["status"]
            self.shipment_date =  result["shipment_date"]
    
        result = None   
        return self
    
    def save(self):

            if self.order_id : 
                self.update_date = datetime.now()
                sql = "UPDATE Orders SET update_date = %s  WHERE order_id = %s;"
                cursor.execute(sql, (self.update_date, self.order_id))
            else: 
                self.order_id = int(uuid.uuid4().int % 2147483647)
                self.create_date = self.update_date = datetime.now()
                self.status = "inprocess"

                sql = "INSERT INTO Orders (order_id, customer_id, create_date, update_date, status) VALUES (%s, %s, %s, %s, %s);"
                cursor.execute(sql,(self.order_id, self.customer_id, self.create_date, self.update_date, self.status),)

            dbConnection.commit()
            return self
    
    def mark_as_complete(self, first_name, last_name, postal_zip, address, city, country):

        if not self.order_id:
            return
        
        self.first_name = first_name
        self.last_name = last_name
        self.postal_zip = postal_zip
        self.address = address
        self.city = city
        self.country = country
        self.status = "complete"
        self.update_date = datetime.now()
        self.shipment_date = datetime.now() + timedelta(days=3)


        sql = " UPDATE Orders SET first_name = %s, last_name = %s, postal_zip = %s, address = %s, city = %s, country = %s,  status = %s, update_date = %s,  shipment_date = %s WHERE order_id = %s;"
        cursor.execute(sql, (self.first_name, self.last_name, self.postal_zip, self.address, self.city, self.country,self.status, self.update_date, self.shipment_date, self.order_id))

        dbConnection.commit()
        return self


    def to_dict(self):
        return {
            'order_id': self.order_id,
            'customer_id': self.customer_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'address': self.address,
            'postal_zip': self.postal_zip,
            'city': self.city,
            'country': self.country,
            'total': self.total,
            'create_date': self.create_date.strftime("%Y-%m-%d") if self.create_date else None,
            'update_date': self.update_date.strftime("%Y-%m-%d") if self.update_date else None,
            'status': self.status,
            'shipment_date': self.shipment_date.strftime("%Y-%m-%d") if self.shipment_date else None,
        }

    
    
    def from_dict(self, data):

        self.order_id = data["order_id"]
        self.customer_id = data["customer_id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.address = data["address"]
        self.postal_zip = data["postal_zip"]
        self.city =  data["city"]
        self.country =  data["country"]
        self.total =  data["total"]
        self.create_date =  data["create_date"]
        self.update_date =  data["update_date"]
        self.status =  data["status"]
        self.shipment_date =  data["shipment_date"]

        return self
    