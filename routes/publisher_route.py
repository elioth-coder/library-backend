from flask import Blueprint
from controllers import PublisherController
from services import PublisherService
from repositories import PublisherRepository

publisher_repository = PublisherRepository()
publisher_service = PublisherService(publisher_repository)
publisher_controller = PublisherController(publisher_service)
publisher_route = Blueprint('publisher', __name__)
publisher_route.add_url_rule('/add', 'add', publisher_controller.add, methods=['POST'])
publisher_route.add_url_rule('/<int:id>', 'get', publisher_controller.get, methods=['GET'])
publisher_route.add_url_rule('/update', 'update', publisher_controller.update, methods=['PUT'])
publisher_route.add_url_rule('/delete/<int:id>', 'delete', publisher_controller.delete, methods=['DELETE'])
publisher_route.add_url_rule('/', 'get_all', publisher_controller.get_all, methods=['GET'])
publisher_route.add_url_rule('/search/', 'search', publisher_controller.search, methods=['GET'])
publisher_route.add_url_rule('/search_by/', 'search_by', publisher_controller.search_by, methods=['GET'])
