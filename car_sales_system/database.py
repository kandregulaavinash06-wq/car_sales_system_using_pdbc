import MySQLdb
class DatabaseConnection:
    def __init__(self):
        self.connection=None
    def connect(self):
        self.connection=MySQLdb.connect(
            user='root',
            host='localhost',
            password='avinash',
            database='car_sales_db'
        )
        return self.connection
db=DatabaseConnection()
connection=db.connect()
connection.close()