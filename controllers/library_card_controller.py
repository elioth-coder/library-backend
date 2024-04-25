from .controller import Controller

class LibraryCardController(Controller):
    def __init__(self, service):
        super().__init__(service, [
            'card_number',
            'visitor_id',
            'email',
            'issue_date',
            'expiration_date',
        ])