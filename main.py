import requests
import json

url = "https://richard-perreault.com/Documents/JEOPARDY_QUESTIONS1.json"

response = requests.get(url)
data = json(response.text)
print(data)
#print(response.text)