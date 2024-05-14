from .repository import Repository

class QueueRepository(Repository):
    def __init__(self):
        super().__init__('queue')