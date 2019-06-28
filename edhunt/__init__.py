# !/usr / bin / env python3
# coding: utf - 8

# logging
import logging
import os
from logging import warning, info, debug
logging.basicConfig(level=logging.INFO)
logging.basicConfig(format='%(levelname)s - %(message)s')
warning(f"{os.getcwd()}")


# flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin
from flask_mail import Mail
from edhunt.config import Config, Params


import pandas as pd
import numpy as np
from sklearn.cluster import SpectralClustering


# display
from pyvirtualdisplay import Display
if Params.HEADLESS_WEB_DRIVER:
    display = Display(visible=0, size=(1024, 768))
    display.start()

# app
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class=Config):

    app = Flask(__name__, template_folder="templates", static_folder='static')
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from edhunt.main.routes import main
    from edhunt.users.routes import users
    from edhunt.searchs.routes import searchs
    from edhunt.plateforms.routes import plateforms
    from edhunt.opportunities.routes import opportunities

    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(searchs)
    app.register_blueprint(opportunities)
    app.register_blueprint(plateforms)

    return app


# handle
__app = Flask(__name__, template_folder="templates", static_folder='static')
__app.config.from_object(Config)
db = SQLAlchemy(__app)

from edhunt.users import Users
from edhunt.plateforms import Plateforms
from edhunt.searchs import Searchs
from edhunt.opportunities import Opportunities
from edhunt.main import Main

# from edhunt.searchs.model import Search
# from edhunt.searchs.utils import SearchEnums

from edhunt.main.model import (School, Country, Town, Company, Job,
                               ZipCode, Departement, Region)
from edhunt.main.utils import *

from edhunt.opportunities.model import Opportunity

from edhunt.utils.db_admin import Db
from edhunt.utils import rename_resize_images
