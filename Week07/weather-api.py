import requests, json

url = " http://api.weatherbit.io/v2.0/forecast/daily?key=bfc8d10fd32a4c8f9f4d791d59a51ec8&city=Dublin&country=Ireland"

apiKey = "bfc8d10fd32a4c8f9f4d791d59a51ec8"

response = requests.get(url)

data = response.json()
#print(data["data"])
repoJSON = response.json()
#print (response.json())
file = open("weather", 'w') 
json.dump(repoJSON, file, indent=4)