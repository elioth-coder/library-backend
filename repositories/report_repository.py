from .repository import Repository

class ReportRepository(Repository):
    def __init__(self):
        super().__init__('report')
