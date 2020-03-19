import cv2 as cv

import flask
from flask import Flask
from flask import Response
from flask import render_template

import threading
from threading import Lock
from threading import Thread

outputfrmae = None;
lock = Lock();

app = Flask(__name__);
cap = cv.VideoCapture(0);

def frame():
	global lock, cap, outputframe;
	while True:
		ret, frame = cap.read();
		mirrorframe = cv.flip(frame,1);
		lock.acquire();
		outputframe = mirrorframe;
		lock.release();

def gen():
	global outputframe;
	while True:
		(flag, encodedImage) = cv.imencode(".jpg",outputframe);
		yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')
		

@app.route("/")
def index():
	return render_template("index.php");

@app.route("/video_feed")
def video_feed():
	return Response(gen(),mimetype="multipart/x-mixed-replace; boundary=frame");

if __name__ == "__main__":
	t = Thread(target=frame,args=());
	t.daemon = True;
	t.start();
	app.run(debug=True,port=80,host="0.0.0.0",threaded=True,use_reloader=False);

cap.release();
