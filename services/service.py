class Service:
    def __init__(self, repository):
        self.repository = repository

    def add(self, item):
        return self.repository.add(item)

    def update(self, item):
        self.repository.update(item)

    def update_by(self, column, item):
        self.repository.update_by(column, item)
                
    def delete(self, id):
        self.repository.delete(id)

    def delete_by(self, column, value):
        self.repository.delete_by(column, value)

    def get(self, id):
        return self.repository.get(id)

    def get_all(self):
        return self.repository.get_all()

    def get_by(self, column, value):
        return  self.repository.get_by(column, value)

    def get_one(self, column, value):
        return  self.repository.get_one(column, value)

    def search(self, query):
        return  self.repository.search(query)

    def search_by(self, column, query):
        return  self.repository.search_by(column, query)