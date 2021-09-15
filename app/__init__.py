from flask import Flask
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()
app = Flask(__name__)
bootstrap.init_app(app)
from . import views, error

""" 
def create_app(config_name):
 
    # initialize the application
    app = Flask(__name__)

    # initialize bootstrap
    bootstrap.init_app(app)

    from . import views, error

    return app
"""