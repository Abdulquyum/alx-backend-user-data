
#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, jsonify, request, abort
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound
import uuid

app = Flask(__name__)

AUTH = Auth()


@app.route("/", methods=['GET'], strict_slashes=False)
def basic():
    """basic route"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'], strict_slashes=False)
def users():
    """Register user"""
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({
            "email": email,
            "message": "user created"
            })
    except ValueError as e:
        return jsonify({
            "message": "email already registered"
            }), 400


@app.route("/sessions", methods=['POST'], strict_slashes=False)   
def login():
    """Log in authorized user"""
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        if AUTH.valid_login(email, password):
            session_id = AUTH.create_session(email)
            response = jsonify({"email": email, "message": "logged in"})
            response.set_cookie('session_id', session_id)
            return response
                
        abort(401)
            
    except NoResultFound:
            abort(401)


@app.route("/sessions", methods=['DELETE'], strict_slashes=False)
def logout():
    """Delete session"""
    session_id = request.cookies.get('session_id')
    if session_id is None:
        abort(403)
    try:
        user = AUTH.get_user_from_session_id(session_id)
        if user:
            AUTH.destroy_session(user.id)
            return redirect("/")
        abort(403)
    except NoResultFound:
        abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """get user email"""
    session_id = request.cookies.get('session_id')
    if session_id is None:
        abort(403)
    try:
        user = AUTH.get_user_from_session_id(session_id)
        if user:
            return jsonify({"email": user.email}), 200
    except NoResultFound:
        abort(403)


    @app.route('/reset_password', methods=['POST'], strict_slashes=False)
    def get_reset_password_token():
        """get rest password token"""
        try:
            email = request.form.get('email')

            if email is None:
                abort(403)

            reset_token = AUTH.get_reset_password_token(email)
            return jsonify({ "email": email, "reset_token": reset_token })

        except NoresultFound:
            abort(403)


    @app.route('/reset_password', methods=["PUT"], strict_slashes=False)
    def update_password():
        """update Password """
        try:
            email = request.form.get("email")
            reset_token = request.form.get('reset_token')
            new_password = request.form.get('new_password')

            if reset_token is None:
                abort(403)

            AUTH.update_password(reset_token, new_password)

            return jsonify({"email": email, "message": "Password updated"}), 200

        except NoResultFound:
            abort(403)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port="5000")
