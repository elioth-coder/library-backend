from .controller import Controller
from flask import request, jsonify

class BorrowedController(Controller):
    def __init__(self, service):
        super().__init__(service, [
            'book_copy_id',
            'member_id',
            'borrowed_date',
            'returned_date', 
            'due_date',
            'penalty',    
        ])

    def get_borrowed(self): 
        sql = "SELECT * FROM `borrowed` WHERE `returned_date` IS NULL"
        results = self.service.query(sql)

        data = {
            'status' : 'success',
            'results': results,
        }
        response = jsonify(data)
        return response, 200

    def get_borrowed_by(self): 
        borrowed_by = request.args.get('id')
        sql = "SELECT * FROM `borrowed` WHERE `returned_date` IS NULL AND `member_id`=%(id)s"
        params = {
            'id' : borrowed_by
        }
        print(params)
        results = self.service.query(sql, params)

        data = {
            'status' : 'success',
            'results': results,
        }
        response = jsonify(data)
        return response, 200

    def get_returned_by(self): 
        borrowed_by = request.args.get('id')
        sql = "SELECT * FROM `borrowed` WHERE `returned_date` IS NOT NULL AND `member_id`=%(id)s"
        params = {
            'id' : borrowed_by
        }
        print(params)
        results = self.service.query(sql, params)

        data = {
            'status' : 'success',
            'results': results,
        }
        response = jsonify(data)
        return response, 200