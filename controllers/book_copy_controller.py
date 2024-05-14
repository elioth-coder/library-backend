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

