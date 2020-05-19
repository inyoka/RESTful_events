#!/usr/bin/env python3.8

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


eventRegister = []


class CompanyTimeline(Resource):

    def get(self, name):
        
        for event in eventRegister:
            if event['name'] == name:
                return event

        return {'name':None}, 404


    def post(self, name):
        
        event = {'name': name}

        eventRegister.append(event)

        return event

    def delete(self, name):
        
        for index, event in enumerate(eventRegister):
            if event['name'] == name:
                deleted_event = eventRegister.pop(index)
                return {'note':'Event deleted'}


class AllEvents(Resource):

    def get(self):
        return {'events':eventRegister}

api.add_resource(CompanyTimeline, '/event/<string:name>')
api.add_resource(AllEvents, '/events')


if __name__ == '__main__':
    app.run(debug=True)
