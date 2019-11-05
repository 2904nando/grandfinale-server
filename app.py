from flask import Flask, render_template, redirect, request, Response, url_for
import pigpio
import time

app = Flask(__name__)

pi = pigpio.pi()
pi.set_mode(2, pigpio.OUTPUT)
pi.set_mode(3, pigpio.OUTPUT)
pi.set_mode(4, pigpio.OUTPUT)
pi.set_mode(17, pigpio.OUTPUT)

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

@app.route("/servoHorizontal")
def servo():
    pos = request.args.get('position')
    pi.set_servo_pulsewidth(4, pos)
    return "ok"

@app.route("/servoVertical")
def servo2():
    pos = request.args.get('position')
    pi.set_servo_pulsewidth(17, pos)
    return "ok"

@app.route("/getTemperatura")
def temperatura():
    temperatura = 26 #Ainda a ser implementado sensor de temperatura e umidade Dht22
    return temperatura

@app.route("/getUmidade")
def umidade():
    umidade = 75 #Ainda a ser implementado sensor de temperatura e umidade Dht22
    return umidade

if __name__ == "__main__":
    app.run(debug=True, host="192.168.15.5")