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


app.secret_key = os.environ.get('SECRET_KEY')
MONGO_URI=os.environ.get('MONGO_URI'),
CLOUD_NAME = os.environ.get('CLOUD_NAME')
UPLOAD_PRESET = os.environ.get('UPLOAD_PRESET')

# Mongo Client 
client = pymongo.MongoClient(MONGO_URI)
db = client['EatRank']

class User(flask_login.UserMixin):
    pass

login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def user_loader(email):
    customer = db.customer.find_one({
        'email': email
    })

    if customer:
        user_object = User()
        user_object.account_id=customer['_id']
        user_object.id = customer['email']
        user_object.name = customer['name']
        return user_object
    
    else:
        return None 
        #please report error here later

# Home page ( this page will be static and show the various routes)
@app.route('/')
def home():
    return render_template('home.template.html')


# Customer Login & Logout Below
@app.route('/login')
def login():
    return render_template('login.template.html')

@app.route('/login', methods=['POST'])
def process_login():
    email = request.form.get('email')
    password = request.form.get('password')

    customer = db.customer.find_one({
        'email' : email
    })

    if customer and customer["password"] == password:
        user_object = User()
        user_object.id = customer['email']
        user_object.name = customer['name']
        flask_login.login_user(user_object)
        return redirect(url_for('show_reviews'))

    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return redirect(url_for('login'))

@app.route('/secret')
@flask_login.login_required
def secret():
        return "Secret Area"

# Show for all customer (admin) This is not meant for the site and should be kept "secret"
@app.route('/show-customers')
def show_customer():
    all_customer = db.customer.find()

    return render_template('show/all_customer.template.html', 
                    customer = all_customer)

# Customer account and all that he/she commented on
@app.route('/show-customer-account/<customer_id>')
def show_customer_account(customer_id):

    all_reviews = db.review.find({
        'customer._id': ObjectId(customer_id),
    })

    # print(flask_login.current_user.is_authenticated)
    return render_template('show/one_customer.template.html',review=all_reviews)


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
    'password': password
    }

    db.customer.insert_one(new_record)

    return redirect(url_for("login"))

# Restaurants below
# Show all available restaurants and the link to their page
@app.route('/show-restaurants')
def search():
    
    required_restaurant_name = request.args.get('restaurant_name')

    criteria = {}

    if required_restaurant_name:
        criteria['name'] = {
            '$regex': required_restaurant_name,
            '$options':'i' 
        }
 
    all_restaurants = db.restaurant.find(criteria)
    
    return render_template('show/all_restaurant.template.html', 
                           restaurant = all_restaurants)

# Show one restaurant after selecting their ID, (To display Menu and details for people to consider)
@app.route('/show-restaurants/<restaurant_id>')
def show_one_restaurant(restaurant_id):
    one_restaurant=db.restaurant.find_one({
        '_id':ObjectId(restaurant_id)
    })

    menu_item = db.menu_item.find()

    return render_template('show/one_restaurant.template.html', restaurant=one_restaurant, menu=menu_item )

# Create Restaurant (route)
@app.route('/create-restaurant')
def create_restaurant():
    return render_template('create/create_restaurant.template.html', cloud_name=CLOUD_NAME , upload_preset = UPLOAD_PRESET )

# Create Restaurant (get details from form to insert to DB)
@app.route('/create-restaurant', methods=['POST'])
def process_create_reviews():
    
    # Get Information from form 
    name = request.form.get('name')
    location = request.form.get('location')
    contact = request.form.get('contact')
    email = request.form.get('email')
    uploadURL = request.form.get('uploaded-file-url')
    assetID = request.form.get('asset-id')


    # Do validation later (focus on functionality first)

    # Insert new restaurant 
    new_record = {
    'name': name,
    'location': location,
    'contact': contact,
    'email': email,
    'menuItems':[],
    'uploadURL':uploadURL,
    'assetID':assetID
    }

    db.restaurant.insert_one(new_record)
    return redirect(url_for('search'))

@app.route('/restuarants/menu/<restaurant_id>')
def show_add_menu_items(restaurant_id):
    restaurant = db.restaurant.find_one({
        '_id':ObjectId(restaurant_id)
    })

    return render_template('create/create_menuItems.template.html', 
                           restaurant = restaurant)

