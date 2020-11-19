#!/usr/bin/env python3
"""
SQLAlchemy model User
"""
from flask import Flask, jsonify, request, abort, redirect

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/', methods=['GET'])
def hello():
    """ GET/Return welcome message"""
    return jsonify({"message": "Bienvenue"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
