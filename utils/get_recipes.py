from get_database import get_database

dbname = get_database()
collection_name = dbname["recipes"]


def get_recipes():
    recipes = [recipe for recipe in collection_name.find({})]

    return recipes
