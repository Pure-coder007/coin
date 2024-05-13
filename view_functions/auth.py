from flask import Blueprint, render_template

authenticator = Blueprint("auth", __name__)


@authenticator.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@authenticator.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    return render_template("sign_up.html")


@authenticator.route("/reset_password", methods=["GET", "POST"])
def reset_password():
    return render_template("reset_password.html")
