from .repository import Repository

class VisitorRepository(Repository):
    def __init__(self):
        super().__init__('visitor')