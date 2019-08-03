import os
from flask import Flask, jsonify
from flask_restful import Resource, Api
import sys

# instantiate the app
app = Flask(__name__)
api = Api(app)


# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)
#print(app.config, file=sys.stderr) #ensure proper config was loaded

@api.resource('/users/ping')
class UsersPing(Resource):
    def get(self):
        return { 'status': 'Success', 'message' : 'pong!'}
