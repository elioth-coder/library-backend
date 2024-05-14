from .controller import Controller

class ReserveController(Controller):
    def __init__(self, service):
        super().__init__(service, [
            'number',
            'book_id',
        ])