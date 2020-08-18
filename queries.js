// Mongo Shell
mongo "mongodb+srv://cluster0.xclop.mongodb.net/" --username root




// <!-- Create user collection -->
db.createCollection("customer", {autoIndexId:true})

db.customer.insert({
	'name':'Peter Gan',
	'contactNumber':'97890000',
    'email':'pg1964@gmail.com',
    'password':'polarbear1234'
})

db.customer.insert({
	'name':'Paige Sng',
	'contactNumber':'9910200',
    'email':'pgsng@gmail.com',
    'password':'deathstar'
})

db.customer.insert({
	'name':'Gabriel DeCruz',
	'contactNumber':'91938420',
    'email':'gabrieldc@gmail.com',
    'password':'quackquack'
})


// <!-- Restaurants created -->
db.createCollection("restaurant", {autoIndexId:true})

db.restaurant.insert({
	'name':'Food Alley @ RV',
	'location':'13 River Valley Height, #1-20',
    'contact':'67208930',
    'email':'booking@fa.com',
    'password':'0928346'
})

db.restaurant.insert({
	'name':'HEY Sushi!',
	'location':'Aljunied MRT',
    'contact':'67201245',
    'email':'booking@hey.com',
    'password':'034848'
})

db.restaurant.insert({
	'name':'Jab Theory',
	'location':'Kent Rich Park, #03-9092',
    'contact':'N/A',
    'email':'jabtheory@yeetmail.com',
    'password':'039075'
})

// <!-- Menu Items created for river valley food court -->
db.createCollection("menuItems", {autoIndexId:true})

db.menuItems.insert({
	'name':'MillionDollar Nasi Lemak',
	'shortDes':'Made with golden achovies, secret-marinate chicken, herbal rice and awesome chilli',
})

db.menuItems.insert({
	'name':'Kway Chap',
	'shortDes':'Plain old pork noodle soup with a colloquail sounding name',
})

db.menuItems.insert({
	'name':'Salted Egg Fries',
	'shortDes':'Salty and savoury!',
})

// <!-- amend the db to accomodate menu items -->
db.restaurant.update(
    {
        _id:ObjectId('5f3a283b38a68d1d0d2d0bf9')
    },
    {
            '$set': {
                'menuItems':
                [
                    {
                        '_id':ObjectId('5f3a9c8d2860f9421568db8c'),
                        'name':'MillionDollar Nasi Lemak'
                    }, 
                    {
                        '_id':ObjectId('5f3a9cfc2860f9421568db8d'),
                        'name':'Kway Chap'
                    },
                    {
                        '_id':ObjectId('5f3a9d882860f9421568db8e'),
                        'name':'Salted Egg Fries'
                    } 
                ]
 
        }
    } 
)

// <!-- Menu Items created for Jab Theory food court -->

db.menuItems.insert({
    'name': 'Hokkien Noodles',
    'shortDes': 'A recipe from the Fujian/Hokkien province in China',
})

db.menuItems.insert({
                'name': 'Satay',
                'shortDes': 'Meat on skewers',
            })

db.menuItems.insert({
                'name': 'Ice Kachang',
                'shortDes': 'Shave ice with sweet syrup',
})

// <!-- Menu Items created for HEY Sushi food court -->

db.menuItems.insert({
    'name': 'Raw Sashimi',
    'shortDes': 'Freshest fish used for sashimi',
})

db.menuItems.insert({
                'name': 'Nigiri Rolls',
                'shortDes': 'Something rolled up in seaweed!',
            })

db.menuItems.insert({
                'name': 'Onigiri',
                'shortDes': 'Triangle is the new square. Wrapped in rice!',
})

// Embed Jab Theory Food
db.restaurant.update(
    {
        _id:ObjectId('5f3a283b38a68d1d0d2d0bf9')
    },
    {
            '$set': {
                'menuItems':
                [
                    {
                        '_id':ObjectId('5f3a9c8d2860f9421568db8c'),
                        'name':'MillionDollar Nasi Lemak'
                    }, 
                    {
                        '_id':ObjectId('5f3a9cfc2860f9421568db8d'),
                        'name':'Kway Chap'
                    },
                    {
                        '_id':ObjectId('5f3a9d882860f9421568db8e'),
                        'name':'Salted Egg Fries'
                    } 
                ]
 
        }
    } 
)

// Create Review
db.createCollection("review", {autoIndexId:true})

db.review.insert({
	'title':'Awesome food! Never really tasted something this wonderful!',
	'review':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas molestie nec diam at convallis. Proin augue urna, pharetra eu iaculis sit amet, rhoncus eget augue. Pellentesque volutpat leo at rhoncus auctor. Etiam blandit magna lorem. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. ',
    'rating':10,
    'cost':9,
    'customer':[
        
    ]

})