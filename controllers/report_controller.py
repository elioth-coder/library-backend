from .controller import Controller
from flask import request, jsonify

class ReportController(Controller):
    def __init__(self, service):
        super().__init__(service, [])

    def books_inventory(self):
        sql = """
        SELECT `isbn`, `title`,
            (SELECT COUNT(*) FROM `book_copy` WHERE `book_id`=`book`.`id` AND `status`='Available') AS `available`,
            (SELECT COUNT(*) FROM `book_copy` WHERE `book_id`=`book`.`id`  AND `status`='Borrowed') AS `borrowed`,
            (SELECT COUNT(*) FROM `book_copy` WHERE `book_id`=`book`.`id`  AND `status`='Damaged') AS `damaged`,
            (SELECT COUNT(*) FROM `book_copy` WHERE `book_id`=`book`.`id`  AND `status`='Lost') AS `lost`
        FROM `book`;
        """
        results = self.service.query(sql)

        data = {
            'status' : 'success',
            'results': results,
        }
        response = jsonify(data)
        return response, 200