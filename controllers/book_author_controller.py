from .controller import Controller

class BookAuthorController(Controller):
    def __init__(self, service):
        super().__init__(service, [
            'book_id',
            'author_id',
            'type',
        ])