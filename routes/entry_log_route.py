from flask import Blueprint
from controllers import EntryLogController
from services import EntryLogService
from repositories import EntryLogRepository

entry_log_repository = EntryLogRepository()
entry_log_service = EntryLogService(entry_log_repository)
entry_log_controller = EntryLogController(entry_log_service)
entry_log_route = Blueprint('entry_log', __name__)
entry_log_route.add_url_rule('/add', 'add', entry_log_controller.add, methods=['POST'])
entry_log_route.add_url_rule('/<int:id>', 'get', entry_log_controller.get, methods=['GET'])
entry_log_route.add_url_rule('/update', 'update', entry_log_controller.update, methods=['PUT'])
entry_log_route.add_url_rule('/delete/<int:id>', 'delete', entry_log_controller.delete, methods=['DELETE'])
entry_log_route.add_url_rule('/', 'get_all', entry_log_controller.get_all, methods=['GET'])
entry_log_route.add_url_rule('/get_by/', 'get_by', entry_log_controller.get_by, methods=['GET'])
entry_log_route.add_url_rule('/search/', 'search', entry_log_controller.search, methods=['GET'])
entry_log_route.add_url_rule('/find_face', 'find_face', entry_log_controller.find_face, methods=['POST'])
