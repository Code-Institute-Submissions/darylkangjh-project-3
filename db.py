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
@app.route('/all')
def show_reviews():
    all_reviews = db.review.find()

    return render_template('show/all_review.template.html',
                            reviews=all_reviews)

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)