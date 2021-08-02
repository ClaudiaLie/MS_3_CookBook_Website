![A Tavola](/workspace/MS_3_CookBook_Website/readme_img/a_tavola_responsive.png?raw=true)

A Tavola is the project submission for the Data Centric Development Milestone Project By Code Institute, it consists in a recipes website with an interactive design that allows the registered user to upload their recipes or simply search for recipes through the database. 

## Table of contents

1. [User Experience](#user-experience)
   - [User Stories](#stories)
   - [The 5 Planes](#planes)
   - [Wireframes](#wireframes)
2. [Database Schema](#dbschema)
3. [Technologies Used](#technologies)
4. [Testing](#testing)
5. [Deployment](#deployment)
6. [Resources](#resources)
7. [Credits](#credits)
    - [Code Snippets](#code)
    - [Acknowledgements](#acknowledgements)

## **User Experience (UX)** <a name="user-experience"></a>

The main focus of A Tavola is to have a clean and intuitive website on the front-end, with a full user access to the C.R.U.D. functionality (Create, Read, Update and Delete) simply navigating throught the pages. In addition to that, the back-end needs a good solid structure to make the search of the recipes and the navigation easier for the user.

### **User Stories** <a name="stories"></a>

1. _As a_ **first time visitor**, _I need to_ **understand the purpose of the site**, _in order to_ **consider exploring the site further**.

2. _As a_ **first time visitor**, _I need to_ **quickly and easily register on the site**,  _in order to_ **fully interact with the site**.
   
3. _As a_ **first time visitor**, _I need to_ **easily access the recipe collection**, _in order to_ **search for a recipe worth making**.

4. _As a_ **returning user**, _I need to_ **have the ability to edit or delete a recipe I have uploaded** _in order to_ **make changes to, or remove an out of date or incorrect recipe**.

6. _As a_ **site owner**, _I need to_ **ensure some basic access control to edit and delete functionality**, _in order to_ **prevent unauthorised editing or deletion of user uploaded data**.

### **The 5 Planes of UX** <a name="planes"></a>

#### **Strategy**  

A Tavola wants to provide a reliable source of "easy to do at home" recipes, a cookbook for everyone mainly made from the users themselves thanks to the C.R.U.D. functionality.

#### **Scope** 

In order to reach a well functioning C.R.U.D. , it is important to have a good communication betweek the MongoDB Atlas cloud database and the website, but it has to be easy also for the user to understand how to access to the C.R.U.D. interactions.

#### **Structure**  

A Tavola website has a very simple structure. 
The landing page is the "Cookbook", the collection of recipes in the database.
Depending on the authentication of the user, the main navbar allows to navigate through different sections of the website, in order to give to only registered users a full access to the website.

#### **Skeleton** 

If the user is not logged in, the navbar displays three pages: 
- **Cookbook** the main landing page, it has a search bar on the top of the page and displays all the recipes contained into the database;
- **Register** allows through a form to register to the website;
- **Log In** a form for users already registered who want to simply log in.

If the user is logged in, the navbar will display some additional options:
- **Add Recipe** only the users will be able to contribute to the addition of recipes to the website;
- **Recipe Edit/Delete** each user will be able to see on their recipe card an edit or delete button, to menage their entries.
- **Log Out** a direct link to the log out.

#### **Wireframes** <a name="wireframes"></a>

The original Wireframes display the ideal Homepage, Recipe Page and Registration Page, definitely a goal for future additions to this project:

**Homepage**

![Home Page](https://github.com/ClaudiaLie/MS_3_CookBook_Website/blob/master/readme_img/Homepage.png?raw=true)

**Recipe Page**

![Recipe Page](https://github.com/ClaudiaLie/MS_3_CookBook_Website/blob/master/readme_img/Recipe_page.png?raw=true) 

**Registration Page**

![Register page](https://github.com/ClaudiaLie/MS_3_CookBook_Website/blob/master/readme_img/Register.png?raw=true) 

#### **Surface**
My vision for A Tavola is an open family cookbook on a kitchen table, and I wanted to resemble through the color scheme the feeling of a warm wood table: 

![Palette](https://github.com/ClaudiaLie/MS_3_CookBook_Website/blob/master/readme_img/Palette.png?raw=true)

**Typography**
The font for the logo follows the same idea of reading a family cookbook, handwritten by each member of the family during the years. After searching through Google Fonts, I have found the perfect combination with readability and style:

![Font Logo](https://github.com/ClaudiaLie/MS_3_CookBook_Website/blob/master/readme_img/Logo_font.png?raw=true)

## **Database Schema** <a name="dbschema"></a>

For the data storage, the website relies on MongoDB Atlas, a fully-managed cloud database.

The schema for A Tavola considers the option of different relationships between the data (one-to-many and many-to-many) but since the website has been build with a more basic structure it wasn't necessary to go in depth with that structure:

![DB Schema](https://github.com/ClaudiaLie/MS_3_CookBook_Website/blob/master/readme_img/Database_schema.jpeg?raw=true)  

## **Technologies Used** <a name="technologies"></a> 

**Core Coding**

- HTML5
- CSS3
- Python

**Integrations**

- Flask
- Jinja
- Materialize CSS
- Font Awesome
- Google Fonts
- JQuery

**Database Management**

- MongoDB Atlas

**Version Control, Storage and Hosting**

- Gitpod
- Github
- Heroku

## **Testing** <a name="testing"></a>

- For python code testing I have been using [pep8](http://pep8online.com/)
- For HTML validation I have used [validatorW3](https://validator.w3.org/#validate_by_input)
- For CSS validation I have used [jigsaw.W3](https://jigsaw.w3.org/css-validator/)
- For responsiveness testing I have used Google DevTools

**Deployment** <a name="deployement"></a>

This is a full-stack website hosted by Heroku:
- Log In to Heroku.com
- From the Dashboard, select "New" on the top-right of the page and then select "Create new app"
- Choose an app name
- Select the closest region to you
- Click "Create app"

**Heroku Deployment**
- In the "Deployment Method" section select Github and connect your GitHub
- Search for the Repository associated with the Heroku
- Click "Connect"
- Remember to enable the automatic deployment, selecting the Heroku "Deploy" tab and "Automatic Deploys"

## **Resources** <a name="resources"></a>
Some very important resources helped to create this project:
- Code Institute mini-project material
- StackOverFlow
- W3Schools
- [Am I responsive?](http://ami.responsivedesign.is/)
- [Dreams Time stock photos](https://www.dreamstime.com/)
- [Color Hex](https://www.color-hex.com/)
- [Materialize](https://materializecss.com/)
- [Giallo Zafferano](https://www.giallozafferano.com/)
- Google Fonts

## **Credits** <a name="credits"></a>
I have looked for suggestions on the README.md structure from another student beautiful project: [GazzaJ](https://github.com/GazzaJ/CI-MS3-W3Recipes)
