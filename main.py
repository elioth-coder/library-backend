from flask import Flask
from flask_cors import CORS
from routes import (
    user_route,
    book_route, 
    book_copy_route,
    borrowed_route,
    entry_log_route,
    dashboard_route,
    member_route,
    reserve_route,
    queue_route,
    wishlist_route,
    report_route,
    campus_route,
    setting_route,
)

app = Flask(__name__)
app.secret_key = 'mansibang'
CORS(
    app, 
    # resources={r"/*": {"origins": "http://localhost:5173"}}, 
    resources={r"/*": {"origins": "*"}}, 
    supports_credentials=True
)

app.register_blueprint(user_route, url_prefix='/api/user')
app.register_blueprint(book_route, url_prefix='/api/book')
app.register_blueprint(book_copy_route, url_prefix='/api/book_copy')
app.register_blueprint(borrowed_route, url_prefix='/api/borrowed')
app.register_blueprint(entry_log_route, url_prefix='/api/entry_log')
app.register_blueprint(dashboard_route, url_prefix='/api/dashboard')
app.register_blueprint(member_route, url_prefix='/api/member')
app.register_blueprint(reserve_route, url_prefix='/api/reserve')
app.register_blueprint(queue_route, url_prefix='/api/queue')
app.register_blueprint(wishlist_route, url_prefix='/api/wishlist')
app.register_blueprint(report_route, url_prefix='/api/report')
app.register_blueprint(campus_route, url_prefix='/api/campus')
app.register_blueprint(setting_route, url_prefix='/api/setting')

if __name__ == "__main__":
    app.run(debug=True, port=4000, host="0.0.0.0")