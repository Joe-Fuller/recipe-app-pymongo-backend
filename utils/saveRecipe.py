from getDatabase import get_database

dbname = get_database()
collection_name = dbname["recipes"]


def save_recipe(recipe):
    collection_name.insert_one(recipe)
