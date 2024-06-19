import os
import db
from flask import Flask
from flask_restful import Api, Resource


class Recipe(Resource):
    def get(self, id):
        return db.get_value({"recipe": [{"id": id}]})

class Ingredients(Resource): 
    def get(self, recipe_id):
        return db.get_values({"ingredient_recipe": [{"recipe_id": recipe_id}]})


class Instructions(Resource):
    def get(self, recipe_id):
        return db.get_instructions_of_recipe(recipe_id)


class Tag(Resource):
    def get(self, id):
        return db.get_value({"tag": [{"id": id}]})


def create_app(test_config=None):
    db.init()
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    api = Api(app)


    api.add_resource(Recipe, "/recipe/<int:id>")
    api.add_resource(Ingredient, "/ingredients/<int:recipe_id>")
    api.add_resource(Instruction, "/instructions/<int:recipe_id>")
    api.add_resource(Tag, "/tag/<int:recipe_id>")

    return app


