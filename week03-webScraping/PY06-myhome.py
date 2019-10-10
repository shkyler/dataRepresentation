# web scraping from myhome.ie
# scraping page 2 of the south dublin properties
# https://www.myhome.ie/residential/mayo/property-for-sale?page=1

import requests
from bs4 import BeautifulSoup
import csv

page = requests.get("https://www.myhome.ie/residential/mayo/property-for-sale?page=1")
soup = BeautifulSoup(page.content, 'html.parser')

home_file = open('week03MyHime.csv', mode='w')
home_writer = csv.writer(home_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

listings = soup.findAll("div", class_="PropertyListingCard")

for listing in listings:
  entrylist = []
  #find the price and add it to the empty ist
  price = listing.find(class_="PropertyListingCard__Price").text 
  entrylist.append(price)
  # find the address and add it to the empty list
  address = listing.find(class_="PropertyListingCard__Address").text 
  entrylist.append(address)
 
  home_writer.writerow(entrylist)

home_file.close()