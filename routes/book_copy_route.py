from flask import Blueprint
from controllers import BookCopyController
from services import BookCopyService
from repositories import BookCopyRepository

book_copy_repository = BookCopyRepository()
book_copy_service = BookCopyService(book_copy_repository)
book_copy_controller = BookCopyController(book_copy_service)
book_copy_route = Blueprint('book_copy', __name__)
book_copy_route.add_url_rule('/add', 'add', book_copy_controller.add, methods=['POST'])
book_copy_route.add_url_rule('/<int:id>', 'get', book_copy_controller.get, methods=['GET'])
book_copy_route.add_url_rule('/update', 'update', book_copy_controller.update, methods=['PUT'])
book_copy_route.add_url_rule('/delete/<int:id>', 'delete', book_copy_controller.delete, methods=['DELETE'])
book_copy_route.add_url_rule('/', 'get_all', book_copy_controller.get_all, methods=['GET'])
book_copy_route.add_url_rule('/get_one/', 'get_one', book_copy_controller.get_one, methods=['GET'])
book_copy_route.add_url_rule('/search/', 'search', book_copy_controller.search, methods=['GET'])
book_copy_route.add_url_rule('/copies_count/', 'copies_count', book_copy_controller.copies_count, methods=['GET'])
book_copy_route.add_url_rule('/count/', 'count', book_copy_controller.count, methods=['GET'])
book_copy_route.add_url_rule('/get_by/', 'get_by', book_copy_controller.get_by, methods=['GET'])
