from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

class Recipe:
    def __init__ (self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.date_made = data['date_made']
        self.under_thirty = data['under_thirty']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.user = {}
    
    @classmethod
    def save_recipe(cls, data):
        query = "INSERT INTO recipes (user_id, name, description, instruction, date_made, under_thirty, created_at, updated_at) VALUES (%(user_id)s, %(name)s, %(description)s, %(instruction)s, %(date_made)s, %(under_thirty)s, NOW(), NOW());"
        return connectToMySQL("recipes_schema").query_db(query, data)

    @classmethod
    def one_recipe(cls, data):
        query = "SELECT * FROM recipes LEFT JOIN users ON users.id = recipes.user_id WHERE recipes.id = %(id)s;"
        results = connectToMySQL('recipes_schema').query_db(query, data)

        this_recipe = Recipe(results[0])

        user_data = {
            "id" : results[0]['users.id'],
            "first_name" : results[0]['first_name'],
            "last_name" : results[0]['last_name'],
            "email" : results[0]['email'],
            "password" : results[0]['password'],
            "created_at" : results[0]['users.created_at'],
            "updated_at" : results[0]['users.updated_at']
        }
        
        this_recipe.user = user.User(user_data)

        return this_recipe

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL('recipes_schema').query_db(query, data)

    @classmethod
    def update_recipe(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instruction = %(instruction)s, date_made = %(date_made)s, under_thirty = %(under_thirty)s, updated_at = NOW() WHERE id = %(id)s;"
        connectToMySQL('recipes_schema').query_db(query, data)


    @staticmethod
    def validate_recipe(recipe):
        is_valid = True

        if len(recipe['name']) < 3:
            flash(u"Recipe Name must be at least 3 characters long", "recipes")
            is_valid = False

        if len(recipe['description']) < 3:
            flash(u"Recipe Description must be at least 3 characters long", "recipes")
            is_valid = False

        if len(recipe['instruction']) < 3:
            flash(u"Recipe Instructions must be at least 3 characters long", "recipes")
            is_valid = False

        if not recipe['date_made']:
            flash(u"Please provide a date for this recipe", "recipes")
            is_valid = False

        return is_valid