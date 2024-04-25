from .db_connector import DBConnector
from contextlib import contextmanager
import datetime

class Repository:
    def __init__(self, table_name):
        self.connector  = connector = DBConnector()
        self.table_name = table_name

    @contextmanager
    def connect(self): 
        yield self.connector.create_connection()

    def columns(self):
        sql = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{self.table_name}'"
        with self.connect() as db: 
            with db.cursor() as cursor: 
                cursor.execute(sql)
                results = cursor.fetchall()

        columns = [column[0] for column in results]
        return columns

    def add(self, item):
        keys   = ','.join([f'`{key}`' for key in item.keys()])
        values = ','.join([f'%({key})s' for key in item.keys()])
        sql = f'INSERT INTO `{self.table_name}` ({keys}) VALUES ({values})'
        
        params = {
            **item
        }
        with self.connect() as db:
            with db.cursor() as cursor: 
                cursor.execute(sql, params)
                db.commit()
                id = cursor.lastrowid

        return id

    def update(self, item):
        item = { **item }
        id = item.pop('id')
        values = ','.join([f'`{key}`=%({key})s' for key in item.keys()])
        sql = f'UPDATE `{self.table_name}` SET {values} WHERE `id`=%(id)s'
        
        params = {
            'id': id,
            **item
        }
        with self.connect() as db:
            with db.cursor() as cursor: 
                cursor.execute(sql, params)
                db.commit()
                
    def update_by(self, column, item):
        item = { **item }
        value = item.pop(column)
        values = ','.join([f'`{key}`=%({key})s' for key in item.keys()])
        sql = f'UPDATE `{self.table_name}` SET {values} WHERE `{column}`=%(value)s'
        
        params = {
            'value': value,
            **item
        }
        with self.connect() as db:
            with db.cursor() as cursor: 
                cursor.execute(sql, params)
                db.commit()

    def delete(self, id):
        sql = f'DELETE FROM `{self.table_name}` WHERE `id`=%(id)s'
        params = {
            'id': id
        }
        with self.connect() as db:
            with db.cursor() as cursor: 
                cursor.execute(sql, params)
                db.commit()

    def get(self, id):
        sql = f'SELECT * FROM `{self.table_name}` WHERE `id`=%(id)s'
        params = {
            'id': id
        }
        with self.connect() as db:
            with db.cursor(dictionary=True) as cursor: 
                cursor.execute(sql, params)
                result = cursor.fetchone()

        return self.transform_result(result)

    def get_all(self):
        sql = f'SELECT * FROM `{self.table_name}` ORDER BY `id` DESC'

        with self.connect() as db: 
            with db.cursor(dictionary=True) as cursor: 
                cursor.execute(sql)
                results = cursor.fetchall()

        return self.transform_results(results)

    def get_by(self, column, value):
        sql = f"SELECT * FROM `{self.table_name}` WHERE `{column}`=%(value)s"
        params = {
            'value': value,
        }
        with self.connect() as db: 
            with db.cursor(dictionary=True) as cursor: 
                cursor.execute(sql, params)
                results = cursor.fetchall()

        return self.transform_results(results)

    def get_one(self, column, value):
        sql = f"SELECT * FROM `{self.table_name}` WHERE `{column}`=%(value)s"
        params = {
            'value': value,
        }
        with self.connect() as db: 
            with db.cursor(dictionary=True) as cursor: 
                cursor.execute(sql, params)
                result = cursor.fetchone()

        return self.transform_result(result)

    def delete_by(self, column, value):
        sql = f"DELETE FROM `{self.table_name}` WHERE `{column}`=%(value)s"
        params = {
            'value': value,
        }
        with self.connect() as db: 
            with db.cursor(dictionary=True) as cursor: 
                cursor.execute(sql, params)
                db.commit()

    def search(self, query):
        columns = self.columns()
        sql = f"SELECT * FROM `{self.table_name}` WHERE "
        sql += " OR ".join(map(lambda column: f"`{column}` LIKE %(query)s", columns))

        params = {
            'query': f'%{query}%',
        }
        with self.connect() as db: 
            with db.cursor(dictionary=True) as cursor: 
                cursor.execute(sql, params)
                results = cursor.fetchall()

        return self.transform_results(results)
    
    def search_by(self, column, query):
        sql = f"SELECT * FROM `{self.table_name}` WHERE `{column}` LIKE %(query)s"
        params = {
            'query': f'%{query}%',
        }
        with self.connect() as db: 
            with db.cursor(dictionary=True) as cursor: 
                cursor.execute(sql, params)
                results = cursor.fetchall()

        return self.transform_results(results)

    def transform_results(self, results): 
        if not results:
            return results
        results = self.stringify_dates(results)
        return results

    def transform_result(self, result): 
        if not result:
            return result
        result = self.stringify_date(result)
        return result

    def stringify_dates(self, results):
        for index, result in enumerate(results):
            result = self.stringify_date(result)
            results[index] = result

        return results

    def stringify_date(self, result):
        for key in result:
            value = result[key]
            if isinstance(value, datetime.date) or isinstance(value, datetime.datetime):
                result[key] = str(value)
        
        return result

    