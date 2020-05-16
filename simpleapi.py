#!/usr/bin/env python3.8

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class CompanyTimeline(Resource):

    def get(self):
        return {'text':'it works!'}


api.add_resource(CompanyTimeline, '/')


if __name__ == '__main__':
    app.run(debug=True)
