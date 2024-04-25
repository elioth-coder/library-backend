from .service import Service

class VisitorService(Service):
    def __init__(self, repository):
        super().__init__(repository)

    