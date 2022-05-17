#Requests will allow you to  can add content like headers, form data, multipart files, and parameters via simple Python libraries#
import requests
#file which is made of text in a programming language, is used to store and transfer the data#
import json
# Imort Pretty print to print data structures in a readable, pretty way for debugging code dealing with API requests#
from pprint import pprint
# for automate your workflows, build with the GitHub REST API#
url = "https://api.github.com"
#Enter the organization name and repo as input (Dynamic Variable)#
org = input("Enter Organisation name : ")
Repo = input("Enter the Repo name : ")
# Analyzing issue data with Github REST API#
response= f"https://api.github.com/repos/{org}/{Repo}/issues"
params = {
    "state": "all",
}
#We can request all the information we need from this object called Response r#
r = requests.get(response , params=params)
#print the response#
print(r)
#Load the package required to read JSON files#
rjson = r.json()
print(type(rjson))
# open the results.json file with argument w if doest exit in lib#
with open('results.json', 'w') as json_file:
#dump the data from json file#
    json.dump(rjson, json_file)
#pretty print the JSON object of the result#
pprint(r.json())
#use Python's json.load() and json.loads() methods to read JSON data from file and String#
data = json.loads(rjson)
print(json.dumps(data, indent =1))
