import cv2 as cv

import flask
from flask import Flask
from flask import Response
from flask import render_template

from threaded_camera import WebcamVideoStream 
#from threaded_camera2 import CameraStream

app = Flask(__name__);
cap = WebcamVideoStream().start();
#cap = CameraStream().start();

def gen():
	while cap:
		outputframe = cap.read();
		(flag, encodedImage) = cv.imencode(".jpg",outputframe);
		yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')
		

@app.route("/")
def index():
	return render_template("index.php");

@app.route("/video_feed")
def video_feed():
	return Response(gen(),mimetype="multipart/x-mixed-replace; boundary=frame");

if __name__ == "__main__":
	app.run(debug=True,port=80,host="0.0.0.0",threaded=True,use_reloader=False);

cap.stop();
