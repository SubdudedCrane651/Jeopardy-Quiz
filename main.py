import requests
import json
import pandas as pd
import random

url = "https://richard-perreault.com/Documents/JEOPARDY_QUESTIONS1.json"

response = requests.get(url)
data = json.loads(response.text)

count = len(data)

print(count)