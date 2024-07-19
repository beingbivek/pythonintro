import requests # pip install requests # easily requests for json
import json # handle json data

url = "https://jsonguide.technologychannel.org/quotes.json"

data = requests.get(url) # request data from url
quotes = json.loads(data.text) # data.text converts data to string and json loads helps to read json data

for quote in quotes:
    print(quote['text'])