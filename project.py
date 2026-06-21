import requests
import json

response = requests.get("https://statsapi.mlb.com/api/v1/teams/143")

data = response.json()
print(json.dumps(data, indent=2))