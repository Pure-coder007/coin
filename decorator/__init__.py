from models import Users, Admins
from flask_login import current_user
from flask import url_for, redirect, session
from functools import wraps


# decorator admin required
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not Admins.query.get(current_user.id):
            session["alert"] = "You cannot access this page"
            session["bg_color"] = "danger"
            return redirect(url_for('users.index'))
        return f(*args, **kwargs)
    return decorated_function


# user decorator
def user_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not Users.query.get(current_user.id):
            session["alert"] = "You cannot access this page"
            session["bg_color"] = "danger"
            return redirect(url_for('users.index'))
        return f(*args, **kwargs)
    return decorated_function