@app.route('/restuarants/menu/<restaurant_id>', methods =["POST"])
def add_menu_items(restaurant_id):

    name = request.form.get('item-name')
    shortDes = request.form.get('short-des')

    menuItems ={
        'name':name,
        'shortDes':shortDes
    }

    db.menuItems.insert_one(menuItems)

    db.restaurant.update_one({
        '_id':ObjectId(restaurant_id)
    },{
            '$push':{
                'menuItems':{
                    'item':menuItems,
                    'shortDes':shortDes
                }
            }
       }
    )
    return redirect(url_for('search'))



#WIP NOW!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DON"T CHANGE

# Get data from form 
@app.route('/amend-restaurant/<restaurant_id>')
def show_update_restaurant(restaurant_id):
    restaurant = db.restaurant.find_one({
        '_id': ObjectId(restaurant_id)
    })

    return render_template('edit/edit_restaurant.template.html', restaurant=restaurant, cloud_name=CLOUD_NAME , upload_preset = UPLOAD_PRESET  )

# Edit restaurant 
@app.route('/amend-restaurant/<restaurant_id>', methods=["POST"])
def process_show_update_restaurant(restaurant_id):

    name = request.form.get('name')
    location = request.form.get('location')
    contact = request.form.get('contact')
    email = request.form.get('email')
    uploadURL = request.form.get('uploaded-file-url')
    assetID = request.form.get('asset-id')

    db.restaurant.update_one({
        '_id': ObjectId(restaurant_id)
    },{
        '$set': {
            'name': name,
            'location': location,
            'contact': contact,
            'email': email,
            'menuItems':[],
            'uploadURL':uploadURL,
            'assetID':assetID
        }
    })
    return redirect(url_for('search'))

# Edit restaurant end

# Reviews
# Reviews (Show all reviews// user can read reviews similar to reddit post)
@app.route('/review')
def show_reviews():
    all_reviews = db.review.find()

    return render_template('show/all_review.template.html', review = all_reviews)

# Review create
@app.route('/create-review')
def create_review():
    all_reviews = db.review.find()
    all_restaurants = db.restaurant.find()
    return render_template('create/create_review.template.html', 
                           review = all_reviews, restaurant = all_restaurants)  


#get data from form
@app.route('/create-review', methods=['POST'])
@flask_login.login_required
def process_create_review():

    # Get Information from form 
    title = request.form.get('title')
    review = request.form.get('review')
    ratingFood = request.form.get('ratingFood')
    ratingRes = request.form.get('ratingRes')
    cost = request.form.get('cost')
    customer = flask_login.current_user.account_id
    name = flask_login.current_user.name
    # need to make sure it is a object id (save it in a dictionary)
    restaurant = request.form.get('restaurants')

    resid = ObjectId(restaurant)
    # query and populate into review! 
    restaurant_name = db.restaurant.find_one(resid)



    # Do validation later (focus on functionality first)

    # Insert new review 
    new_review = {
        'title': title,
        'review': review,
        'ratingFood': ratingFood,
        'ratingRes': ratingRes,
        'cost': cost,
        'customer': {
            '_id':ObjectId(customer),
            'name':name
        },
        'restaurant':{
            '_id':resid,
            'name':restaurant_name["name"]
        }
    }

    db.review.insert_one(new_review)
    return redirect(url_for('show_reviews'))

# Review edit 
@app.route('/amend-review/<review_id>')
def show_update_review(review_id):
    review = db.review.find_one({
        '_id': ObjectId(review_id)
    })

    return render_template('edit/edit_review.template.html', review=review)


# Actual edit (Methods = post)
@app.route('/amend-review/<review_id>', methods=["POST"])
def process_show_update_review(review_id):
    title = request.form.get('title')
    review = request.form.get('review')
    ratingFood = request.form.get('ratingFood')
    ratingRes = request.form.get('ratingRes')
    cost = request.form.get('cost')
    restaurantName = request.form.get('restaurantName')

    db.review.update_one({
        '_id': ObjectId(review_id)
    },{
        '$set': {
            'title': title,
            'review': review,
            'ratingFood': ratingFood,
            'ratingRes': ratingRes,
            'cost': cost,
            'restaurantName': restaurantName
        }
    })
    return redirect(url_for('show_reviews'))

@app.route('/delete-review/<review_id>')
def show_delete_review(review_id):
    review = db.review.find_one({
        '_id':ObjectId(review_id)
    })
    return render_template('edit/delete_review.template.html', review = review)

@app.route('/delete-review/<review_id>', methods=["POST"])
def process_delete_review(review_id):
    db.review.remove({
        '_id':ObjectId(review_id)
    })
    return redirect(url_for('show_reviews'))






# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)