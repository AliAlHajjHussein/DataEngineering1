from flask import Flask, render_template, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["articles"]
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/data')
def get_data():
    # Retrieve data from MongoDB
    data = list(collection.find())

    # Return the data as JSON
    return jsonify(data)

