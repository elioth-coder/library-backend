from .repository import Repository

class PublisherRepository(Repository):
    def __init__(self):
        super().__init__('publisher')