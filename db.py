from flask import Flask, render_template, request, redirect, url_for
import pymongo
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

MONGO_URI=os.environ.get('MONGO_URI'),

# Mongo Client 
client = pymongo.MongoClient(MONGO_URI)
db = client['EatRank']

# Routes Below 
@app.route('/')
def show_reviews():
    all_reviews = db.review.find()

    return render_template('show/all_review.template.html', 
                    review = all_reviews)

@app.route('/show-restaurants')
def show_restaurants():
    all_restaurants = db.restaurant.find()

    return render_template('show/all_restaurant.template.html', 
                    restaurant = all_restaurants)

@app.route('/create-review')
def create_reviews():
    all_reviews = db.review.find()

    return render_template('show/all_review.template.html', 
                    review = all_reviews)  

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)