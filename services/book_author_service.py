from .service import Service

class BookAuthorService(Service):
    def __init__(self, repository):
        super().__init__(repository)

    def add(self, item): 
        if item['type'] == 'Main Author':
            _item = {
                'type': 'Co-Author',
                'book_id': item['book_id'],
            }
            self.repository.update_by('book_id', _item)
            
        return self.repository.add(item)

        