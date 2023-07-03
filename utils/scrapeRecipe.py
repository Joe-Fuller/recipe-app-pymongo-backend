from bs4 import BeautifulSoup
import urllib.request

html = urllib.request.urlopen("https://www.bbcgoodfood.com/recipes/vegan-sponge").read()

soup = BeautifulSoup(html, "html.parser")

# scripts = soup.find_all("scripts")
scripts = soup.find_all(lambda tag: tag.name == "script" and "schema" in tag.text)
print(len(scripts))
