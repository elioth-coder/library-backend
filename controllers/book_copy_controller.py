from .controller import Controller

class BookCopyController(Controller):
    def __init__(self, service):
        super().__init__(service, [
            'book_id',
            'barcode',
            'status',            
        ])