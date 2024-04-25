import mysql.connector

class DBConnector:
    def __init__(self, database='library'):
        self.host = 'localhost'
        self.user = 'root'
        self.password = ''
        self.database = database


    def create_connection(self):
        return mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )