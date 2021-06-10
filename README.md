A Tavola is the project submission for the Data Centric Development Milestone Project By Code Institute, it consists in a recipes website with an interactive design that allows the registered user to upload their recipes or simply search for recipes through the database. 

## Table of contents

1. [User Experience](#user-experience)
   - [User Stories](#stories)
   - [The 5 Planes](#planes)
   - [Wireframes](#wireframes)
2. [Database Schema](#dbschema)
3. [Features](#features)
4. [Technologies Used](#technologies)
5. [Testing](#testing)
6. [Database Creation](#database)
7. [Deployment](#deployment)
8. [Resources](#resources)
9. [Credits](#credits)
    - [Media](#media)
    - [Code Snippets](#code)
    - [Acknowledgements](#acknowledgements)

## **User Experience (UX)** <a name="user-experience"></a>
The main focus of A Tavola is to have a clean and intuitive website on the front-end, with a full user access to the C.R.U.D. functionality (Create, Read, Update and Delete) simply navigating throught the pages. In addition to that, the back-end needs a good solid structure to make the search of the recipes and the navigation easier for the user.

### **User Stories** <a name="stories"></a>

1. _As a_ **first time visitor**, _I need to_ **understand the purpose of the site**, _in order to_ **consider exploring the site further**.

2. _As a_ **first time visitor**, _I need to_ **quickly and easily register on the site**,  _in order to_ **fully interact with the site**.
   
3. _As a_ **first time visitor**, _I need to_ **easily access the recipe collection**, _in order to_ **search for a recipe worth making**.

4. _As a_ **returning user**, _I need_ **an interface where I can upload and save my recipes**, _in order to_ **share my favourite recipes with other site users**.

5. _As a_ **returning user**, _I need to_ **have the ability to edit or delete a recipe I have uploaded** _in order to_ **make changes to, or remove an out of date or incorrect recipe**.

6. _As a _ **site owner**, _I need to_ **ensure some basic access control to edit and delete functionality**, _in order to_ **prevent unauthorised editing or deletion of user uploaded data**.

7.  _As a _ **site owner**, _I need to_ **have a unique feature which generates some competition between users**, _in order to_ **encourage users to post new recipes**

### **The 5 Planes of UX** <a name="planes"></a>

#### **Strategy**  
A Tavola wants to provide a reliable source of "easy to do at home" recipes, a cookbook for everyone mainly made from the users themselves thanks to the C.R.U.D. functionality.

#### **Scope** 
In order to reach a well functioning C.R.U.D. , it is important to have a good communication betweek the MongoDB Atlas cloud database and the website, but it has to be easy also for the user to understand how to access to the C.R.U.D. interactions.

##### Functional Requirements

##### Content Requirements

#### **Structure**  

#### **Skeleton** 

#### Wireframes <a name="wireframes"></a>
The original Wireframes display the ideal Homepage, Recipe Page and Registration Page:

**Homepage**
![Home Page](https://github.com/ClaudiaLie/MS_3_CookBook_Website/blob/master/readme_img/Homepage.png?raw=true)

**Recipe Page**
![Recipe Page](https://github.com/ClaudiaLie/MS_3_CookBook_Website/blob/master/readme_img/Recipe_page.png?raw=true) 

**Registration Page**
![Register page](https://github.com/ClaudiaLie/MS_3_CookBook_Website/blob/master/readme_img/Register.png?raw=true) 

#### **Surface**

## **Database Schema** <a name="dbschema"></a>
![DB Schema](https://github.com/ClaudiaLie/MS_3_CookBook_Website/blob/master/readme_img/Database_schema.jpeg?raw=true)  

## **Features** <a name="features"></a>

## **Technologies Used** <a name="technologies"></a> 

## **Testing** <a name="testing"></a>

## **Resources** <a name="resources"></a>

## **Credits** <a name="credits"></a>

### **Acknowledgements** <a name="acknowledgements"></a>

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidently make it public then you can create a new one with _Regenerate API Key_.