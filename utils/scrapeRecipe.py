from bs4 import BeautifulSoup
import urllib.request

line = urllib.request.urlopen("https://www.bbcgoodfood.com/recipes/vegan-sponge").read()
print(line)

# soup = BeautifulSoup
