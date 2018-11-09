from flask import Flask, jsonify, request
import math

app = Flask(__name__)  # Flask running as imported object in program


@app.route("/name", methods=["GET"])
def name():
    dictionary = {
        "name": "Erica"
    }
    return jsonify(dictionary)


@app.route("/hello/<name>", methods=["GET"])
def hello(name):
    dictionary = {
        "message": "Hello there, {}".format(name)
    }
    return jsonify(dictionary)


@app.route("/distance", methods=["POST"])
def distance():
    r = request.get_json() #already parsed
    # p = r.json()
    a = r["a"]
    b = r["b"]
    temp = (b[1]-a[1]) ^ 2 + (b[0]-a[0]) ^ 2
    d = math.sqrt(temp)
    print(d)
    return jsonify(d)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
