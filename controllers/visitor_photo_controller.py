from .controller import Controller
from flask import request, jsonify

class VisitorPhotoController(Controller):
    def __init__(self, service):
        super().__init__(service, [
            'visitor_id',
            'file',
            'encoding',
        ])

    def add(self):
        item = {}
        item['visitor_id'] = request.form.get('visitor_id')
        item['file'] = self.service.save_image(request.form.get('base64_file'))
        item['encoding'] = self.service.extract_encoding(item['file'])
        item['id'] = self.service.add(item)
        item.pop('encoding')

        data = {
            'status': 'success',
            'message': 'Successfully added.',
            'item': item
        }
        response = jsonify(data)

        return response, 200

    def update(self):
        id = request.form.get('visitor_photo_id')
        self.service.delete(id)
        
        item = {}
        item['visitor_id'] = request.form.get('visitor_id')
        item['file'] = self.service.save_image(request.form.get('base64_file'))
        item['encoding'] = self.service.extract_encoding(item['file'])
        item['id'] = self.service.add(item)
        item.pop('encoding')

        data = {
            'status': 'success',
            'message': 'Successfully updated.',
            'item': item
        }
        response = jsonify(data)

        return response, 200

    def delete(self, id):
        visitor_photo = self.service.get(id)

        self.service.delete_image(visitor_photo['file'])
        self.service.delete(id)

        data = {
            'status': 'success',
            'message': 'Successfully deleted.',
        }
        response = jsonify(data)
        
        return response, 200

    def get_all(self):
        items = self.service.get_all()
        
        for item in items, index:
            item.pop('encoding')
            items[index] = item

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

        item = self.service.get_by(column, value)
        if(item):
            item.pop('encoding')
        data = {
            'status': 'success',
            'item': item,
        }
        response = jsonify(data)

        return response, 200