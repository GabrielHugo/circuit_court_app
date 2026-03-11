import os

from flask import Flask, render_template

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from dotenv import load_dotenv
load_dotenv()

CONNECTION_URI = os.getenv("URI")
client = MongoClient(CONNECTION_URI, server_api=ServerApi('1'))

db = client["circuit_court_db"]
products = db["products"]
app = Flask(__name__)

@app.route("/")
def home() :
    return render_template("home.html")

@app.route("/products", methods=["GET"])
def products() :
    products_list = db["products"].find()
    return render_template("products.html", products=products_list)

@app.route("/stocks", methods=["GET"])
def stocks() :
    stocks_list = db["products"].find()
    return render_template("stocks.html", products=stocks_list)

@app.route("/basket")
def basket() :
    return render_template("basket.html")

if __name__ == "__main__" :
    app.run(debug=True)
