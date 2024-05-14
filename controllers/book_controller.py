from .controller import Controller
from flask import request, jsonify

class BookController(Controller):
    def __init__(self, service):
        super().__init__(service, [
            'cover',
            'title',
            'isbn',
            'publication_year',
            'genre',            
            'publisher_id',            
            'page_count',            
            'language',            
            'edition',            
            'synopsis',            
        ])

    def add(self):
        item = {}
        item['cover'] = self.service.save_image(request.form.get('base64'))
        item['title'] = request.form.get('title')
        item['isbn'] = request.form.get('isbn')
        item['publication_year'] = request.form.get('publication_year')
        item['genre'] = request.form.get('genre')
        item['publisher_id'] = request.form.get('publisher_id')
        item['page_count'] = request.form.get('page_count')
        item['language'] = request.form.get('language')
        item['edition'] = request.form.get('edition')
        item['synopsis'] = request.form.get('synopsis')
        item['id'] = self.service.add(item)
        data = {
            'status': 'success',
            'message': 'Successfully added',
            'item': item
        }
        response = jsonify(data)
        return response, 200

    def update(self):
        item = {}
        if(request.form.get('cover')):
            self.service.delete_image(request.form.get('cover'))
        item['cover'] = self.service.save_image(request.form.get('base64'))
        item['title'] = request.form.get('title')
        item['isbn'] = request.form.get('isbn')
        item['publication_year'] = request.form.get('publication_year')
        item['genre'] = request.form.get('genre')
        item['publisher_id'] = request.form.get('publisher_id')
        item['page_count'] = request.form.get('page_count')
        item['language'] = request.form.get('language')
        item['edition'] = request.form.get('edition')
        item['synopsis'] = request.form.get('synopsis')
        item['id'] = request.form.get('id')
        self.service.update(item)
        data = {
            'status': 'success',
            'message': 'Successfully added',
            'item': item
        }
        response = jsonify(data)
        return response, 200

    def delete(self, id):
        book = self.service.get(id)

        if(book['cover']):
            self.service.delete_image(book['cover'])
        self.service.delete(id)

        data = {
            'status': 'success',
            'message': 'Successfully deleted.',
        }
        response = jsonify(data)
        
        return response, 200

    def authors(self):
        book_id = request.args.get('book_id')
        author_type = request.args.get('author_type')
        params = {
            'book_id': book_id,
            'author_type': author_type, 
        }

        sql = f"""
        SELECT `author`.* FROM `author` 
            INNER JOIN `book_author` 
            ON `author`.`id`=`book_author`.`author_id`
        WHERE `book_author`.`book_id`=%(book_id)s
            AND `book_author`.`type`=%(author_type)s
        """
        results = self.service.query(sql, params)

        data = {
            'status' : 'success',
            'authors': results,
        }
        response = jsonify(data)
        return response, 200   