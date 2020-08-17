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

<!-- Menu Items created -->
db.createCollection("menuItems", {autoIndexId:true})

db.restaurant.insert({
	'name':'MillionDollar Nasi Lemak',
	'shortDes':'Made with golden achovies, secret-marinate chicken, herbal rice and awesome chilli',
})