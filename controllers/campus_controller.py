from .controller import Controller

class CampusController(Controller):
    def __init__(self, service):
        super().__init__(service, [
            'name',
            'location',
        ])