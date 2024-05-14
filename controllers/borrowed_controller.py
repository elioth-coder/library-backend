from .controller import Controller

class BorrowedController(Controller):
    def __init__(self, service):
        super().__init__(service, [
            'book_copy_id',
            'member_id',
            'borrowed_date',
            'returned_date', 
            'due_date',        
        ])