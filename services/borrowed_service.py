from .service import Service

class BorrowedService(Service):
    def __init__(self, repository):
        super().__init__(repository)