from .repository import Repository
from flask import request, jsonify


class DashboardRepository(Repository):
    def __init__(self):
        super().__init__('dashboard')
