from .controller import Controller

class QueueController(Controller):
    def __init__(self, service):
        super().__init__(service, [
            'dt_created',
        ])