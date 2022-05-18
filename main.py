import requests
import json
url = "https://api.github.com"
org = input("Enter Organisation name : ")
Repo = input("Enter the Repo name : ")
response= f"https://api.github.com/repos/{org}/{Repo}/issues"
params = {
    "state": "closed",
}
r = requests.get(response , params=params)
print(r)
rjson = r.json()
print(type(rjson))
leng = len(rjson)
print(leng)
with open('results.json', 'w') as json_file:
    json.dump(rjson, json_file)
f = open('results.json', "r")
# Reading from file
data = json.loads(f.read())
print(json.dumps(data, indent =1))
