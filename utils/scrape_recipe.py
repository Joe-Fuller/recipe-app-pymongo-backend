from bs4 import BeautifulSoup
import urllib.request
import json
from utils.save_recipe import save_recipe


def scrape_recipe(url):
    html = urllib.request.urlopen(url).read()

    soup = BeautifulSoup(html, "html.parser")

    scripts = soup.find_all(
        lambda tag: tag.name == "script" and "recipeIngredient" in tag.text
    )

    schema = scripts[0]
    text = schema.get_text()
    data = json.loads(text)

    recipeData = {
        "name": data["name"],
        "timeToCook": data["totalTime"],
        "ingredients": data["recipeIngredient"],
        "instructions": [x["text"] for x in data["recipeInstructions"]],
        "imageUrl": data["image"]["url"],
    }

    print(recipeData)

    save_recipe(recipeData)
