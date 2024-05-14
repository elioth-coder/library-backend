from .service import Service
from datetime import datetime
import base64
import os
import face_recognition
import cv2
import pickle
from pathlib import Path


class MemberService(Service):
    def __init__(self, repository):
        super().__init__(repository)

    def save_image(self, base64_data):
        data = base64_data.split(',')[1]
        decoded_bytes = base64.b64decode(str.encode(data))
        current_time = datetime.now()
        current_milliseconds = int(current_time.timestamp() * 1000)
        filename = 'member' + str(current_milliseconds) + '.png'

        with open(os.path.join('static/uploads', filename), 'wb') as f:
            f.write(decoded_bytes)
    
        return filename

    def extract_encoding(self, filename):
        img_path = os.path.join('static/uploads', filename)
        img = cv2.imread(img_path)
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encoding = face_recognition.face_encodings(rgb_img)[0]

        return pickle.dumps(encoding)

    def delete_image(self, filename): 
        file_path = Path(os.path.join('static/uploads', filename))
        if file_path.exists():
            os.remove(file_path)