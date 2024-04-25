from flask import Blueprint
from controllers import VisitorPhotoController
from services import VisitorPhotoService
from repositories import VisitorPhotoRepository

visitor_photo_repository = VisitorPhotoRepository()
visitor_photo_service = VisitorPhotoService(visitor_photo_repository)
visitor_photo_controller = VisitorPhotoController(visitor_photo_service)
visitor_photo_route = Blueprint('visitor_photo', __name__)
visitor_photo_route.add_url_rule('/add', 'add', visitor_photo_controller.add, methods=['POST'])
visitor_photo_route.add_url_rule('/<int:id>', 'get', visitor_photo_controller.get, methods=['GET'])
visitor_photo_route.add_url_rule('/update', 'update', visitor_photo_controller.update, methods=['PUT'])
visitor_photo_route.add_url_rule('/delete/<int:id>', 'delete', visitor_photo_controller.delete, methods=['DELETE'])
visitor_photo_route.add_url_rule('/', 'get_all', visitor_photo_controller.get_all, methods=['GET'])
visitor_photo_route.add_url_rule('/get_by/', 'get_by', visitor_photo_controller.get_by, methods=['GET'])
visitor_photo_route.add_url_rule('/get_one/', 'get_one', visitor_photo_controller.get_one, methods=['GET'])
visitor_photo_route.add_url_rule('/search/', 'search', visitor_photo_controller.search, methods=['GET'])
visitor_photo_route.add_url_rule('/delete_by/', 'delete_by', visitor_photo_controller.delete_by, methods=['DELETE'])
