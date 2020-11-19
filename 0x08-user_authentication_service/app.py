#!/usr/bin/env python3
"""
SQLAlchemy model User
"""
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth

app = Flask(__name__)
app.url_map.strict_slashes = False
AUTH = Auth()


@app.route('/', methods=['GET'])
def hello():
    """ GET/Return welcome message"""
    return jsonify({"message": "Bienvenue"}), 200


@app.route('/users', methods=['POST'])
def register():
    """register user using email and password"""
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except Exception:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
