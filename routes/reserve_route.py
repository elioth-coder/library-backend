from flask import Blueprint
from controllers import ReserveController
from services import ReserveService
from repositories import ReserveRepository

reserve_repository = ReserveRepository()
reserve_service = ReserveService(reserve_repository)
reserve_controller = ReserveController(reserve_service)
reserve_route = Blueprint('reserve', __name__)
reserve_route.add_url_rule('/add', 'add', reserve_controller.add, methods=['POST'])
reserve_route.add_url_rule('/<int:id>', 'get', reserve_controller.get, methods=['GET'])
reserve_route.add_url_rule('/update', 'update', reserve_controller.update, methods=['PUT'])
reserve_route.add_url_rule('/delete/<int:id>', 'delete', reserve_controller.delete, methods=['DELETE'])
reserve_route.add_url_rule('/', 'get_all', reserve_controller.get_all, methods=['GET'])
reserve_route.add_url_rule('/search/', 'search', reserve_controller.search, methods=['GET'])
reserve_route.add_url_rule('/get_by/', 'get_by', reserve_controller.get_by, methods=['GET'])
reserve_route.add_url_rule('/delete_by/', 'delete_by', reserve_controller.delete_by, methods=['DELETE'])
reserve_route.add_url_rule('/count/', 'count', reserve_controller.count, methods=['GET'])
reserve_route.add_url_rule('/count_by/', 'count_by', reserve_controller.count_by, methods=['GET'])

