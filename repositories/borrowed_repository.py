from .repository import Repository

class BorrowedRepository(Repository):
    def __init__(self):
        super().__init__('borrowed')