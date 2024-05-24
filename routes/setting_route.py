from flask import Blueprint
from controllers import SettingController
from services import SettingService
from repositories import SettingRepository

setting_repository = SettingRepository()
setting_service = SettingService(setting_repository)
setting_controller = SettingController(setting_service)
setting_route = Blueprint('setting', __name__)
setting_route.add_url_rule('/add', 'add', setting_controller.add, methods=['POST'])
setting_route.add_url_rule('/<int:id>', 'get', setting_controller.get, methods=['GET'])
setting_route.add_url_rule('/update', 'update', setting_controller.update, methods=['PUT'])
setting_route.add_url_rule('/delete/<int:id>', 'delete', setting_controller.delete, methods=['DELETE'])
setting_route.add_url_rule('/', 'get_all', setting_controller.get_all, methods=['GET'])
setting_route.add_url_rule('/search/', 'search', setting_controller.search, methods=['GET'])
setting_route.add_url_rule('/search_by/', 'search_by', setting_controller.search_by, methods=['GET'])
setting_route.add_url_rule('/delete_by/', 'delete_by', setting_controller.delete_by, methods=['DELETE'])
setting_route.add_url_rule('/count/', 'count', setting_controller.count, methods=['GET'])
setting_route.add_url_rule('/get_one/', 'get_one', setting_controller.get_one, methods=['GET'])
