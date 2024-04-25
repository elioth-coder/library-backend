from flask import Blueprint
from controllers import BorrowedController
from services import BorrowedService
from repositories import BorrowedRepository

borrowed_repository = BorrowedRepository()
borrowed_service = BorrowedService(borrowed_repository)
borrowed_controller = BorrowedController(borrowed_service)
borrowed_route = Blueprint('borrowed', __name__)
borrowed_route.add_url_rule('/add', 'add', borrowed_controller.add, methods=['POST'])
borrowed_route.add_url_rule('/<int:id>', 'get', borrowed_controller.get, methods=['GET'])
borrowed_route.add_url_rule('/update', 'update', borrowed_controller.update, methods=['PUT'])
borrowed_route.add_url_rule('/delete/<int:id>', 'delete', borrowed_controller.delete, methods=['DELETE'])
borrowed_route.add_url_rule('/', 'get_all', borrowed_controller.get_all, methods=['GET'])