from flask import Blueprint
from controllers import DashboardController
from services import DashboardService
from repositories import DashboardRepository

dashboard_repository = DashboardRepository()
dashboard_service = DashboardService(dashboard_repository)
dashboard_controller = DashboardController(dashboard_service)
dashboard_route = Blueprint('dashboard', __name__)
dashboard_route.add_url_rule('/count_books/', 'count_books', dashboard_controller.count_books, methods=['GET'])
dashboard_route.add_url_rule('/daily_visitors/', 'daily_visitors', dashboard_controller.daily_visitors, methods=['GET'])
