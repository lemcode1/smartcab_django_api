import mysql.connector
def get_db_conn():
         #connect to database
         database_connection = mysql.connector.connect(host="localhost",port=3306,user="root",password="root123")
         return database_connection