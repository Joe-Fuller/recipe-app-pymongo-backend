from bs4 import BeautifulSoup
import urllib.request
import json
from utils.save_recipe import save_recipe
import split_ingredient_string


def scrape_recipe(url):
    html = urllib.request.urlopen(url).read()

    soup = BeautifulSoup(html, "html.parser")

    scripts = soup.find_all(
        lambda tag: tag.name == "script" and "recipeIngredient" in tag.text
    )

    schema = scripts[0]
    text = schema.get_text()
    data = json.loads(text)

    name = data["name"]
    timeToCook = data["totalTime"]
    ingredients = [
        split_ingredient_string(ingredient) for ingredient in data["recipeIngredient"]
    ]
    instructions = [instruction["text"] for instruction in data["recipeInstructions"]]
    imageUrl = data["image"]["url"]

    recipeData = {name, timeToCook, ingredients, instructions, imageUrl}

    print(recipeData)

    save_recipe(recipeData)
