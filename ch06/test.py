from flask import Flask, request, render_template, jsonify
import db_model
import sensor_dht

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")
    
@app.route("/now")
def now():
    try:
        current = sensor_dht.get_now()
        db_model.add(current[0],current[1])
        return current
    except: return "완전 실패함"

@app.route("/record")
def record():
    result = db_model.selectAll()
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001)

