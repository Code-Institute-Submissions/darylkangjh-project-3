from flask import Flask, render_template, request, redirect, url_for
import pymongo
import os
import flask_login
from passlib.hash import pbkdf2_sha256
from dotenv import load_dotenv
from bson.objectid import ObjectId
import datetime

app = Flask(__name__)

load_dotenv()

app.secret_key = os.environ,get('SECRET_KEY')
MONGO_URI=os.environ.get('MONGO_URI'),

# Mongo Client 
client = pymongo.MongoClient(MONGO_URI)
db = client['EatRank']

# Login Manager
login_manager= flask_login.LoginManager()
login_manager.init_app(db)

class User(flask_login.UserMixin):
    pass

def encrypt_password(plaintext):
    return pbkdf2_sha256.hash(plaintext)

def verify_password(plaintext, encrypted):
    return pbkdf2_sha256.verify(plaintext, encrypted)

@login_manager.user_loader
def user_loader(email):

    # attempt to get user
    user_in_db = client[DB_NAME]['customer'].find_one({
        "email":email
    })

    customer = Customer()
    customer.id = customer_in_db['email']

    # if found
    if customer:
        return customer 
    else: 
        return None
 
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

# Show for all customer (admin)
@app.route('/show-customers')
def show_customer():
    all_customer = db.customer.find()

    return render_template('show/all_customer.template.html', 
                    customer = all_customer)

# Customer account and all that she commented on
@app.route('/show-customer-account/<customer_id>')
def show_customer_account(customer_id):

    customer = db.customer.find_one({
        '_id': ObjectId(customer_id),
    })
   
    all_reviews = db.review.find({
        'customer._id':ObjectId(customer_id),
    })
    return render_template('show/one_customer.template.html', customer=customer, review=all_reviews)

# Create a customer account
@app.route('/create-customer')
def create_customers():
    all_customer = db.customer.find()

    return render_template('create/create_customer.template.html', 
                    customer = all_customer)  

@app.route('/create-customer', methods=['POST'])
def process_create_customers():
    
    # Get Information from form 
    name = request.form.get('name')
    contact = request.form.get('contact')
    email = request.form.get('email')
    password = request.form.get('password')

    # Do validation later (focus on functionality first)

    # Insert new customer 
    new_record = {
    'name': name,
    'email': email,
    'contact': contact,
    'password': password,
    }

    db.customer.insert_one(new_record)
    return redirect(url_for('show_customer_account'))  

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

# Review create
@app.route('/create-review')
def create_review():
    all_reviews = db.review.find()

    return render_template('create/create_.template.html', 
                    review = all_reviews)  


@app.route('/create-review', methods=['POST'])
def process_create_reviews():
    
    # Get Information from form 
    title = request.form.get('title')
    review = request.form.get('review')
    ratingFood = request.form.get('ratingFood')
    ratingRes = request.form.get('ratingRes')
    cost = request.form.get('cost')
    restaurantName = request.form.get('restaurantName')

    # Do validation later (focus on functionality first)


    # Get the restaurant id 
    # Insert new restaurant 
    new_review = {
    'title' : title
    'review' : review
    'ratingFood' : ratingFood
    'ratingRes' : ratingRes
    'cost' : cost
    'restaurantName' : restaurantName
    }

    db.restaurant.insert_one(new_record)
    return redirect(url_for('show_restaurants'))  


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)