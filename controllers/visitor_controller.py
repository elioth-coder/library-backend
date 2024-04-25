from .controller import Controller

class VisitorController(Controller):
    def __init__(self, service):
        super().__init__(service, [
            'first_name',
            'middle_name',
            'last_name',
            'type',
            'registration_date',      
        ])