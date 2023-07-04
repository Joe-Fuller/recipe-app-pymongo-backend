from database_functions import get_recipes, delete_recipe

recipes = get_recipes()
print([recipe["_id"] for recipe in recipes])

delete_recipe(recipes[0]["_id"])

recipes = get_recipes()
print([recipe["_id"] for recipe in recipes])
