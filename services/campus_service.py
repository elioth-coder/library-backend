from .service import Service

class CampusService(Service):
    def __init__(self, repository):
        super().__init__(repository)