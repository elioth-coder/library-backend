from .service import Service

class ReportService(Service):
    def __init__(self, repository):
        super().__init__(repository)

    def query(self, sql, params=[]):
        return self.repository.query(sql, params)