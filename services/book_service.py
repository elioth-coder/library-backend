from .service import Service

class BookService(Service):
    def __init__(self, repository):
        super().__init__(repository)
        