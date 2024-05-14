from flask import Flask
from flask_cors import CORS
from routes import (
    user_route,
    author_route, 
    book_route, 
    book_author_route, 
    book_copy_route,
    borrowed_route,
    library_card_route,
    publisher_route,
    visitor_route,
    visitor_photo_route,
    entry_log_route,
    dashboard_route,
    member_route,
    reserve_route,
    queue_route,
    wishlist_route,
)

app = Flask(__name__)
app.secret_key = 'mansibang'
CORS(
    app, 
    resources={r"/*": {"origins": "http://localhost:5173"}}, 
    supports_credentials=True
)

app.register_blueprint(user_route, url_prefix='/api/user')
app.register_blueprint(author_route, url_prefix='/api/author')
app.register_blueprint(book_route, url_prefix='/api/book')
app.register_blueprint(book_author_route, url_prefix='/api/book_author')
app.register_blueprint(book_copy_route, url_prefix='/api/book_copy')
app.register_blueprint(borrowed_route, url_prefix='/api/borrowed')
app.register_blueprint(library_card_route, url_prefix='/api/library_card')
app.register_blueprint(publisher_route, url_prefix='/api/publisher')
app.register_blueprint(visitor_route, url_prefix='/api/visitor')
app.register_blueprint(visitor_photo_route, url_prefix='/api/visitor_photo')
app.register_blueprint(entry_log_route, url_prefix='/api/entry_log')
app.register_blueprint(dashboard_route, url_prefix='/api/dashboard')
app.register_blueprint(member_route, url_prefix='/api/member')
app.register_blueprint(reserve_route, url_prefix='/api/reserve')
app.register_blueprint(queue_route, url_prefix='/api/queue')
app.register_blueprint(wishlist_route, url_prefix='/api/wishlist')

if __name__ == "__main__":
    app.run(debug=True, port=4000, host="0.0.0.0")