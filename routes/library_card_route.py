from flask import Blueprint
from controllers import LibraryCardController
from services import LibraryCardService
from repositories import LibraryCardRepository

library_card_repository = LibraryCardRepository()
library_card_service = LibraryCardService(library_card_repository)
library_card_controller = LibraryCardController(library_card_service)
library_card_route = Blueprint('library_card', __name__)
library_card_route.add_url_rule('/add', 'add', library_card_controller.add, methods=['POST'])
library_card_route.add_url_rule('/<int:id>', 'get', library_card_controller.get, methods=['GET'])
library_card_route.add_url_rule('/update', 'update', library_card_controller.update, methods=['PUT'])
library_card_route.add_url_rule('/delete/<int:id>', 'delete', library_card_controller.delete, methods=['DELETE'])
library_card_route.add_url_rule('/', 'get_all', library_card_controller.get_all, methods=['GET'])
library_card_route.add_url_rule('/search/', 'search', library_card_controller.search, methods=['GET'])
library_card_route.add_url_rule('/get_by/', 'get_by', library_card_controller.get_by, methods=['GET'])
library_card_route.add_url_rule('/get_one/', 'get_one', library_card_controller.get_one, methods=['GET'])
library_card_route.add_url_rule('/delete_by/', 'delete_by', library_card_controller.delete_by, methods=['DELETE'])
