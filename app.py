from flask import Flask, render_template, redirect, request, Response, url_for
import pigpio
import cv2
from imutils.video import VideoStream
import time

app = Flask(__name__)

pi = pigpio.pi()
pi.set_mode(2, pigpio.OUTPUT)
pi.set_mode(3, pigpio.OUTPUT)
pi.set_mode(4, pigpio.OUTPUT)
pi.set_mode(17, pigpio.OUTPUT)

vs = VideoStream(src=0).start()
time.sleep(2.0)

@app.route("/")
def index():
    pi.set_servo_pulsewidth(4, 1500)
    pi.set_servo_pulsewidth(17, 1500)
    return render_template("index.html")

def gen():
    while True:
        frame = vs.read()
        cv2.imwrite('pic.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('pic.jpg', 'rb').read() + b'\r\n')
        
@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/ligarLed")
def ligar():
    pi.write(2, 1)
    return "ok"
    #return redirect("/")

@app.route("/desligarLed")
def desligar():
    pi.write(2, 0)
    return "ok"
    #return redirect("/")

@app.route("/servo")
def servo():
    pos = request.args.get('position')
    pi.set_servo_pulsewidth(4, pos)
    return "ok"

@app.route("/servo2")
def servo2():
    pos = request.args.get('position')
    pi.set_servo_pulsewidth(17, pos)
    return "ok"

if __name__ == "__main__":
    app.run(debug=True, host="192.168.15.5")