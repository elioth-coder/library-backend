from flask import Blueprint
from controllers import UserController
from services import UserService
from repositories import UserRepository

user_repository = UserRepository()
user_service = UserService(user_repository)
user_controller = UserController(user_service)
user_route = Blueprint('user', __name__)
user_route.add_url_rule('/add', 'add', user_controller.add, methods=['POST'])
user_route.add_url_rule('/<int:id>', 'get', user_controller.get, methods=['GET'])
user_route.add_url_rule('/update', 'update', user_controller.update, methods=['PUT'])
user_route.add_url_rule('/delete/<int:id>', 'delete', user_controller.delete, methods=['DELETE'])
user_route.add_url_rule('/', 'get_all', user_controller.get_all, methods=['GET'])
user_route.add_url_rule('/login', 'login', user_controller.login, methods=['POST'])
user_route.add_url_rule('/me', 'me', user_controller.me, methods=['GET'])
user_route.add_url_rule('/logout', 'logout', user_controller.logout, methods=['GET'])
