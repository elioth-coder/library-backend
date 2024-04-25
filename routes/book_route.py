from flask import Blueprint
from controllers import BookController
from services import BookService
from repositories import BookRepository

book_repository = BookRepository()
book_service = BookService(book_repository)
book_controller = BookController(book_service)
book_route = Blueprint('book', __name__)
book_route.add_url_rule('/add', 'add', book_controller.add, methods=['POST'])
book_route.add_url_rule('/<int:id>', 'get', book_controller.get, methods=['GET'])
book_route.add_url_rule('/update', 'update', book_controller.update, methods=['PUT'])
book_route.add_url_rule('/delete/<int:id>', 'delete', book_controller.delete, methods=['DELETE'])
book_route.add_url_rule('/', 'get_all', book_controller.get_all, methods=['GET'])
book_route.add_url_rule('/search/', 'search', book_controller.search, methods=['GET'])
