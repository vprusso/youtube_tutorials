import json

with open('..\\twitter_credentials.json') as f:
    creds = json.load(f)

for key in creds.keys():
    print(f"creds['{key}']")