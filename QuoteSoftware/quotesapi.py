import requests
import json
from quote import Quote

def listquotes():
    return json.loads(requests.get("https://jsonguide.technologychannel.org/quotes.json").text)

def get_quotes():
    all_quotes = []
    for quote in listquotes():
        q = Quote(quote['text'],quote['from'])
        all_quotes.append(q)
    return all_quotes

def totalquotes():
    return len(get_quotes())