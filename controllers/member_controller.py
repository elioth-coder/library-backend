from .controller import Controller
from flask import request, jsonify

class MemberController(Controller):
    def __init__(self, service):
        super().__init__(service, [
            'card_number',
            'photo',
            'encoding',
            'last_name',
            'first_name',
            'email',
            'issue_date',
            'expiration_date',
            'year_level',
            'course',
            'campus',
            'type',
            'gender',
            'birthday',
            'status',
        ])
        

    def add(self):
        item = {}
        item['photo'] = self.service.save_image(request.form.get('base64'))
        item['encoding'] = self.service.extract_encoding(item['photo'])
        item['last_name'] = request.form.get('last_name')
        item['first_name'] = request.form.get('first_name')
        item['gender'] = request.form.get('gender')
        item['birthday'] = request.form.get('birthday')
        item['card_number'] = request.form.get('card_number')
        item['type'] = request.form.get('type')
        item['email'] = request.form.get('email')
        item['year_level'] = request.form.get('year_level')
        item['course'] = request.form.get('course')
        item['campus'] = request.form.get('campus')
        item['issue_date'] = request.form.get('issue_date')
        item['expiration_date'] = request.form.get('expiration_date')
        item['status'] = 'Pending'

        item['id'] = self.service.add(item)
        item.pop('encoding')

        data = {
            'status': 'success',
            'message': 'Successfully added.',
            'item': item
        }
        response = jsonify(data)

        return response, 200

    def get_all(self):
        items = self.service.get_all()
        
        for index, item in enumerate(items):
            item.pop('encoding')
            items[index] = item

        data = {
            'status': 'success',
            'items': items,
        }
        response = jsonify(data)
        
        return response, 200

    def get(self, id):
        item = self.service.get(id)
        if(item):
            item.pop('encoding')
        data = {
            'status': 'success',
            'item': item,
        }
        response = jsonify(data)
        return response, 200

    def get_by(self): 
        column = request.args.get('column')
        value = request.args.get('value')

        if column not in self.columns:
            data = {
                'status': 'error',
                'message': 'Invalid column',
            }
            response = jsonify(data)

            return response, 200

        item = self.service.get_by(column, value)
        if(item):
            item.pop('encoding')
        data = {
            'status': 'success',
            'item': item,
        }
        response = jsonify(data)

        return response, 200

    def get_one(self): 
        column = request.args.get('column')
        value = request.args.get('value')

        if column not in self.columns:
            data = {
                'status': 'error',
                'message': 'Invalid column',
            }
            response = jsonify(data)
            return response, 200

        item = self.service.get_one(column, value)
        item.pop('encoding')
        data = {
            'status': 'success',
            'item': item,
        }
        response = jsonify(data)
        return response, 200
