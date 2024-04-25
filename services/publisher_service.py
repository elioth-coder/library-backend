from .service import Service

class PublisherService(Service):
    def __init__(self, repository):
        super().__init__(repository)