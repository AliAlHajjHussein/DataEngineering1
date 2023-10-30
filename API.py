from flask import Flask, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
# Configure the Flask app with the MongoDB connection details
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydatabase'
mongo = PyMongo(app)

# Create an API route to retrieve the data from the MongoDB collection
@app.route('/articles', methods=['GET'])
def get_articles():
    collection = mongo.db.articles
    articles = list(collection.find({}, {'_id': 0}))
    return jsonify(articles)

if __name__ == '__main__':
    app.run()