from flask import Flask, request, render_template
import RPi.GPIO as GPIO
import db_model


app = Flask(__name__)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/y")
def led_y_on():
    try:
        GPIO.output(12, GPIO.HIGH)
        return "ok"
    except:
        return "fail"

@app.route("/r")
def led_r_on():
    try:
        GPIO.output(10, GPIO.HIGH)
        return "ok"
    except:
        return "fail"

@app.route("/g")
def led_g_on():
    try:
        GPIO.output(8, GPIO.HIGH)
        return "ok"
    except:
        return "fail"

@app.route("/off")
def led_off():
    try:
        GPIO.output(8, GPIO.LOW)
        GPIO.output(10, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
        return "ok"
    except:
        return "fail"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
