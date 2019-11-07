# script to change the datarepresentation repo

import requests
import json
url = 'https://api.github.com/repos/datarepresentationstudent/aPrivateOne'
apiKey = '8c0e5202752a9f00b139b7d0f36bd79f7574197-5'
dataString = {"description": "Hello"}


response = requests.put(url, json=dataString, auth=('token',apiKey)) 
repoJSON = response.json()

print(response.json())