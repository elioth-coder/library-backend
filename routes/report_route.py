from flask import Blueprint
from controllers import ReportController
from services import ReportService
from repositories import ReportRepository

report_repository = ReportRepository()
report_service = ReportService(report_repository)
report_controller = ReportController(report_service)
report_route = Blueprint('report', __name__)
report_route.add_url_rule('/books_inventory/', 'books_inventory', report_controller.books_inventory, methods=['GET'])
