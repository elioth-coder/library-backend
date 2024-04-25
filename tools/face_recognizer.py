import face_recognition
import cv2
import os
import glob
import numpy as np

class FaceRecognizer:
    def __init__(self, face_encodings):
        self.known_face_encodings = face_encodings

        # Resize frame for a faster speed
        self.frame_resizing = 0.25

    def detect_known_faces(self, image):
        match_index = -1
        if len(self.known_face_encodings) <= 0:
            return match_index

        small_frame = cv2.resize(image, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)
        # Find all the faces and face encodings in the current frame of video
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding, 0.4)
            match_index = -1

            if True in matches:
                match_index = matches.index(True)

        return match_index
