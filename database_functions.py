from pymongo import MongoClient
from dotenv import dotenv_values
from bson.objectid import ObjectId

config = dotenv_values(".env")


def get_database():
    mongodb_client = MongoClient(config["ATLAS_URI"])

    return mongodb_client[config["DB_NAME"]]


dbname = get_database()
collection = dbname["recipes"]


def get_recipes():
    recipes = [recipe for recipe in collection.find({})]

    return recipes


def save_recipe(recipe):
    collection.insert_one(recipe)
    print("Saved Recipe: ", recipe)


def delete_recipe(recipe_id):
    collection.delete_one({"_id": recipe_id})


def update_recipe(recipe_id, updates):
    collection.update_one({"_id": ObjectId(recipe_id)}, {"$set": updates}, upsert=True)


if __name__ == "__main__":
    dbname = get_database()
