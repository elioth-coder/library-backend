from flask import Blueprint
from controllers import MemberController
from services import MemberService
from repositories import MemberRepository

member_repository = MemberRepository()
member_service = MemberService(member_repository)
member_controller = MemberController(member_service)
member_route = Blueprint('member', __name__)
member_route.add_url_rule('/add', 'add', member_controller.add, methods=['POST'])
member_route.add_url_rule('/<int:id>', 'get', member_controller.get, methods=['GET'])
member_route.add_url_rule('/update', 'update', member_controller.update, methods=['PUT'])
member_route.add_url_rule('/delete/<int:id>', 'delete', member_controller.delete, methods=['DELETE'])
member_route.add_url_rule('/', 'get_all', member_controller.get_all, methods=['GET'])
member_route.add_url_rule('/get_by/', 'get_by', member_controller.get_by, methods=['GET'])
member_route.add_url_rule('/get_one/', 'get_one', member_controller.get_one, methods=['GET'])
member_route.add_url_rule('/search/', 'search', member_controller.search, methods=['GET'])
member_route.add_url_rule('/delete_by/', 'delete_by', member_controller.delete_by, methods=['DELETE'])
