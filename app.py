import os

from flask import Flask

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from dotenv import load_dotenv
load_dotenv()

CONNECTION_URI = os.getenv("URI")
client = MongoClient(CONNECTION_URI, server_api=ServerApi('1'))

app = Flask(__name__)

@app.route("/")
def acceuil() :
    return "test"

if __name__ == "__main__" :
    app.run(debug=True)