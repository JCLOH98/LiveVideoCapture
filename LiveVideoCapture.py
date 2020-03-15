import cv2 as cv

import flask
from flask import Flask
from flask import Response
from flask import render_template

app = Flask(__name__);

def gen():
	cap = cv.VideoCapture(0);
	while cap.isOpened():
		_,frame = cap.read();
		mirrorframe = cv.flip(frame,1);
		flag, encodedImage = cv.imencode(".jpg",mirrorframe);
		yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')
		#cv.imshow("LiveVideo",frame);
		#if (cv.waitKey(1) == ord("q")):
			#break;
	#cv.destroyAllWindows();
	cap.release();

@app.route("/")
def index():
	return render_template("index.php");
@app.route("/video_feed")
def video_feed():
	return Response(gen(),mimetype="multipart/x-mixed-replace; boundary=frame");

if __name__ == "__main__":
	app.run(debug=True,port=80,host="0.0.0.0");

