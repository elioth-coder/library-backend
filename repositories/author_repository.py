from .repository import Repository

class AuthorRepository(Repository):
    def __init__(self):
        super().__init__('author')