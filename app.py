from flask import Flask, jsonify, request


app = Flask(__name__)


_MESSAGE = {"text": ""}


@app.route("/hello", methods=["GET"])
def hello():
    return jsonify(message="Hello, World!")


@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json(force=True) or {}
    return jsonify(data), 201


@app.route("/message", methods=["GET", "PUT", "DELETE"])
def message():
    if request.method == "GET":
        return jsonify(message=_MESSAGE["text"])

    if request.method == "PUT":
        payload = request.get_json(force=True) or {}
        new_text = payload.get("message", "")
        _MESSAGE["text"] = str(new_text)
        return jsonify(message=_MESSAGE["text"]), 200

    # DELETE
    _MESSAGE["text"] = ""
    return jsonify(deleted=True, message=""), 200


if __name__ == "__main__":
    app.run(debug=True)
