import os

from flask import Flask
from flask_restful import Resource, Api
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
api = Api(app)

app.run(port=os.environ['PORT'])