from flask import Blueprint
from controllers import AuthorController
from services import AuthorService
from repositories import AuthorRepository

author_repository = AuthorRepository()
author_service = AuthorService(author_repository)
author_controller = AuthorController(author_service)
author_route = Blueprint('author', __name__)
author_route.add_url_rule('/add', 'add', author_controller.add, methods=['POST'])
author_route.add_url_rule('/<int:id>', 'get', author_controller.get, methods=['GET'])
author_route.add_url_rule('/update', 'update', author_controller.update, methods=['PUT'])
author_route.add_url_rule('/delete/<int:id>', 'delete', author_controller.delete, methods=['DELETE'])
author_route.add_url_rule('/', 'get_all', author_controller.get_all, methods=['GET'])
author_route.add_url_rule('/search/', 'search', author_controller.search, methods=['GET'])
author_route.add_url_rule('/count/', 'count', author_controller.count, methods=['GET'])
