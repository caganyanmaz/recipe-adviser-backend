import os
from flask import Flask
from flask_restful import Api, Resource


class Recipe(Resource):
    def get(self, recipe_id):
        return A


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    api = Api(app)


    api.add_resource(Recipe, '/')

    return app


