from .controller import Controller
from flask import request, jsonify

class DashboardController(Controller):
    def __init__(self, service):
        super().__init__(service, [])

    def count_books(self): 
        status = request.args.get('status')
        statuses = status.split(',')

        if statuses[0]=="New":
            sql = "SELECT COUNT(`id`) AS `count` FROM `book_copy` WHERE `status` NOT IN ('Missing') and `date_added`>=DATE_SUB(CURDATE(), INTERVAL 2 WEEK)"
            results = self.service.query(sql)
        else:
            sql = "SELECT COUNT(`id`) AS `count` FROM `book_copy` WHERE `status` IN (%s)"
            placeholders = ', '.join(['%s'] * len(statuses))
            sql = sql % placeholders
            results = self.service.query(sql, statuses)

        data = {
            'status' : 'success',
            'results': results,
        }
        response = jsonify(data)
        return response, 200

    def daily_visitors(self):
        sql = """
        SELECT 
            COUNT(DISTINCT CASE WHEN DATE(dt_logged) = CURDATE() THEN member_id ELSE NULL END) AS day_7,
            COUNT(DISTINCT CASE WHEN DATE(dt_logged) = CURDATE() - INTERVAL 1 DAY THEN member_id ELSE NULL END) AS day_6,
            COUNT(DISTINCT CASE WHEN DATE(dt_logged) = CURDATE() - INTERVAL 2 DAY THEN member_id ELSE NULL END) AS day_5,
            COUNT(DISTINCT CASE WHEN DATE(dt_logged) = CURDATE() - INTERVAL 3 DAY THEN member_id ELSE NULL END) AS day_4,
            COUNT(DISTINCT CASE WHEN DATE(dt_logged) = CURDATE() - INTERVAL 4 DAY THEN member_id ELSE NULL END) AS day_3,
            COUNT(DISTINCT CASE WHEN DATE(dt_logged) = CURDATE() - INTERVAL 5 DAY THEN member_id ELSE NULL END) AS day_2,
            COUNT(DISTINCT CASE WHEN DATE(dt_logged) = CURDATE() - INTERVAL 6 DAY THEN member_id ELSE NULL END) AS day_1
        FROM 
            entry_log
        """
        results = self.service.query(sql)

        data = {
            'status' : 'success',
            'results': results,
        }
        response = jsonify(data)
        return response, 200