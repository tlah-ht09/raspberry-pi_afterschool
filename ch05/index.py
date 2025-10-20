from flask import Flask, request, render_template
import RPi.GPIO as GPIO



GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
servo = GPIO.PWM(16, 50)


def setAngle(angle):
    duty = 2.5 + 10 * int(angle) / 180
    print(f"degree : {angle} to {duty}(duty)")
    servo.ChangeDutyCycle(duty)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send/<value>")
def led_y_on(value):
    try:
        setAngle(value)
        return "ok"
    except:
        return "fail"


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
