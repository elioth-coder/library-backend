from flask import Blueprint
from controllers import WishlistController
from services import WishlistService
from repositories import WishlistRepository

wishlist_repository = WishlistRepository()
wishlist_service = WishlistService(wishlist_repository)
wishlist_controller = WishlistController(wishlist_service)
wishlist_route = Blueprint('wishlist', __name__)
wishlist_route.add_url_rule('/add', 'add', wishlist_controller.add, methods=['POST'])
wishlist_route.add_url_rule('/<int:id>', 'get', wishlist_controller.get, methods=['GET'])
wishlist_route.add_url_rule('/update', 'update', wishlist_controller.update, methods=['PUT'])
wishlist_route.add_url_rule('/delete/<int:id>', 'delete', wishlist_controller.delete, methods=['DELETE'])
wishlist_route.add_url_rule('/', 'get_all', wishlist_controller.get_all, methods=['GET'])
wishlist_route.add_url_rule('/search/', 'search', wishlist_controller.search, methods=['GET'])
