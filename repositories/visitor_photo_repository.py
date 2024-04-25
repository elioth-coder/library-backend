from .repository import Repository

class VisitorPhotoRepository(Repository):
    def __init__(self):
        super().__init__('visitor_photo')