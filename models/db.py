import mysql.connector

dbConnection=mysql.connector.connect( host="127.0.0.1",port = '3306', user="root", password="pw", database="BookShope")
cursor = dbConnection.cursor()