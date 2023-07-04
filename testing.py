from database_functions import get_recipes, delete_recipe, update_recipe

# recipes = get_recipes()
# print([recipe["_id"] for recipe in recipes])

# delete_recipe(recipes[0]["_id"])

# recipes = get_recipes()
# print([recipe["_id"] for recipe in recipes])

update_recipe("64a419a8b6762c9e029ade95", {"name": "test2"})
