#Reading data from the html filw

from bs4 import BeautifulSoup

with open("../Week 02/Lab/cars-week-02.html") as fp:
  soup = BeautifulSoup(fp,'html.parser')

#print(soup.tr)
rows = soup.findAll("tr")
for row in rows:
  print("------------")
  #print(row)
  datalist = []
  cols = row.findAll("td")
  for col in cols:
    datalist.append(col.text)
  print(datalist)  
