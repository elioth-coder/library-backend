from .repository import Repository

class CampusRepository(Repository):
    def __init__(self):
        super().__init__('campus')