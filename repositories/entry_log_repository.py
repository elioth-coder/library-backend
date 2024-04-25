from .repository import Repository

class EntryLogRepository(Repository):
    def __init__(self):
        super().__init__('entry_log')