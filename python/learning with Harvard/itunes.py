import json
import sys
import requests

if len(sys.argv) != 2:
    print("need more arg")
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=" + sys.argv[1] + "&term=weezer")
o = response.json()
# print(json.dumps(o, indent = 6))
# print(f'outsise loop: {o["results"]}')
for result in o["results"]:
    print(f'Track Name: "{result["trackName"]}"')