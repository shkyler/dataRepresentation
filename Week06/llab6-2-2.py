# script to pull info from the datarepresentation repo

import requests
import json
url = 'https://api.github.com/repos/datarepresentationstudent/aPrivateOne'

apiKey = '8c0e5202752a9f00b139b7d0f36bd79f7574197-5'


response = requests.get(url, auth=('token',apiKey)) 
repoJSON = response.json()
#print (response.json())
file = open("test", 'w') 
json.dump(repoJSON, file, indent=4)