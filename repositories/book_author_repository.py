from .repository import Repository

class BookAuthorRepository(Repository):
    def __init__(self):
        super().__init__('book_author')