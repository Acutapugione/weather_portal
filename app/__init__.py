from flask import Flask
# from flask_cors import CORS
from os import getenv

from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()
api_key = getenv("API_KEY")
# CORS(app)

from . import routes