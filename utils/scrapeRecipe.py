from bs4 import BeautifulSoup
import urllib.request

html = urllib.request.urlopen("https://www.bbcgoodfood.com/recipes/vegan-sponge").read()

soup = BeautifulSoup(html, "html.parser")
print(soup)