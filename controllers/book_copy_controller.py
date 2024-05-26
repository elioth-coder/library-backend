from .controller import Controller
from flask import request, jsonify

class BookCopyController(Controller):
    def __init__(self, service):
        super().__init__(service, [
            'book_id',
            'barcode',
            'call_no',
            'price',
            'status', 
            'date_added',           
        ])

    def get_all(self):
        sql = "SELECT *, (SELECT `isbn` FROM `book` WHERE `id`=`book_id`) AS `isbn`, (SELECT `title` FROM `book` WHERE `id`=`book_id`) AS `title`, (SELECT `publication_year` FROM `book` WHERE `id`=`book_id`) AS `publication_year` FROM `book_copy`"
        items = self.service.query(sql)
        data = {
            'status': 'success',
            'items': items,
        }
        response = jsonify(data)
        return response, 200

    def copies_count(self):
        book_id = request.args.get('book_id')
        status = request.args.get('status')
        params = {
            'book_id': book_id, 
            'status': status,
        }

        sql = f"SELECT COUNT(`id`) AS `count` FROM `book_copy` WHERE `book_id`=%(book_id)s AND `status`=%(status)s"
        results = self.service.query(sql, params)

        data = {
            'status' : 'success',
            'count': results[0]['count'],
        }
        response = jsonify(data)
        return response, 200        

