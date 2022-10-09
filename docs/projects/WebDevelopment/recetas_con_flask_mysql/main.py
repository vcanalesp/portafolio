from Python_Belt.recipes.flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt

from Python_Belt.recipes.flask_app.models.user import User
from flask_app import app

if __name__ == '__main__':
    query = "SELECT * FROM users WHERE email = 'hola'"
    results = connectToMySQL('recipes_schema').query_db(query)
    #data = {'email':'valeska.canales.p@gmail.com'}
    #query = "SELECT * FROM users WHERE email = %(email)s;"
    #result = connectToMySQL('recipes_schema').query_db(query, data)
    #user = User.one_user_all_recipes()


    pass