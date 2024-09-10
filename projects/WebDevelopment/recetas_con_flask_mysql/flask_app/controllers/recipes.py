from flask import render_template, request, redirect, flash, session
from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

@app.route('/recipes/new')
def create_recipe():
    if 'user_id' not in session:
        flash(u"You must be logged in to view the dashboard", "login")
        return redirect('/')

    user = User.one_user_all_recipes()

    return render_template("new_recipe.html", user = user)

@app.route('/recipes/submit', methods=['POST'])
def submit_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')

    data = {
        "user_id" : session['user_id'],
        "name" : request.form['name'],
        "description" : request.form['description'],
        "instruction" : request.form['instruction'],
        "date_made" : request.form['date_made'],
        "under_thirty" : request.form['under_thirty'],
    }

    Recipe.save_recipe(data)
    return redirect('/dashboard')

@app.route('/recipes/<int:id>')
def one_recipe(id):
    if 'user_id' not in session:
        flash(u"You must be logged in to view the dashboard", "login")
        return redirect('/')

    data = {
        'id' : id
    }

    recipe = Recipe.one_recipe(data)
    return render_template("onerecipe.html", recipe = recipe)

@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    if 'user_id' not in session:
        flash(u"You must be logged in to edit recipes", "login")
        return redirect('/')

    data = {
        'id' : id
    }

    recipe = Recipe.one_recipe(data)
    if recipe.user_id != session['user_id']:
        return redirect('/dashboard')
    
    return render_template("edit_recipe.html", recipe = recipe)

@app.route('/recipes/edit/<int:id>/update', methods=['POST'])
def update_recipe(id):
    print(id)
    if not Recipe.validate_recipe(request.form):
        return redirect(f"/recipes/edit/{id}")

    data = {
        'id' : id,
        'name' : request.form['name'],
        'description' : request.form['description'],
        'instruction' : request.form['instruction'],
        'date_made' : request.form['date_made'],
        'under_thirty' : request.form['under_thirty']
    }

    Recipe.update_recipe(data)
    print("*" * 10 + "Update Successful" + "*" * 10)
    return redirect('/dashboard')

@app.route('/recipes/delete/<int:id>')
def destroy(id):
    data = {
        'id' : id
    }
    Recipe.delete(data)
    return redirect('/dashboard')
