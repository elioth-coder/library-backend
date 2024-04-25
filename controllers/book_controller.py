from .controller import Controller

class BookController(Controller):
    def __init__(self, service):
        super().__init__(service, [
            'title',
            'publication_year',
            'genre',            
            'publisher_id',            
            'page_count',            
            'language',            
            'edition',            
            'synopsis',            
        ])