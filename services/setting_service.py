from .service import Service

class SettingService(Service):
    def __init__(self, repository):
        super().__init__(repository)