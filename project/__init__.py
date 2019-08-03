from flask import Flask, jsonify
from flask_restful import Resource, Api

# instantiate the app
app = Flask(__name__)
api = Api(app)


# set config
app.config.from_object('project.config.DevelopmentConfig') # new


@api.resource('/users/ping')
class UsersPing(Resource):
    def get(self):
        return { 'status': 'Success', 'message' : 'pong!'}

# https://testdriven.io/courses/microservices-with-docker-flask-and-react/part-one-getting-started/