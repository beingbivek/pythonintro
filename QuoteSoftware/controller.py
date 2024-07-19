import quotesapi
import random

allquotes = quotesapi.get_quotes()

def showallquotes():
    syntax = ""
    for data in allquotes:
        syntax = syntax + "\n" + data.quote + "\n" + "-" + data.author + "\n"
    return syntax

def randomquotes():
    return random.choice(allquotes)

def showquotebyid(index):
    return allquotes[index]