import requests
import json

url = "https://richard-perreault.com/Documents/JEOPARDY_QUESTIONS1.json"

request = requests.get(url)
print(request.text)