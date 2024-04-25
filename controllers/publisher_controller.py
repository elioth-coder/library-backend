from .controller import Controller

class PublisherController(Controller):
    def __init__(self, service):
        super().__init__(service, [
            'name',
            'location',
            'email',            
        ])