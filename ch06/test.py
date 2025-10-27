from flask import Flask, request, render_template
import db_model
import sensor_dht

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")
    
@app.route("/now")
def now():
    temperature, huminity = sensor_dht.get_now()
    result = db_model.add(temperature, huminity)
    return result

@app.route("/record")
def record():
    result = db_model.selectAll()
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001)

