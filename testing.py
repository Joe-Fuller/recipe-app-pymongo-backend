from database_functions import get_recipes, delete_recipe, update_recipe
from bs4 import BeautifulSoup
import urllib.request
import json


# recipes = get_recipes()
# print([recipe["_id"] for recipe in recipes])

# delete_recipe(recipes[0]["_id"])

# recipes = get_recipes()
# print([recipe["_id"] for recipe in recipes])

# update_recipe("64a419a8b6762c9e029ade95", {"name": "test2"})


html = urllib.request.urlopen(
    "https://www.bbcgoodfood.com/recipes/collection/vegan-recipes"
).read()
soup = BeautifulSoup(html, "html.parser")

articles = soup.find_all("article")

recipes = [article for article in articles if article.get("data-item-type") == "recipe"]

recipe_names = [recipe["data-item-name"] for recipe in recipes]

print(recipe_names)
