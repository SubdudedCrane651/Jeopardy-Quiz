import requests
import json
import pandas as pd
import random

url = "https://richard-perreault.com/Documents/JEOPARDY_QUESTIONS1.json"

response = requests.get(url)
data = json.loads(response.text)

count = len(data)
rand = random.randrange(1,count)
quiz = pd.DataFrame(data)

print("Category: "+quiz['category'][rand]+"\n"
+"Air Date: "+quiz['air_date'][rand]+"\n"
+"Question: "+quiz['question'][rand]+"\n"
+"Value :"+quiz['value'][rand]+"\n"
+"Round :"+quiz['round'][rand]+"\n"
+"Show number :"+quiz['show_number'][rand]+"\n")

input("<ENTER> for Answer")
print("Answer :"+quiz['answer'][rand])