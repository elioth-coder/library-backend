from .repository import Repository

class LibraryCardRepository(Repository):
    def __init__(self):
        super().__init__('library_card')