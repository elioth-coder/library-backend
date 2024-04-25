from .service import Service

class UserService(Service):
    def __init__(self, repository):
        super().__init__(repository)

    def login(self, username, password):
        return self.repository.login(username, password)