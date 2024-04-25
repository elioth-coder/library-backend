from .controller import Controller
from flask import request, jsonify

class EntryLogController(Controller):
    def __init__(self, service):
        super().__init__(service, [
            'visitor_id',
            'file',        
        ])

    def add(self):
        item = {}
        item['file'] = self.service.save_image(request.form.get('base64_file'))
        item['visitor_id'] = request.form.get('visitor_id')
        item['id'] = self.service.add(item)
        data = {
            'status': 'success',
            'message': 'Successfully added',
            'item': item
        }
        response = jsonify(data)
        return response, 200


    def find_face(self):
        item = {}
        image_data = request.form.get('base64_file')
        photos = self.service.get_visitor_photos()
        encodings = self.service.extract_encodings(photos)
        image = self.service.base64_to_image(image_data)
        match_index = self.service.find_face(encodings, image)

        if match_index == -1: 
            data = {
                'status': 'error',
                'message': 'No face match was found',
            }
            response = jsonify(data)
            return response, 200

        visitor_id = photos[match_index]['visitor_id']
        visitor = self.service.get_visitor(visitor_id)
        item['visitor'] = visitor

        data = {
            'status': 'success',
            'message': 'A face match was found',
            'item': item,
        }
        response = jsonify(data)
        return response, 200

    def delete(self, id):
        entry_log_photo = self.service.get(id)

        self.service.delete_image(entry_log_photo['file'])
        self.service.delete(id)

        data = {
            'status': 'success',
            'message': 'Successfully deleted.',
        }
        response = jsonify(data)
        return response, 200