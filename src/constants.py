from flask import Flask
from redis import Redis
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
redis = Redis(host='cache', port=6379)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
