from .service import Service
import base64
import os
from datetime import datetime
from pathlib import Path

class BookService(Service):
    def __init__(self, repository):
        super().__init__(repository)

    def save_image(self, base64_data):
        data = base64_data.split(',')[1]
        decoded_bytes = base64.b64decode(str.encode(data))
        current_time = datetime.now()
        current_milliseconds = int(current_time.timestamp() * 1000)
        filename = 'book_cover' + str(current_milliseconds) + '.png'

        with open(os.path.join('static/uploads', filename), 'wb') as f:
            f.write(decoded_bytes)
    
        return filename

    def delete_image(self, filename): 
        file_path = Path(os.path.join('static/uploads', filename))
        if file_path.exists():
            os.remove(file_path)