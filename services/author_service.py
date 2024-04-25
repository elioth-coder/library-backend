from .service import Service

class AuthorService(Service):
    def __init__(self, repository):
        super().__init__(repository)