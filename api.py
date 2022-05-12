import requests
import json

from pprint import pprint
url = "https://api.github.com"
org = input("Enter Organisation name : ")
Repo = input("Enter the Repo name : ")
response= f"https://api.github.com/repos/{org}/{Repo}/issues"
params = {
    "state": "all",
}

r = requests.get(response , params=params)
print(r)
rjson = r.json()
with open('results.json', 'w') as json_file:
    json.dump(rjson, json_file)
pprint(r.json())
data = json.loads(rjson)
print(json.dumps(data, indent =1))
