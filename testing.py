from database_functions import get_recipes, delete_recipe, update_recipe, clear_database
from bs4 import BeautifulSoup
import urllib.request
import json
from utils.scrape_recipe import scrape_recipe

clear_database()

# recipes = get_recipes()
# print([recipe["_id"] for recipe in recipes])

# delete_recipe(recipes[0]["_id"])

# recipes = get_recipes()
# print([recipe["_id"] for recipe in recipes])

# update_recipe("64a419a8b6762c9e029ade95", {"name": "test2"})

all_recipe_names = []
all_recipe_links = []

page = 15
print("fetching page 1")
while page <= 34:
    if page % 5 == 0:
        print(f"fetching page {page}")
    html = urllib.request.urlopen(
        f"https://www.bbcgoodfood.com/search?tab=recipe&mealType=afternoon-tea%2Cbreakfast%2Cbrunch%2Cbuffet%2Ccanapes%2Ccheese-course%2Ccondiment%2Cdessert%2Cdinner%2Clunch%2Cmain-course%2Cpasta%2Cside-dish%2Csnack%2Csoup%2Csupper%2Cstarter%2Ctreat%2Cvegetable%2Cflatbreads%2Cside&diet=vegan&page={page}"
    ).read()
    soup = BeautifulSoup(html, "html.parser")

    articles = soup.find_all("article")

    recipes = [
        article for article in articles if article.get("data-item-type") == "recipe"
    ]

    # recipe_names = [recipe["data-item-name"] for recipe in recipes]

    # all_recipe_names += recipe_names

    recipe_links = [recipe.div.a["href"] for recipe in recipes]

    all_recipe_links += recipe_links

    page += 1

# print(all_recipe_names)

# for recipe_name in all_recipe_names:
#     formatted_recipe_name = "-".join(recipe_name.lower().split())

#     # print(formatted_recipe_name)

#     scrape_recipe(f"https://www.bbcgoodfood.com/recipes/{formatted_recipe_name}")

for recipe_link in all_recipe_links:
    print("trying ", recipe_link)
    scrape_recipe(f"https://www.bbcgoodfood.com{recipe_link}")
