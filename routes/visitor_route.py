from flask import Blueprint
from controllers import VisitorController
from services import VisitorService
from repositories import VisitorRepository

visitor_repository = VisitorRepository()
visitor_service = VisitorService(visitor_repository)
visitor_controller = VisitorController(visitor_service)
visitor_route = Blueprint('visitor', __name__)
visitor_route.add_url_rule('/add', 'add', visitor_controller.add, methods=['POST'])
visitor_route.add_url_rule('/<int:id>', 'get', visitor_controller.get, methods=['GET'])
visitor_route.add_url_rule('/update', 'update', visitor_controller.update, methods=['PUT'])
visitor_route.add_url_rule('/delete/<int:id>', 'delete', visitor_controller.delete, methods=['DELETE'])
visitor_route.add_url_rule('/', 'get_all', visitor_controller.get_all, methods=['GET'])
visitor_route.add_url_rule('/search/', 'search', visitor_controller.search, methods=['GET'])
