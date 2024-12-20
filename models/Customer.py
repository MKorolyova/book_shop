import uuid
from .db import dbConnection;
from .db import cursor;

class Customer:

    def __init__(self):
        self.customer_id = None
        self.password  = None
        self.email = None

    def from_dict(self, data):
        self.customer_id = data["customer_id"]
        self.password = data["password"]
        self.email = data["email"]
        return self
    
    def to_dict(self):
        return {
            'customer_id': self.customer_id,
            'password': self.password,
            'email': self.email
    }
    
    def save(self):
            if self.customer_id:  
                sql = "UPDATE Customers SET password = %s, email = %s WHERE customer_id = %s"
                values = (self.password, self.email, self.customer_id)
            else:  
                self.customer_id = int(uuid.uuid4().int % 2147483647) 
                sql = "INSERT INTO Customers (customer_id, password, email) VALUES (%s, %s, %s)"
                values = (self.customer_id, self.password, self.email)

            cursor.execute(sql, values)
            dbConnection.commit()


    def load_by_email(self, email, password):
        
        self.password = password
        self.email = email
    
        sql = "SELECT * FROM Customers WHERE Customers.email = %s;"
        cursor.execute(sql, (email,))

        values = cursor.fetchone()
        columns = cursor.description
        result = {}

        if not values:
            return

        for (index, value) in enumerate(values):
            result[columns[index][0]] = value

        self.customer_id = result["customer_id"]
        self.password = result["password"]
        self.email = result["email"]

        result = None   
        return self
 


