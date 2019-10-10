# 2nd exercise to open a html gile and use BS4 to view it
from bs4 import BeautifulSoup

with open("../Week 02/Lab/cars-week-02.html") as fp:
  soup = BeautifulSoup(fp,'html.parser')

print(soup.prettify())