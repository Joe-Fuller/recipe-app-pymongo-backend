from getDatabase import get_database

dbname = get_database()
collection_name = dbname["recipes"]


recipe_1 = {
    "name": "Trifle",
    "timeToCook": "1 Hour",
    "image": "http:image.com/recipeimage",
    "ingredients": [{"name": "milk", "amount": "2", "units": "cups"}],
    "instructions": ["Make trifle", "Serve trifle"],
}

collection_name.insert_one(recipe_1)
