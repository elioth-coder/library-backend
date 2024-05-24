from .repository import Repository

class SettingRepository(Repository):
    def __init__(self):
        super().__init__('setting')