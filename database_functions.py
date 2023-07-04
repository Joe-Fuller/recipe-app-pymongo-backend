from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values(".env")


def get_database():
    mongodb_client = MongoClient(config["ATLAS_URI"])

    return mongodb_client[config["DB_NAME"]]


dbname = get_database()
collection_name = dbname["recipes"]


def get_recipes():
    recipes = [recipe for recipe in collection_name.find({})]

    return recipes


def save_recipe(recipe):
    collection_name.insert_one(recipe)
    print("Saved Recipe: ", recipe)


if __name__ == "__main__":
    dbname = get_database()
