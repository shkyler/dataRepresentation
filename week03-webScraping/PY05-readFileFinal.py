#import the libraries
from bs4 import BeautifulSoup
import csv

with open("../Week 02/Lab/cars-week-02.html") as fp:
  soup = BeautifulSoup(fp, "html.parser")

employee_file = open('week02data.csv', mode='w')
employee_writer = csv.writer(employee_file, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)

rows = soup.findAll("tr")
for row in rows:
  datalist = []
  cols = row.findAll("td")
  for col in cols:
    datalist.append(col.text)
  # here i modified the output so as not to output the 'update' or 'delete' buttons  
  employee_writer.writerow(datalist[0:3])

employee_file.close()  
