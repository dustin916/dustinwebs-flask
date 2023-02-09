from flask import Flask

import os
from os import path


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "This !s f0r Bu$sine$$ site"

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app
 