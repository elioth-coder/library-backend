from .service import Service
from repositories.member_repository import MemberRepository
from .member_service import MemberService
from tools.face_recognizer import FaceRecognizer
from datetime import datetime
import os
import face_recognition
import cv2
import base64
from PIL import Image
from io import BytesIO
import pickle
import numpy as np
from pathlib import Path

class EntryLogService(Service):
    def __init__(self, repository):
        super().__init__(repository)

    def save_image(self, base64_data):
        data = base64_data.split(',')[1]
        decoded_bytes = base64.b64decode(str.encode(data))
        current_time = datetime.now()
        current_milliseconds = int(current_time.timestamp() * 1000)
        filename = 'entry_log_photo' + str(current_milliseconds) + '.png'

        with open(os.path.join('static/uploads', filename), 'wb') as f:
            f.write(decoded_bytes)
    
        return filename

    def delete_image(self, filename): 
        file_path = Path(os.path.join('static/uploads', filename))
        if file_path.exists():
            os.remove(file_path)

    def get_members(self): 
        member_repository = MemberRepository()
        member_service = MemberService(member_repository)
        members = member_service.get_all()

        return members

    def get_member(self, member_id):
        member_repository = MemberRepository()
        member_service = MemberService(member_repository)
        member = member_service.get(member_id)

        return member

    def extract_encodings(self, photos):        
        encodings = []
        for photo in photos:            
            encodings.append(pickle.loads(photo['encoding']))

        return encodings

    def find_face(self, encodings, image): 
        image_np = np.array(image)
        face_recognizer = FaceRecognizer(encodings)
        match_index = face_recognizer.detect_known_faces(image_np)

        return match_index

    def base64_to_image(self, base64_data):
        data = base64_data.split(',')[1]
        image_data = base64.b64decode(data)
        img_stream = BytesIO(image_data)
        image = Image.open(img_stream)
        
        return image

            