from .repository import Repository

class BorrowedRepository(Repository):
    def __init__(self):
        super().__init__('borrowed')

    def get_by(self, column, value):
        sql = f"SELECT * FROM `{self.table_name}` WHERE `{column}`=%(value)s AND `returned_date` IS NULL"
        params = {
            'value': value,
        }
        with self.connect() as db: 
            with db.cursor(dictionary=True) as cursor: 
                cursor.execute(sql, params)
                results = cursor.fetchall()

        return self.transform_results(results)
