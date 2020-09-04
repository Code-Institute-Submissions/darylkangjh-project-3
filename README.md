# EatRank | We can't get enough of reviews 

## Introduction 
EatRank is a crowd-source food review website that selects genuine customers from a community of food enthusiast to help review various restaurants in Singapore. The platform aims to moderate between the consumer’s need for credible information while balancing the anonymity of the internet which most famous reviews platform fail to moderate.
At this current stage, the idea for the platform is to have EatRank employees add partner restaurants into our platform while reviewers are verified offline via a 1-day training programme on how to utilise the platform. 
The platform aims to generate revenue from a small platform fee from restaurants and advertisements by “bumping” listings to the top of the page. 

## Demo
### You may test the current working page at: 
    https://dkjh-eatrank-project3.herokuapp.com/

### To log-in, please use: 
    Email: pg1964@gmail.com
    Password: polarbear1234

## UI/UX 


### Strategy

#### __Owner Goals__
The site owner aims to use the platform to on-board partner restaurants and encourage more user sign ups. To that end, the initial phase of EatRank will allow verified users to create restaurants themselves by adding in places they have visited and wish to list on EatRank. This is to prove that the concept works and gather initial traffic to the site with an adequate number of restaurant listed.
However, this feature will be temporary and closely monitored by the Team to ensure there is no exploitation of this feature. In future, restaurants can only be added by EatRank staff.

#### __User Goals__

##### Scope 
__App features for members of the public:__
1.	A page to show all restaurants with an option to see each individual restaurant’s review. 
2.	A page to browse all reviews in the EatRank database
3.	A page to login

__App features for EatRank Community Members:__ 
1.	Log-in page 
2.	Individual review page to create/update/delete reviews made by the community member 
3.	Restaurant page to create/update/delete restaurants. 

##### User Story
For the public, they may browse (or search) for the restaurant they intend to patronise and read up on the reviews before heading down. This is done primarily on the “Restaurants” page where they may click on the review button beneath each restaurant to read the reviews.

For the public who like to read reviews casually, the “Review” page offers all the reviews, the reviewer, the rating as well as the restaurant name. This is designed for members of the public to browse and try out new places with interesting reviews. 

For community members, after logging in, they may edit their reviews by clicking on their name on the “Review” page which displays all the reviews within the EatRank database. 

Community members (upon logging in) may delete, edit or create new restaurants they visited. As mentioned in the introduction, this function is temporary.

##### Unavailable features to be implemented soon
1.	__Hashing of password.__ Currently, passwords are stored as a string in MongoDB. This feature will be done before going live. 
2.	__User/Password validation.__ Currently, there is no restrictions/limit to what a new community member can input to create an account. Technically, a new user may leave all the fields empty to sign up for EatRank. This shouldn’t be the case. For future development, validation will be included to ensure such discrepancies do not occur. 
3.	__User edit & profile picture page.__ Customisation of a user profile is a good feature to increase a community user’s ownership and commitment to the platform. Future development will include this feature where any logging in will be able to add a profile picture, a short-description and the date they joined EatRank. 
4.	__Lack of date for each review.__ This is an error discovered before submission. Date & timestamp should have been included for each review.
5.	__Bootstrap -md mosaic template error.__ One bug found during testing was the lack of responsiveness for -md for the mosaic function on the “Review” page displaying all reviews. Further investigation is warranted. 
6.	__Refined restaurant search & tag.__ One feature that was suggested but lacked the time to implement was a more refined search for restaurants. Future updates will include a “#” function for each restaurant so community users may create or follow tag trends and display those trends to the public. Restaurant may also be segmented base on their cuisine type (e.g. Japanese, Local, Fusion, Fine-Dining…) 
7.	__Footer sitemap.__ UX wise, a site map for the footer will be included in future updates. 
