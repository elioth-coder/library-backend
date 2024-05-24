from .repository import Repository

class DashboardRepository(Repository):
    def __init__(self):
        super().__init__('dashboard')
