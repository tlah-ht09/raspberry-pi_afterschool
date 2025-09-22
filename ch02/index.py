from flask import Flask, render_template, redirect, url_for, request
import pymysql

conn = pymysql.connect(host='localhost',user="root",password="q1w2e3",db="study")
cur = conn.cursor()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

"""@app.route("/<num>")
def asd(num):
    cur.execute(f"insert into numcount(num) values({num})")
    conn.commit()
    print(num)
    return redirect(url_for("home"))"""


@app.route("/submit", methods=["POST"])
def save_db():
    data = request.get_json()
    print(data.get("value"))
    cur.execute(f"insert into numcount(num) values({data.get("value")})")
    conn.commit()
    conn.close()2
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(port="5001",host="0.0.0.0")