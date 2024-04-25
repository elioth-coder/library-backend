from flask import Blueprint
from controllers import BookAuthorController
from services import BookAuthorService
from repositories import BookAuthorRepository

book_author_repository = BookAuthorRepository()
book_author_service = BookAuthorService(book_author_repository)
book_author_controller = BookAuthorController(book_author_service)
book_author_route = Blueprint('book_author', __name__)
book_author_route.add_url_rule('/add', 'add', book_author_controller.add, methods=['POST'])
book_author_route.add_url_rule('/<int:id>', 'get', book_author_controller.get, methods=['GET'])
book_author_route.add_url_rule('/update', 'update', book_author_controller.update, methods=['PUT'])
book_author_route.add_url_rule('/delete/<int:id>', 'delete', book_author_controller.delete, methods=['DELETE'])
book_author_route.add_url_rule('/', 'get_all', book_author_controller.get_all, methods=['GET'])
book_author_route.add_url_rule('/search/', 'search', book_author_controller.search, methods=['GET'])
book_author_route.add_url_rule('/get_by/', 'get_by', book_author_controller.get_by, methods=['GET'])
