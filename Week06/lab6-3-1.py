from github import Github
import requests

g = Github("bcd73d53c81bb2ce925f0b62297f7452f5591a7b")

repo = g.get_repo('shkyler/grannys-garden')

fileInfo = repo.get_contents("test.txt") 
urlOfFile = fileInfo.download_url
#print(urlOfFile)

# get the content of test.txt
response = requests.get(urlOfFile)
contentOfFile = response.text

# change the content of the file
newContents = contentOfFile + "I am adding this with a script!"

#update the content of the file

gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents ,fileInfo.sha)
print (gitHubResponse)
