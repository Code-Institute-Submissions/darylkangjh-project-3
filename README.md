<!-- Create user collection -->
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


<!-- Restaurants created -->
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

<!-- Menu Items created -->
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

<!-- amend the db to accomodate menu items -->

db.amenities.update({_id:ObjectId('5d35fb429957d32e05ca955e')}, {
 $set: {
  'description':'Black box'
 }
 }
);


