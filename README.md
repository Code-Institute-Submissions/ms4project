# Hits 'n' Hops

Hits 'n' Hops is a beer store with a memebership option giving users a new exclusive record delivered each month.
The beer store is vast and holds beers form all around the world and records are hand picked by site admin to give members a small insight into our music preferences.

## Purpose

Hits 'n' Hops was built as a way to bring people together through music and beer. Browsing our beer store and finding the perfect IPA or stout to match
whatever songs you fancy. Records are hand selected by site admins carefully to give members a taste of our musical

## Wireframe Mockups

Before starting the project I put together a few wireframe mockups so I had an idea of what I was trying to 
create and what I should include. It also allowed me to see how the features would be scaled and incorporated 
over various device sizes. These were created using [Balsamiq](https://balsamiq.com/ "Balsamiq"):

[Wireframe Mockups](/assets/wireframes/home-pub-quiz.bmpr "Home Pub Quiz")

These wireframe mockups show how I intended the site design and layout to look on various devices, the streamline 
design does not vary too much between device sizes to bring a familiarity to revisiting users. 

## Theme

The deep navy background used throughout the page gives a clear contrast with the white and subtle yellow used 
for the quiz information, questions and answers. This contrast makes the quiz information and questions easy 
for the user to read and understand. Answers change colour to green(correct) and red(incorrect) when selected 
to indicate how well a user has done with each question. 

## UX

The [Materialize CSS](https://materializecss.com/ "Materialize") standard 12 column fluid responsive grid system 
allowed for an easily structured mobile-first design. It also made sure that Home Pub Quiz is responsive over 
varying screen sizes and devices. Images below show how the design and layout scales to suit each device size:

* Mobile Designs: [Mobile Home Page](/assets/img/HPQ-mobile-home.png "Mobile Home Page"), [Mobile Quiz Page](/assets/img/HPQ-mobile-quiz.png "Mobile Quiz Page"), [Mobile Score Page](/assets/img/HPQ-mobile-score.png "Mobile Score Page") 
* Tablet Designs: [Tablet Home Page](/assets/img/HPQ-tablet-home.png "Tablet Home Page"), [Tablet Quiz Page](/assets/img/HPQ-tablet-quiz.png "Tablet Quiz Page"), [Tablet Score Page](/assets/img/HPQ-tablet-score.png "Tablet Score Page")
* Desktop Designs: [Desktop Home Page](/assets/img/HPQ-desktop-home.png "Desktop Home Page"), [Desktop Quiz Page](/assets/img/HPQ-desktop-quiz.png "Desktop Quiz Page"), [Desktop Score Page](/assets/img/HPQ-desktop-score.png "Desktop Score Page")


## Features & Layout

### Home-Landing Page

Welcomes the user to Hits 'n' Hops and asks new users to register and become a member if they wish. The top navbar (dispalyed throughout the site) allows users to navagate to any page on the site
and allows them to search the beer store by name or description. More information about what we do and how we operate is available as you scroll through the home
page, alongside various links to beer store, sign in page, etc.
A footer gives further information about how Hits 'n' Hops operates and shows how to get in contact with our team.

### Beer Store

Our Beer Store contains the entire beer library we have in our database. This page allows users to browse and view key information about each beer before selecting
the for purchase. Three buttons above the beer store library allow users to view beers of specified styles or breweries or sort by price, volume, abv, etc. 

Each Beer is displayed on a card with an image and all relevant information including name, price, style, volume, abv. and rating. Superusers will be able to edit and delete
beers from the library with the click of a button in the form of icons on the bottom right of each card.
The hidden display of the card is shown by clicking the icon top right of the card infromation section and allows the user to view the beer's brewery and decription
A back to top button is provided for users at the bottom right of the page.

Selecting the beer image or name will bring users to the beer detail page.

### Beer Detail Page

When a user selects a beer they are brought to the beer detail page. 
From this page users are able to add the beer to their cart for purchase with a link to the checkout being provided via a success toast. Users can choose to continue shopping
and return to the beer store via the buttton below the beer information.

Superusers can also edit or delete beers from beer store using buttons provided on the right of the screen.

### Cart Page

A table of contents for a user's current cart are found on the cart page. There is a link to checkout following the table.
If the user's cart is currently empty they are invited to head back to the beer store via the button link.

### Checkout Page

When a user is done beer shopping they can head to the checkout page via the navbar link or cart page button. The checkout page provides the user a list of beers in their cart and a form to fill
in their perosnal information including an option to save personal information to user profile to allow for faster checkout next time round.
There is an option to adjust cart which takes back the user Cart Page.
Payment information is processed with Stripe to ensure a secure checkout.

A transparent blue overlay with spinning icon covers page whilst order is processing.
When order is successfully processed the user is transferred to the checkout success page.

### Checkout Success Page

Users are transferred here on completion of purchases. They are greeted with a thank you message and sent a confirmation email. The order details are displayed
in a reciept style to allow users to clearly review orders.

Buttons taking users back to the beer store or their user profile page are provided at the foot of the order.

### User Profile Pages

Whilst a user is signed in they can view their profile page via the navbar link. On the profile page users can edit their delivery details via the form displayed.
Users can also view their order history and can view previous specific orders by selecting the order number from the list.

### Record Collection Page

Users can view our collection of records which are sent to members each month. Each record is displayed in row containing an album artwork image alonside details including title, artist,
genre, record label and year of original release with a description. 

Superusers can edit or delete an record from this page using the icons provided.

### Product Management Pages

These pages are only available to superusers and allow them to add beers or records to the database as well as editing the current library. 
This is achiebed by simply submitting the forms displayed with the required information.

## Future Improvements

### Rate and Comment on Beers
Add comment section on the beer detail page that would allow users to leave their personal views on each beer. alongsode the comments section would be a feature
to allow users to rate beers out of 5, this rating would then be used as part of the average rating displayed in the beer details.
### Listening Parties Add-on
Allow members to arrange virtual listening parties to share new music and beers with fellow users.
### Add forums
Start forums to interact with users and findo out how they think the site can be improved. Discuss potential new beers with users and allow members to have a sneak peek at our next
record of the month.

## Testing

All basic style and layout testing for each device size during development was done using Chrome's developer tools while previewing the site.

To validate my HTML I used [W3C HTML Validator](https://validator.w3.org/ "W3C HTML Validator").

To validate my CSS I used [W3C CSS Validator](https://jigsaw.w3.org/css-validator/ "W3C CSS Validator").

I passed my JS through [JSHint](https://jshint.com/ "JSHint") linter without any issues.

Stripe payment handling for orders tested before deployment. 

## Deployment

Site was deployed using [Heroku](https://www.heroku.com/ "Heroku"):

1. Log in to Heroku Dashboard.
2. Click on New dropdown menu on the right a choose Create New App.
3. Complete form then submit to create app.
4. Select App(for-the-record) from Dashboard.
5. Click on the Settings tab then find Reveal Config Vars in the Config Vars section.
6. Add Config Vars.
7. Click on the Deploy tab then Click on GitHub in the Deployment Method section.
8. Then Connect app to [GitHub Repository](https://github.com/aralston3592/ms4-project/ "GitHub Repository")
9. Deploy the app via Heroku using the Master Branch via the Manual Deploy Section.
10. Once completed Click View App button to begin using the app.

## Technology Used

* Wireframes: [Balsamiq](https://balsamiq.com/ "Balsamiq")
* Programming Languages: HTML, CSS, Javascript, Python
* Fonts & Icons: [Google Fonts](https://fonts.google.com/ "Google Fonts"), [Materialize CSS](https://materializecss.com/ "Materialize"), [Share This](https://platform.sharethis.com/ "Share This Platform"). 
* Javascript: [JQuery](https://jquery.com/ "JQuery")
* Responsive Design: [Materialize CSS](https://materializecss.com/ "Materialize")
* IDE: [Gitpod](https://gitpod.io/ "GitPod")
* Version Control: [Git](https://git-scm.com/ "Git")
* Repository Host/Deployment: [Heroku](https://heroku.com/ "Heroku")