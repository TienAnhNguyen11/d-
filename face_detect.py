from flask import Flask, request
from flask_cors import CORS, cross_origin

import numpy as np
import cv2
import base64

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADER'] = 'Content-Type'


def face_counting(face):
    # khoi tao bo phat hien khuon mat
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    # chuyen anh mau thanh anh gray
    gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    # dem so mat trong anh
    faces = face_cascade.detectMultiScale(gray, 1.2, 10)

    face_number = len(faces)
    return face_number


def convert_base64_into_image(base64_image):
    try:
        base64_image = np.fromstring(base64.b64decode(base64_image), dtype=np.uint8)
        base64_image = cv2.imdecode(base64_image, cv2.IMREAD_ANYCOLOR)
    except:
        return None
    return base64_image

@app.route('/face-detecting', methods=['POST'])
@cross_origin(origin='*')

def face_detecting_process():
    face_numbers = 0

    # doc anh tu client gui len
    facebase64 = request.form.get('facebase64')

    # chuyen base64 ve OpenCV format
    face = convert_base64_into_image(facebase64)

    # dem so mat trong anh
    face_numbers = face_counting(face)

    # tra ve
    return "So mat la: " + str(face_numbers)

# start backend
if __name__ == "__main__":
    app.run()