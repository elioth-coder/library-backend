from .service import Service

class QueueService(Service):
    def __init__(self, repository):
        super().__init__(repository)