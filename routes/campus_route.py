from flask import Blueprint
from controllers import CampusController
from services import CampusService
from repositories import CampusRepository

campus_repository = CampusRepository()
campus_service = CampusService(campus_repository)
campus_controller = CampusController(campus_service)
campus_route = Blueprint('campus', __name__)
campus_route.add_url_rule('/add', 'add', campus_controller.add, methods=['POST'])
campus_route.add_url_rule('/<int:id>', 'get', campus_controller.get, methods=['GET'])
campus_route.add_url_rule('/update', 'update', campus_controller.update, methods=['PUT'])
campus_route.add_url_rule('/delete/<int:id>', 'delete', campus_controller.delete, methods=['DELETE'])
campus_route.add_url_rule('/', 'get_all', campus_controller.get_all, methods=['GET'])
campus_route.add_url_rule('/search/', 'search', campus_controller.search, methods=['GET'])
campus_route.add_url_rule('/search_by/', 'search_by', campus_controller.search_by, methods=['GET'])
campus_route.add_url_rule('/count/', 'count', campus_controller.count, methods=['GET'])
