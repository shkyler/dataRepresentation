# api using an authentication key

import requests
import json

# read in the file
f = open("../Week 02/Lab/cars-week-02.html", "r")
html = f.read()
#print(html)

# set the api key and url
apiKey = '46ceed910c24ff7cce8240e89ec7b71912f6f40f2ec55fd217ce150ad6d4f1c4'
url = 'https://api.html2pdf.app/v1/generate'

# request
data = {'html': html,'apiKey': apiKey}
response = requests.post(url, json=data)

print(response.status_code)

# write the returned value to pdf
newFile = open("lab06.02.01.htmlaspdf.pdf", "wb")
newFile.write(response.content)
