from .service import Service

class BookCopyService(Service):
    def __init__(self, repository):
        super().__init__(repository)