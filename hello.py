from flask import Flask
from flask_restful import Resource, Api, reqparse
import ast

app = Flask(__name__)
api = Api(app)

class Welcome(Resource):
	def get(self):
		return 'Hello, world!', 200  # return data and 200 OK code# methods go here

api.add_resource(Welcome, '/')  # '/' is our welcome entry point

if __name__ == "__main__":
	# instead of app.run()
	from waitress import serve
	serve(app, host="0.0.0.0", port=8080)