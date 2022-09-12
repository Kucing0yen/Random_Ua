from urllib import response
from flask import Flask,request
from flask_restful import Resource, Api
from flask_cors import CORS
from fake_useragent import UserAgent

app=Flask(__name__)
api=Api(app)

CORS(app)

identitas={}

class Usa(Resource):
    def get(self):
        user_agent=UserAgent()
        getting=user_agent.random
        return ({
            'status':'success',
            'user_agent':getting

        })

api.add_resource(Usa, "/first/ua")

if __name__ == "__main__":
    app.run(debug=True, port=5005)