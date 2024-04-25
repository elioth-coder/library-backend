from .repository import Repository

class BookCopyRepository(Repository):
    def __init__(self):
        super().__init__('book_copy')