from .controller import Controller

class WishlistController(Controller):
    def __init__(self, service):
        super().__init__(service, [
            'book_id',
            'member_id',
        ])