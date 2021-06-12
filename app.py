import os
from flask import (Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# Index page


@app.route("/")
@app.route("/recipes")
def recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({'$text': {'$search': query}}))
    return render_template("recipes.html", recipes=recipes)


# Registration page


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email").lower(),
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# Login Page


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure that the hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exists
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    return redirect(url_for("recipes"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Add Recipes


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    # called from the user with "Add Recipe" on the menu
    if request.method == "POST":

        recipe = {
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_steps": request.form.get("recipe_steps"),
            "recipe_allergen": request.form.getlist("recipe_allergen"),
            "recipe_category": request.form.getlist("recipe_category"),
            "recipe_img": request.form.get("recipe_img"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Added")
        return redirect(url_for("recipes"))

    allergens = mongo.db.allergens.find().sort("recipe_allergen", 1)
    ingredients = mongo.db.ingredients.find().sort("recipe_ingredients", 1)
    return render_template("add_recipe.html", allergens=allergens, ingredients=ingredients)

# Edit Recipe

@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":

        submit = {
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_steps": request.form.get("recipe_steps"),
            "recipe_allergen": request.form.getlist("recipe_allergen"),
            "recipe_category": request.form.get("recipe_category"),
            "recipe_img": request.form.get("recipe_img"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Updated")
        return redirect(url_for("recipes"))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    ingredients = mongo.db.ingredients.find().sort("recipe_ingredients", 1)
    return render_template("edit_recipe.html", recipe=recipe, ingredients=ingredients)

# Delete Recipe

@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Deleted")
    return redirect(url_for("recipes"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(os.environ.get("PORT")),
    debug=True)
