import os, sys
from flask import Flask, jsonify
from flask_restful import Resource, Api

from flask_sqlalchemy import SQLAlchemy

# instantiate the app
app = Flask(__name__)
api = Api(app)


# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)
#print(app.config, file=sys.stderr) #ensure proper config was loaded

# instantiate the db
db = SQLAlchemy(app)

# model
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

@api.resource('/users/ping')
class UsersPing(Resource):
    def get(self):
        return { 'status': 'Success', 'message' : 'pong!'}
