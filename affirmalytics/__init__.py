''' webserver for affirmalytics '''
from flask import Flask
import os

app = Flask(__name__)
app.config.from_object('config')

# TODO: create the database models
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['PSQL_URI']
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# import affirmalytics.models as affirmabase
# affirmabase.db.init_app(app)

import affirmalytics.views
