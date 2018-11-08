from flask import Flask, jsonify, request
import math

app = Flask(__name__)  # Flask running as imported object in program


@app.route("/name", methods=["GET"])
def name():
    dictionary = {
        "name": "Erica"
    }
    my_name = dictionary.json()
    return my_name


@app.route("/hello/<name>", methods=["GET"])
def hello(name):
    dictionary = {
        "message": "Hello there, {}".format(name)
    }
    return jsonify(dictionary)


@app.route("/distance", methods=["POST"])
def distance():
    r = request.get_json()
    p = r.json
    a, b = p[0, 1]
    d = (b(1)-a(1)) ^ 2 + (b(0)-a(0)) ^ 2
    d = math.sqrt(d)
    print(d)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
