from .controller import Controller

class AuthorController(Controller):
    def __init__(self, service):
        super().__init__(service, [
            'first_name',
            'middle_name',
            'last_name',            
        ])