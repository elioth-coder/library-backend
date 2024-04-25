from .service import Service

class LibraryCardService(Service):
    def __init__(self, repository):
        super().__init__(repository)