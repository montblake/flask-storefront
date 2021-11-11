from flask import Flask, render_template
import os
from logging.handlers import RotatingFileHandler
import logging
from flask.logging import default_handler
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


#######################
#### Configuration ####
#######################

# Create the instances of the Flask extensions in the global scope,
# but without any arguments passed in. These instances are not
# attached to the Flask application at this point.
db = SQLAlchemy()
db_migration = Migrate()


######################################
#### Application Factory Function ####
######################################
def create_app():
    # Create the Flask application
    app = Flask(__name__)

    # Configure the Flask application
    config_type = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.config.from_object(config_type)
    
    initialize_extensions(app)
    register_blueprints(app)
    configure_logging(app)
    register_error_pages(app)
    return app

########################
### Helper Functions ###
########################


def initialize_extensions(app):
    # Since the application instance is now created, pass it to each Flask
    # extension instance to bind it to the Flask application instance (app)
    db.init_app(app)
    db_migration.init_app(app, db)


def register_blueprints(app):
    from app.products import products_blueprint
    from app.users import users_blueprint

    app.register_blueprint(products_blueprint)
    app.register_blueprint(users_blueprint, url_prefix='/users')


def configure_logging(app):
    # Logging Configuration
    file_handler = RotatingFileHandler('instance/marketplace-of-ideas.log',
                                    maxBytes=16384,
                                    backupCount=20)
    file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(filename)s:%(lineno)d]')
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    # Remove the default logger configured by Flask
    app.logger.removeHandler(default_handler)

    # Log that the Flask application is starting
    app.logger.info('Starting the Marketplace of Ideas app...')


def register_error_pages(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(405)
    def method_not_allowed(e):
        return render_template('405.html'), 405

