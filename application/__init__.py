"""Initialize app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    print("start application/__init__.py > def create_app()")
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)

    # Application Configuration
    app.config.from_object('config.Config')
    #this loads class Config from ~/config.py
    #NB: this __init__.py file is loaded by wsgi.py > import create_app & app = create_app()

    with app.app_context():
        # Import parts of our application
        from . import routes
        #this loads ~/application/routes.py
        #
        # Register Blueprints
        app.register_blueprint(routes.main_bp)
        return app
