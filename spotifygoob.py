import requests

with open("spotifyapikey.txt", "r") as tokenfile: 
    lines = [x.strip("\n") for x in tokenfile.readlines()]
id = lines[0]
key = lines[1]
print(id, key)
