from flask import request, jsonify

class Controller:
    def __init__(self, service, columns):
        self.service = service
        self.columns = columns

    def add(self):
        item = {}

        for column in self.columns:
            item[column] = request.form.get(column)

        id = self.service.add(item)
        item['id'] = id
        data = {
            'status': 'success',
            'message': 'Successfully added',
            'item': item
        }
        response = jsonify(data)
        return response, 200
        
        
    def update_by(self):
        column = request.args.get('column')

        if column not in self.columns:
            data = {
                'status': 'error',
                'message': 'Invalid column',
            }
            response = jsonify(data)
            return response, 200

        self.service.update_by(column, item)
        data = {
            'status': 'success',
            'message': 'Successfully updated',
            'item': item
        }
        response = jsonify(data)
        return response, 200 

    def update(self):
        item = {}

        for column in self.columns:
            value = request.form.get(column)
            if value:
                item[column] = value

        item['id'] = request.form.get('id')
        self.service.update(item)
        data = {
            'status': 'success',
            'message': 'Successfully updated',
            'item': item
        }
        response = jsonify(data)
        return response, 200  

    def delete(self, id):
        self.service.delete(id)
        data = {
            'status': 'success',
            'message': 'Successfully deleted',
        }
        response = jsonify(data)
        return response, 200

    def get(self, id):
        item = self.service.get(id)
        data = {
            'status': 'success',
            'item': item,
        }
        response = jsonify(data)
        return response, 200

    def count(self):
        count = self.service.count()
        data = {
            'status': 'success',
            'count': count,
        }
        response = jsonify(data)
        return response, 200

    def count_by(self): 
        column = request.args.get('column')
        value = request.args.get('value')

        if column not in self.columns:
            data = {
                'status': 'error',
                'message': 'Invalid column',
            }
            response = jsonify(data)
            return response, 200

        count = self.service.count_by(column, value)
        data = {
            'status': 'success',
            'count': count,
        }
        response = jsonify(data)
        return response, 200

    def get_all(self):
        items = self.service.get_all()
        data = {
            'status': 'success',
            'items': items,
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

        items = self.service.get_by(column, value)
        data = {
            'status': 'success',
            'items': items,
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
        data = {
            'status': 'success',
            'item': item,
        }
        response = jsonify(data)
        return response, 200

    def delete_by(self): 
        column = request.args.get('column')
        value = request.args.get('value')

        if column not in self.columns:
            data = {
                'status': 'error',
                'message': 'Invalid column',
            }
            response = jsonify(data)
            return response, 200

        self.service.delete_by(column, value)
        data = {
            'status': 'success',
            'message': 'Successfully deleted',
        }
        response = jsonify(data)
        return response, 200

    def search_by(self): 
        column = request.args.get('column')
        query = request.args.get('query')

        if column not in self.columns:
            data = {
                'status': 'error',
                'message': 'Invalid column',
            }
            response = jsonify(data)
            return response, 200

        items = self.service.search_by(column, query)
        data = {
            'status': 'success',
            'items': items,
        }
        response = jsonify(data)
        return response, 200

    def search(self):
        query = request.args.get('query')

        items = self.service.search(query)
        data = {
            'status': 'success',
            'items': items,
        }
        response = jsonify(data)
        return response, 200