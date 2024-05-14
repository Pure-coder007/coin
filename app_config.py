from extensions import db, login_manager, migrate
from flask import redirect, flash, url_for, session, render_template, Flask
from view_functions import AuthenticationBlueprint, UserBlueprint, AdminBlueprint
from models import Users, Admins
from datetime import timedelta
import os
import flask


uri = os.getenv("DATABASE_URI", "postgres://bitnovia:eZotEmgUR0r361aU5peoAyCdj1i7tKSJ@dpg-cp1jn6e3e1ms738nku40-a.oregon-postgres.render.com/bitnovia_db")

print(uri, "uri")

if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)


def create_app():
    base_dir = os.path.dirname(os.path.realpath(__file__))

    app = Flask(__name__)

    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    #     base_dir, "service_hub.db"
    # )

    app.config["SQLALCHEMY_DATABASE_URI"] = uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "4f557e8e5eb51bfb7c42"
    app.config["DEBUG"] = False

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # The decorator that loads the user using the user's id
    @login_manager.user_loader
    def user_loader(id):
        user = Users.query.get(id)
        if not user:
            user = Admins.query.get(id)
        return user

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html"), 404

    # handler for unauthorized
    @app.errorhandler(401)
    def unauthorized(e):
        session["alert"] = "Login to access this page"
        session["bg_color"] = "danger"
        return redirect(url_for("auth.login"))

    app.register_blueprint(AuthenticationBlueprint)
    app.register_blueprint(UserBlueprint)
    app.register_blueprint(AdminBlueprint)

    return app
