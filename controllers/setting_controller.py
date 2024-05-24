from .controller import Controller

class SettingController(Controller):
    def __init__(self, service):
        super().__init__(service, [
            'property',
            'value',
        ])