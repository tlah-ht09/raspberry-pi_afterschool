from flask import Flask, request

app=Flask(__name__)

@app.route('/')
def hello():
    a = request.args.get('name')
    return f"hello {a}, it's flask world"


@app.route("/hi")
def hi():
    return "hi world"

@app.route("/hello")
def hello2():
    return "hello world"

@app.route("/<a>")
def test(a):
    return a + 'vv'


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5001)

