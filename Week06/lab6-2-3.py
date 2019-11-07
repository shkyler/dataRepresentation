# script to pull information from my own repo

import requests
import json
url = 'https://api.github.com/repos/shkyler/grannys-garden'

apiKey = 'bcd73d53c81bb2ce925f0b62297f7452f5591a7-b'

response = requests.get(url, auth=('token',apiKey)) 
repoJSON = response.json()
#print (response.json())
file = open("grannys-garden", 'w') 
json.dump(repoJSON, file, indent=4)

