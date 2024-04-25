from .repository import Repository

class BookRepository(Repository):
    def __init__(self):
        super().__init__('book')