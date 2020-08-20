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
    'menuItems':[],
    }

    db.restaurant.insert_one(new_record)
    return redirect(url_for('show_restaurants'))  



@app.route('/restuarants/menu/<restaurant_id>')
def show_add_menu_items(restaurant_id):
    restaurant = db.restaurant.find_one({
        '_id':ObjectId(restaurant_id)
    })

    return render_template('create/create_menuItems.template.html', restaurant = restaurant)

@app.route('/restuarants/menu/<restaurant_id>', methods =["POST"])
def add_menu_items(restaurant_id):
    name = request.form.get('item-name')
    shortDes = request.form.get('short-des')

    menuItems ={
        'name':name,
        'shortDes':shortDes
    }

    db.menuItems.insert_one(menuItems)

    # Update the restaurant
    menu_item = db.menuItems.find_one({
        'name':name
    })
    
    db.restaurant.update({
        '_id':ObjectId(restaurant_id)
    },{
            '$push':{
                'menuItems':{
                    'item':menu_item,
                }
            }
        }
    )


    return redirect(url_for('show_restaurants'))



# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)