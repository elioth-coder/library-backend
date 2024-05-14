from .repository import Repository

class ReserveRepository(Repository):
    def __init__(self):
        super().__init__('reserve')