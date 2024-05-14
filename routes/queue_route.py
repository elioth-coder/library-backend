from flask import Blueprint
from controllers import QueueController
from services import QueueService
from repositories import QueueRepository

queue_repository = QueueRepository()
queue_service = QueueService(queue_repository)
queue_controller = QueueController(queue_service)
queue_route = Blueprint('queue', __name__)
queue_route.add_url_rule('/add', 'add', queue_controller.add, methods=['POST'])
queue_route.add_url_rule('/<int:id>', 'get', queue_controller.get, methods=['GET'])
queue_route.add_url_rule('/update', 'update', queue_controller.update, methods=['PUT'])
queue_route.add_url_rule('/delete/<int:id>', 'delete', queue_controller.delete, methods=['DELETE'])
queue_route.add_url_rule('/', 'get_all', queue_controller.get_all, methods=['GET'])
queue_route.add_url_rule('/search/', 'search', queue_controller.search, methods=['GET'])
