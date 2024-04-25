from .repository import Repository

class UserRepository(Repository):
    def __init__(self):
        super().__init__('user')

    def login(self, username, password):
        sql = f'SELECT * FROM `{self.table_name}` WHERE `username`=%(username)s AND `password`=%(password)s'
        params = {
            'username': username,
            'password': password,
        }
        with self.connect() as db:
            with db.cursor(dictionary=True) as cursor: 
                cursor.execute(sql, params)
                result = cursor.fetchone()

        return result
