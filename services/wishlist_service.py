from .service import Service

class WishlistService(Service):
    def __init__(self, repository):
        super().__init__(repository)