from flask import Flask, render_template, request, redirect, url_for
import pymongo
import os
from dotenv import load_dotenv
from bson.objectid import ObjectId
import datetime

app = Flask(__name__)

load_dotenv()

MONGO_URI=os.environ.get('MONGO_URI'),

# Mongo Client 
client = pymongo.MongoClient(MONGO_URI)
db = client['EatRank']

# SHOW Routes Below 
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

# CREATE Routes Below 
@app.route('/create-restaurant')
def create_reviews():
    all_reviews = db.review.find()

    return render_template('create/create_restaurant.template.html', 
                    review = all_reviews)  

@app.route('/create-restaurant', methods=['POST'])
def process_create_reviews():
    
    # Get Information from form 
    name = request.form.get('name')
    location = request.form.get('location')
    contact = request.form.get('contact')
    email = request.form.get('email')

    # Do validation later (focus on functionality first)

    # Insert new restaurant 
    new_record = {
    'name': name,
    'location': location,
    'contact': contact,
    'email': email,
    }

    db.restaurant.insert_one(new_record)
    return redirect(url_for('show_restaurants'))  
    


@app.route('/create-menu/update/<restaurant_id>')
def show_reviews(restaurant_id):
    menu = db.restaurant.find_one({
        '_id':ObjectId(restaurant_id)
    })

    
    return render_template('show/all_review.template.html', 
                    review = all_reviews)

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)