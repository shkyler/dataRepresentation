# First part of this weeks lab to test a request from a webpage
# import requests package
import requests
# import Beautiful Soup
from bs4 import BeautifulSoup
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print(page)
print("-----------")
print(page.content)
# Parse the html using beautiful soup
soup1 = BeautifulSoup(page.content, 'html.parser')
# Print out a pretty version of the source code
print("-----------")
print(soup1.prettify())