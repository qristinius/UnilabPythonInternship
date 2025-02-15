from flask import Flask
from src.config import Config 
from src.views.main.routes import main_blueprint 
from src.views.books.routes import book_blueprint 
from src.views.useressay.routes import useressay_blueprint
from src.views.registration.routes import registration_blueprint
from src.views.login.routes import login_blueprint
from src.extensions import db , migrate, login_manager
from src.commands import init_db , populate_db
from src.models.registration import User

BLUEPRINTS = [main_blueprint,book_blueprint,useressay_blueprint, registration_blueprint,login_blueprint]
COMMANDS = [init_db, populate_db]

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_blueprint(app)
    register_extensions(app)
    register_commands(app)
    
    return app


def register_blueprint(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "login.login"

    @login_manager.user_loader
    def load_user(_id):
        return User.query.get(_id)
    
def register_commands(app):
    for command in COMMANDS:
        app.cli.add_command(command)