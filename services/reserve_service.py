from .service import Service

class ReserveService(Service):
    def __init__(self, repository):
        super().__init__(repository)