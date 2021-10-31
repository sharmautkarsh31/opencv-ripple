import cv2
import flask
from flask import jsonify, Response, stream_with_context

from pose_tracking import PoseDetector
from flask_cors import cross_origin

from universal_variable import Cordinates

cordinates = Cordinates()

app = flask.Flask(__name__)
app.config["DEBUG"] = True

cap = cv2.VideoCapture(0)

#screen resolution
# cap.set(3,1920)
# cap.set(4,1080)

detector = PoseDetector()

@app.route('/cordinates', methods=['GET'])
@cross_origin(supports_credentials=True)
def cordinate():
    return_cordinates = cordinates.get_cordinates()
    cordinates.set_cordinates_null()
    return jsonify(return_cordinates)

@app.route('/', methods=['GET'])
@cross_origin(supports_credentials=True)
def home():
    while True:
        success, img = cap.read()
        img = cv2.flip(img,1)
        img = detector.findPose(img)

        lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False)
        if bboxInfo:
            center = bboxInfo["center"]
            cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)
        if len(lmList) != 0:
            cordinates.set_cordinated([lmList[0][1:],lmList[1][1:]])

        # cv2.imshow("Image", img)
        cv2.waitKey(1)

# app.run()
