from extensions import db
from datetime import datetime, timedelta
import uuid
from passlib.hash import pbkdf2_sha256 as sha256
from flask_login import UserMixin
import random
import re


def generate_random_otp():
    otp = random.randint(100000, 999999)
    return str(otp)


def hexid():
    return uuid.uuid4().hex


class Users(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.String(50), primary_key=True, default=hexid)
    fullname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(100), nullable=False, unique=True)
    dob = db.Column(db.Date, nullable=False)
    address = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=True)
    show_message = db.Column(db.Boolean, default=False)
    occupation = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    password = db.Column(db.Text, nullable=False)
    pswd = db.Column(db.Text, nullable=False)

    @staticmethod
    def password_validation(password):
        if len(password) < 8:
            return "password must contain at least 8 characters"
        if password.isnumeric():
            return "password cannot contain only numbers"
        if password.isalpha():
            return "password cannot contain only alphabets"
        if password.isalnum():
            return "password too weak add more characters"
        return "success"

    @staticmethod
    def hash_password(password):
        return sha256.hash(password)

    @staticmethod
    def verify_password(password, hashed):
        return sha256.verify(password, hashed)

    @staticmethod
    def verify_email(email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)


class Admins(db.Model, UserMixin):
    __tablename__ = "admins"
    id = db.Column(db.String(50), primary_key=True, default=hexid)
    fullname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
