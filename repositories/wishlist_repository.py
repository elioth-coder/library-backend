from .repository import Repository

class WishlistRepository(Repository):
    def __init__(self):
        super().__init__('wishlist')